# 20.08.2022_MODELS

Django, bir web framework'tür.

Dolayısıyla hem front hem de backend tarafı yapılabiliyor

Django template etiketleri, Python benzeri yapıların HTML'ye aktarılmasını sağlar,
böylece dinamik web sitelerini daha kolay ve hızlı oluşturabiliriz!

Virtual environment'ın tek amacı çalışma ortamının boyutunu küçültmek değildir.
Virtual environment, farklı projelerdeki paketleri yönetmeye yarar.
Virtual environment kullanmak, global olarak paket yükledikten sonra çıkabilecek
sorunları ortadan kaldırır. Bu tür hatalardan kaçınmak için Python uygulamaları geliştirirken
her zaman virtual environmentkullanılması önerilir.

proje => apartmanın temeli
app => apartmanın daireleri

MODEL => Database Tables # model = class = table

Django'da model, özel bir çeşit nesnedir database içinde kaydedilir.

Burası, kullanıcılar, blog gönderilerimiz, vb. hakkında bilgileri saklayacağımız yerdir.

Verilerimizi depolamak için SQLite veritabanını kullanıyor olacağız.

SQLite, Django için varsayılan veritabanıdır
Veritabanındaki bir modeli, sütünları (alan adı) ve satırları (veri) olan bir hesap tablosuna (spreadsheet) benzetebiliriz.

Backend'in esas görevi Frontend ile DB arasında köprü oluşturmaktır.

Database ile ilişkiyi SQL sorguları ile değil Python kodu ile yapıcaz.

ORM sayesinde kod bloklarımız içerisinde yazdığımız SQL işlemlerini otomatik olarak sınıflarımız üzerinden gerçekleştirebiliriz.

Oluşturduğumuz sınıflar veritabanındaki tablolara, sınıflara ait property’ler ise veritabanındaki ilgili tablonun kolonlarını temsil etmektedir.

Bu sayede veritabanındaki verilere de ait olduğu sınıflar üzerinden erişilebilmektedir.

Inheritance (Miras-Kalitim), bir sinifin temel anlamda yapacagi is ve eylemleri baska bir siniftan kalitim almasidir.

ForeignKey - Many-to-one
Bir yazar birden fazla makale yazabilir.
Bir makale yalnızca bir yazar tarafından yazılabilir.
Django migration ları denilince akla ilk olarak veritabanı şemasını doğrudan etkileyen kavramlar gelir.
Bir modele yeni bir alan eklemek, bazı alanların özelliklerini değişen ihtiyaçlara göre değiştirmek vs.
Django bu değişiklikleri takip eder, migration dosyaları oluşturur, uygular ve veritabanınızı kolayca yeni
şemasına geçirmenize yardımcı olur.

Bunun yanında migrationlar varolan şema içersindeki verileri düzenlemek veya taşımak
için de kullanılabilir. Bu tip migrationlar data migrations olarak adlandırılır.

Şemayı ilgilendirmedikleri için Django tarafından takip edilmezler, geliştirici tarafından
oluştururlar fakat normal şema migrationları gibi yürütülürler ve sistemin bir parçasıdırlar.

MODEL'LERDE KULLANACAĞIMIZ 2 TEMEL KOMUT

python manage.py makemigrations
Ben bir class (model) oluşturdum, Sen gereğini yap.

python manage.py migrate
Bu komutla database'de hazırladığımız tabloyu oluşturuyor.

python manage.py createsuperuser
Bu kod ile oluşturduğumuz tabloda işlem yapabilmek için bir admin oluşturuyoruz.

Admin panelde tabloyu görebilmek ve işlem yapabilmek için admin.py dosyasının içinde hazırladığımız tabloyu import ediyoruz
from .models import Student
admin.site.register(Student)
blank = Form da boş bırakmaya izin ver/Verme
null = DB de null kaydet/kaydetme
auto_now :point_right: her bir güncellemede en son tarihi alıyor
auto_now_add :point_right: create ederken alıyor sadece
