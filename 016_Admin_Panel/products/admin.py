from django.contrib import admin
from .models import Product
from django.utils import timezone

# Register your models here.

# admin.site.register(Product)

# admin.site.site_title = "Clarusway Title"
# admin.site.site_header = "Clarusway Admin Portal"  
# admin.site.index_title = "Welcome to Clarusway Admin Portal"
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock", )
    # list_display_links = ("create_date", ) #can't add items in list_editable to here
    list_filter = ("is_in_stock", "create_date")
    ordering = ("name",)  
    search_fields = ("name",)
    prepopulated_fields = {'slug' : ('name',)}   # when adding product in admin site
    list_per_page = 20
    date_hierarchy = "update_date"
    # fields = (('name', 'slug'), 'description', "is_in_stock") #fieldset kullandığımız zaman bunu kullanamayız
    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago")  

    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description",),
            'description' : "You can use this section for optionals settings"
        })
    )

    
    actions = ("is_in_stock", )

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
        
    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'

    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days

admin.site.register(Product, ProductAdmin)