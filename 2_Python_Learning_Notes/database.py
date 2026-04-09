import sqlite3

db = sqlite3.connect("kitaplar.db")  #python ile kitaplar.db arasında köprü kuran kişinin adı db
yetki = db.cursor()                  #kurduğumuz köprüde bir cursor(elçi) oluştur ve onun adı yetki oldu

kitabın_adı=input("Kitabın adını giriniz: ")
kitabın_sayfası=input("Kitabın sayfa sayısını giriniz: ")
kitabın_yılı=input("Kitabın yılını giriniz: ")

yetki.execute("CREATE TABLE IF NOT EXISTS kitaplar (adı, sayfa_sayısı, yılı)")

yetki.execute(f"INSERT INTO kitaplar VALUES ('{kitabın_adı}','{kitabın_sayfası}','{kitabın_yılı}')")

yetki.execute("SELECT * FROM kitaplar") # * FROM Tablodaki tüm sütunları (adı, sayfa_sayısı, yılı) getir demektir.
#yetki.execute("SELECT yılı FROM kitaplar") veya ("SELECT * FROM kitaplar WHERE yılı='2000' ") yazabilirsin.
yazdır=yetki.fetchall() #fetchmany(2) ise sadece istediğin kadar satırı gösterir.

for i in yazdır:
    print(f"\nKitap adı: {i[0]}, sayfa sayısı: {i[1]}, yılı: {i[2]}")

db.commit()     #kaydet demektir.
db.close()      #bilgisayarı yormadan kapatır.
