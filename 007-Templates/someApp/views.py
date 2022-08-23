from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request):
    print(request)
    print(request.method)
    print(request.COOKIES)
    print(request.path)
    print(request.user)
    print(request.META)
    {{ request.user }}
    html = "<h1>I am a heading 1</h1>"
    return HttpResponse(html)

#? Django uygulamalarında geriye bir html sayfası döndürmek için render() metodunu kullanıyor olmalıyız.
#? render() metodu ilk parametre olarak uygulamaya yapılan request nesnesini  parametre olarak alması gerekiyor. İkinci parametre olarak ise döndürülecek html sayfasının ismini alır.
#folder yapısı onemli app/templates/app/index.html

# def home(request):
#     return render(request, "someApp/index.html")

def home(request):
    context = {
        'caption': '0xkiichiro',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, "someApp/index.html", context)