from numpy import double
import krediKontrol
import krediListele

nameSurname=input("Adınız,Soyadını:")
print(f"Sn.{nameSurname},MIS Bank'a Hoş Geldiniz")

programDevam=1

while(programDevam==1):

    miktar=int(input("İstediğiniz Kredi Tutarı:"))
    krediListele.listele()
    krediTuru=int(input("Kredi Türünü Seçiniz(1-6):"))
    vade=int(input("Vade Süresi:"))
    krediNotu=double(input("Kredi Notunuzu Giriniz:"))
    hesapla=krediKontrol.kullanicidanAlinan(krediNotu,krediTuru,vade,miktar)
    if(krediTuru==1):
        hesapla.ihtiyacKredisi()
    elif(krediTuru==2):
        krediKontrol.kullanicidanAlinan.tasitKredisi()
    elif(krediTuru==3):
        krediKontrol.kullanicidanAlinan.konutKredisi()
    elif(krediTuru==4):
        krediKontrol.kullanicidanAlinan.dugunKredisi()
    elif(krediTuru==5):
        krediKontrol.kullanicidanAlinan.esnafKredisi()
    elif(krediTuru==6):
        krediKontrol.kullanicidanAlinan.ogrenciKredisi()
    else:
        print("Geçerli Bİr Kredi Türü Seçmediniz...")
    programDevam=int(input("Başa dönmek istiyor musunuz? [1(Evet)/2(Hayır)]"))
    if(programDevam==2):
        break
    

