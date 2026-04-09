takım = "Galatasaray"
takım2 = "Fenerbahçe"
print(takım,takım2)
print(type(takım))
yaş=str(20)
print(str(yaş)+takım)

büyükharfler= "NE MUTLU TÜRKÜM DİYENE".lower() #.upper() ise büyük yapar
print(büyükharfler) #.capitalize() sadece ilk harfi büyük yapar
print(büyükharfler.count("t")) #.swapcase() büyükse küçük küçükse büyük yapar
print(büyükharfler.replace("e","x")) #.replace() karakter değiştirir 

sil="Merhaba ---".strip("-") #.strip() siler
print(sil.strip("M"))

print("rümeysa", "esra", sep="-") #virgül yerine istediğini koyar
print("rümeysa", "esra", end="***") #sona karakter ekler 
print("\nTuttuğum takım:", takım, "sevmediğim takım:", takım2)
print(f"Tuttuğum takım: {takım} sevmediğim takım: {takım2}")

#kullanıcısifresi = input("Şifrenizi giriniz: ")
#print("Şifreniz:", kullanıcısifresi)

listeler = ["elma", "armut", "muz"] # len(listeler) uzunluk gösterir
print(listeler[0]) #index 0'dan başlar 
listeler.append("çilek") #listenin sonuna ekler
listeler[2] = "karpuz" #index ile muz değiştirir
listeler[:2] = ["üzüm", "kavun"] #ilk ikisini değiştirir
listeler[0:2] = [] #ilk iki elemanı siler
for i in listeler:
    print(i)

for sayı in range(2,5): #2'den 4'e kadar sayılar
    print(sayı)    

tuple = ("a", "b", 3, "d") #demetler değiştirilemez
print(tuple[-2])

müşteri = 15
if müşteri<18:
    print("Reşit değilsiniz.")
elif müşteri==18:
    print("Yeni reşit oldunuz.")  
else:
    print("Reşitsiniz.")

sayi=1
while sayi<=5:
    print("Sayı:",sayi)
    sayi+=1

ayırma = "rümeysa-esra-güngören" #ayırma = ayırma.split("-") .split() karaktere göre ayırır
print(ayırma[2])
for i in ayırma.split("-"):
    print(i[0], end=" ")

def kullanıcıbilgileri(ad,soyad,yaş="belirtilmedi"):
    print(f"Adınız:{ad}, soyadınız:{soyad} , yaşınız: {yaş}" )

kullanıcıbilgileri("Rümeysa Esra","Güngören",20) 

sözlük = {"Galatasaray": "63 Puan", "Fenerbaçe": "59 Puan"}
#takim=input("Takım adı giriniz:").capitalize()
#print(sözlük.get(takim, "Bu takımın puanı bulunmamaktadır."))
sözlük.setdefault("Beşiktaş","55 Puan")
sözlük.pop("Fenerbaçe")
for i,j in sözlük.items():
    print(i,j)
