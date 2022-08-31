from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):    
    return render(request, "user_example/home.html")

@login_required
def special(request):
    return render(request, "user_example/special.html")

def register(request):
    #! the line below does the same exact thing the 3 lines below commented out
    form = UserCreationForm(request.POST or None)
    # form = UserCreationForm()
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()

        username = form.cleaned_data.get("username")
        # password1 is coming from the name from the html section
        password = form.cleaned_data.get("password1")

        user = authenticate(username=username, password=password)
        
        login(request, user)
        return(redirect("home"))

    else:
        form = UserCreationForm()

    context = {
        "form": form
    }

    return render(request, "registration/register.html", context)


def password_change(request):
    if request.method == 'POST':
        # We will use user change form this time
        # Import it
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = UserChangeForm()
    
    context = {
        'form': form
    }
    
    return render(request, "registration/password_change.html", context)