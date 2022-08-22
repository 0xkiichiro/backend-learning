from django.db import models

# Create your models here.

class Student(models.Model):
    COUNTRIES = [
        ("TR", "TURKEY"),
        ("US", "UNITED STATES"),
        ("DE", "GERMANY"),
        ("FR", "FRANCE"),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField("Surname", max_length=30)
    number = models.IntegerField("Number")
    about = models.TextField("about", blank=True, null=True)
    country = models.CharField("Country", max_length=2, choices=COUNTRIES)
    avatar = models.ImageField('Resim', blank=True, null=True, upload_to='media/')
    registered_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Studentzki"

# s1 = Student.objects.create(number=2, last_name....) # hem oluşturur hem kaydeder.
# q1 = Student(last_name.....) #oluştur. q1.save() ile kaydet...
# g1 = Student.objects.get(number=1)  # tek kayıt döndürür filtreleme birden fazla kayıt 
# #dönecekse filter kullanılır.
# f1 = Student.objects.filter(number=1) # sorguya uyan bütün kayıtları getirir.
# f2 = Student.objects.exclude(number=1) # number'ı 1'e eşit olmayanlar gelir

#! https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups