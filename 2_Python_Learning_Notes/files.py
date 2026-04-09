#dosya = open("deneme.txt","w")
#dosya.write("MERHABA")
#Eğer deneme.txt diye bir dosya yoksa sıfırdan oluşturur. 
#Eğer dosya zaten varsa ve içinde yazılar varsa w modu dosyayı açtığı anda içindekileri tamamen siler.
#Senin yeni yazdıklarını ekler. Yani dosyayı her seferinde sıfırlar.


#with open("deneme.txt","a", encoding ="utf-8") as dosya:
 #dosya.write("SELAM")
#Eğer dosya yoksa, o da sıfırdan oluşturur.
#Ama dosya zaten varsa içindeki eski bilgilere dokunmaz. 
#Yeni yazdıklarını eskilerin altına ekler.


#with open("deneme.txt","r", encoding="utf-8") as dosya:     #türkçe karakterlere izin verir
 #a = dosya.read()   dosyayı yazıyor
 #print(a)
 #b= dosya.readline()  dosyadaki ilk satırı yazıyor
 #print(b)
 #c=dosya.readlines()
 #print(c[4])


#with open("deneme.txt","r+") as dosya:
    #x=dosya.read()         #bir değişken oluşturduk ve bu değişkene tüm dosyayı okuttuk
    #dosya.seek(0)          #dosyanın 0. baytına geri dön
    #x="2. çşöı\n" + x      #artık değişkenimizin başına bunu ekledik sonra da ilk baştaki dosyamızı ekledik
    #dosya.write(x)         #ve oluşturduğumuz x'i dosyamıza yazdır
    #print(x)


with open("deneme.txt","r+") as dosya:
    x=dosya.readlines()              #lines çünkü satırları array olarak alıyoruz
    x.insert(2,"İKİNCİ index\n")     #insert demek bu veriyi araya sıkıştır demek, burda 2. index e sıkıştırcak
    dosya.seek(0)                    
    dosya.writelines(x)