class galeri:
    araç_km= 95000
    araç_markası="Toyota"
    araç_rengi="Kırmızı" 

    def araba_özellikleri(self): #dışardan bir veri alacağın zaman self yaz. Nesne oluşturduğumuzda hangisini çağırdığımızı bilmek için lazım
        print(f"Araç kilometresi: {self.araç_km} , Araç markası: {self.araç_markası}, Araç rengi: {self.araç_rengi} ")


a_otomativ= galeri()    #galeri sınıfından bir nesne oluşturduk. Aynı sınıftan bir sürü nesne oluşturabiliriz.
a_otomativ.araba_özellikleri() #bu nesneden fonksiyonu çağırıyoruz.



class okul:
    def __init__(self,şube, öğretmen, mevcut, bölüm):  #parantez içi istek listesidir, nesne oluştururken bunları eklemelisin.
        self.şube = şube     #sağdaki şube dışardan gelen geçiçi bilgi (9-F), ama soldaki hafızada kalıcı
        self.öğretmen = öğretmen #Dışardan gelen şube bilgisini al benim self.şube'me yerleştir. 
        self.mevcut= mevcut
        self.bölüm= bölüm

    def okul_bilgileri(self):
        print(f"Şube Adı: {self.şube}, Öğretmen Adı: {self.öğretmen}, Sınıf Mevcudu: {self.mevcut}, Ders: {self.bölüm}")    

    def branş_değiş(self):
        yeni_branş= input("Lütfen yeni branşınızı giriniz: ")
        print(f"Eski branş: {self.bölüm}")
        self.bölüm=yeni_branş 
        print(f"Branşınız güncellendi. Yeni branş: {self.bölüm}")
        print(f"Şube Adı: {self.şube}, Öğretmen Adı: {self.öğretmen}, Sınıf Mevcudu: {self.mevcut}, Yeni Ders: {self.bölüm}")


ilk_sınıf=okul("9-F", "Merve Evyapan", "4", "Fizik")
ilk_sınıf.okul_bilgileri()    
ilk_sınıf.branş_değiş()    



class sporokulu (okul):
    print("Spor Okuluna Hoşgeldiniz. Okulumuzun adı Miras(İnheritance)")
    def __init__(self,şube,öğretmen,mevcut,bölüm, maaş): 
        super().__init__(şube,öğretmen,mevcut,bölüm) #Ben hepsini aldım yukardakilerin MİRAS yaptım ama ekleme de yapmak istiyorum diyip maaşı ekledim.
        self.maaş=maaş


    def okul_bilgileri(self):
        super().okul_bilgileri() 
        print(f"Maaş: {self.maaş}")    #AYNI FONKSİYON İSMİ AMA SEN ONA EKLEME YAPINCA OVERRİDİNG OLUYOR
        #class Robot: def calis(self): # ÜSTTE BU İSİMDE BİR ŞEY VAR  print("Robot çalışıyor...")
        #class TemizlikRobotu(Robot): def calis(self): # <--- 2. İŞTE OVERRIDING BURASI! İsim aynı, görev farklı. print("Robot şu an yerleri süpürüyor...")
     

basketbol_sınıf= sporokulu ("9-B", "Sinan Yılmaz", "22", "Basketbol Antrenörü", "10 BİN")
basketbol_sınıf.okul_bilgileri()
