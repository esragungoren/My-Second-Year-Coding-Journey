import locale
import subprocess
locale.setlocale(locale.LC_ALL,"")

import subprocess
subprocess.call("calc.exe")


subprocess.call("calc.exe") #hesap makinesini açar, bunun gibi diğer uyg. açabilirsin

import phonebook as esra #veya import phonebook     from phonebook import topla
esra.topla()                   #phonebook.topla()         topla()
#bunu çağırırken diğer tüm kodlarda gelebiliyor o yüzden fonksiyonları ayrı yere yazmak daha mantıklı.                        

import random
a=random.uniform(0,1)  #arasında sayı seçer
print(round(a*10,2))   #artık 0 ile 10 arası sayı seçer, virgülden sonra 2 basamak gösterir

random.randint(20,100) #20 ve 100 dahil tam sayı seçer 

liste=["Rümeysa", "Esra", "Güngören", 2005, "Adıyaman"]
b=random.choice(liste)
print(b)

print(random.sample(liste,2))

random.shuffle(liste)
for i in liste:
    print(i)

from datetime import datetime
a = datetime.now()    
b = a.strftime("%A") #a.day a.month a.hour a.minute
print(b)

#import içe aktar demek, git kütüphanenden bul ve dosyayı benim şu an yazdığım kodun içine getir.
#sonra import ettiğin dosyayı çağırıyorsun ismiyle ve sonra nokta(.) ve fonksiyonun adı
#from datetime: Python kütüphanesine git ve adı datetime olan modülü dosyayı bul. 
#import datetime: Dosyanın içinden, yine adı datetime olan sınıfı (aracı) al ve koduma getir.    