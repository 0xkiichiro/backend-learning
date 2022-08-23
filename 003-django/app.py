# VirtualEnv, projelerinizde gerekli olan paketleri sistemden bağımsız bir şekilde kurup, kullanmanızı sağlayacak sanal ortam sağlayan bir yapıdır.

# Örneğin, projenizde kullanmak istediğiniz modül sisteminizde yüklü fakat siz projenizde daha düşük veya daha yüksek bir sürümünü kullanmak istediniz ama direk sisteminize kurmak yerine, virtualenv sanal ortamı üzerine kurarak işiniz bittiğinde kaldırabilirsiniz. Bu sayede sisteminizde karışıklık yaratmamış olursunuz. Yüklemeleri tek komut satırıyla kaldırabilirsiniz.

18.08.2022_DJANGO_INTRO_NOTES :point_down::point_down:
:point_right: Django, Yüksek seviyeli bir backend framework'tür.
:heavy_check_mark: Free and open source web framework
:point_up_2: Django, çok kapsamlı bir community'ye sahip. O yüzden tercih ediliyor.
:red_circle: KİMLER KULLANIYOR: YouTube, Dropbox, reddit, Instagram, Quora, Spotify, DISQUS
:point_right: Framework, kendi environment'i olan, yazılmış olan kodları kullandığımız yapılardır. Patron framework.
:heavy_check_mark: Framework bizi fazla kod yazmaktan kurtarıyor.
:triangular_flag_on_post: Framework : Komple bir sistemdir, ekosistemdir, bazı koşulları vardır. Bu framework’u kullanmak istiyorsak bu kurallara uymamız gerekiyor.
:triangular_flag_on_post: Library : Örnek olarak react verebiliriz, JS library’dir. Onu alıp kullanabiliriz ve daha esnektir. Şartlarına zorlamıyor. Kullanırsan iyi olur der.
:point_right: Library'de ise kodu biz yazıyoruz.
:loudspeaker: Django' nun Avantajları
	:dash: Django' nun öğrenimi oldukça kolaydır.
	:dash: Django ile hazırlanmış web projeleri oldukça hızlıdır.
	:dash: Django projeleri modüler bir yapıya sahip olduğundan karmaşıklıktan uzak bir geliştirme ortamı sağlıyor.
	:dash: Django projesini oluşturduğunuz anda istediğiniz gibi özelleştirebilecek yönetim paneline sahipsiniz.
	:dash: Django framework'ü ile güvenlik açısından bir çok konu bizim adımıza düşünülmüş.
	:dash: Django framework'ünü kullanan oldukça popüler firmalar mevcut.
	:dash: Python popülerliğinden dolayı destek konusunda sıkıntı yaşanmıyor.
:loudspeaker: Django Nasıl Çalışıyor?
	:dash: Hazır template sunduğu için projeler çabuk yazılabiliyor.
	:dash: Kullanıcı bir adres girdiği zaman, "url.py" hangi VIEWS'e yönlendireceğine bakıyor.
	:dash: Eğer veritabanı üzerinden bi işlem yapılacaksa bu MODELS katmanında yapılıyor.
	:dash: MODELS katmanında yazdığımız Python kodları (CRUD işlemleri) ORM vasıtasıyla Database'e iletiliyor.
	:dash: TEMPLATES, Django'nun Frontend kısmı
:loudspeaker: Virtual Environment:
	:heavy_check_mark: Global'den bağımsız bir çalışma alanı oluşuyor.
	:heavy_check_mark: Bu alana Django kuruyoruz.
	:heavy_check_mark: Proje dosyasını kuruyoruz.
	:heavy_check_mark: İhtiyacımız olan package'ları ekliyoruz.
	:triangular_flag_on_post: Aradan belli bir zaman geçtikten sonra yeniden proje üzerinde çalışmaya başlağımız zaman Django ve paketlere güncelleme gelmiş olabilir.
	:triangular_flag_on_post: Güncel paketlerin çalışması için proje içinde bulunan requirenments'lar (requirements.txt), yeni oluşturulan sanal ortama aktarılarak güncellik sağlanmış oluyor.
	# VirtualEnv, projelerinizde gerekli olan paketleri sistemden bağımsız bir şekilde kurup, kullanmanızı sağlayacak sanal ortam sağlayan bir yapıdır.
	# Örneğin, projenizde kullanmak istediğiniz modül sisteminizde yüklü fakat siz projenizde daha düşük veya daha yüksek bir sürümünü kullanmak istediniz ama direk sisteminize kurmak yerine,
virtualenv sanal ortamı üzerine kurarak işiniz bittiğinde kaldırabilirsiniz. Bu sayede sisteminizde karışıklık yaratmamış olursunuz. Yüklemeleri tek komut satırıyla kaldırabilirsiniz.
:loudspeaker: Difference between project and app
	:triangular_flag_on_post: Bir proje tüm web sitesini temsil ederken, bir uygulama temelde projenin bir alt modülüdür.
	:triangular_flag_on_post: Tek bir proje birden fazla uygulama içerebilirken, bir uygulama farklı projelerde de kullanılabilir.
	:triangular_flag_on_post: Bir proje, tüm web uygulamasının bir planı gibidir, uygulamalar ise bir web uygulamasının yapı taşlarıdır.
	:triangular_flag_on_post: Genellikle içinde bir veya daha fazla uygulama bulunan web sitemiz için tek bir proje oluştururuz.
	:triangular_flag_on_post: Bir proje, tüm web uygulamasıyla ilgili yapılandırma ve ayarları içerir. Öte yandan, uygulamalar bağımsız olabilir veya birbirleriyle ilişkili olabilir