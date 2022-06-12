"""
kredi notu
kreti türü
vade
miktar
"""
a=1.5
class kullanicidanAlinan:
    def __init__(self,krediNotu,krediTuru,vade,miktar):
        self.krediNotu=krediNotu
        self.krediTuru=krediTuru
        self.vade=vade
        self.miktar=miktar
    def ihtiyacKredisi(self):
        faizOrani=1.89
        if(self.krediNotu>=1.2 and self.krediNotu<=10):
            if(self.vade>=1 and self.vade<=36):
                if(self.miktar<=50000 and self.miktar>=1000):
                    bankaKazanci=self.miktar*(faizOrani/100)*self.vade
                    toplamGeriOdeme=self.miktar+bankaKazanci
                    aylikOdeme=toplamGeriOdeme/self.vade
                    print(f"Kredi Tutarı:{self.miktar}\nVade:{self.vade} Aylık Ödenecek Tutar:{aylikOdeme}\nToplam Geri Ödeme:{toplamGeriOdeme}")
                else:
                    print("İhiyaç kredisi kredi tutarı min: 1000 TL- max: 50.00 TL")
            else:
                print("İhiyaç kredisi min: 1 Ay max:36 Ay")
        else:
            print("İhtiyaç kredisi gerekli puan min:1.2")
    def tasitKredisi(self):
        faizOrani=1.72
        if(self.krediNotu>=2 and self.krediNotu<=10):
            if(self.vade>=24 and self.vade<=60):
                if(self.miktar<=124000 and self.miktar>=40000):
                    bankaKazanci=self.miktar*(faizOrani/100)*self.vade
                    toplamGeriOdeme=self.miktar+bankaKazanci
                    aylikOdeme=toplamGeriOdeme/self.vade
                    print(f"Kredi Tutarı:{self.miktar}\nVade:{self.vade} Aylık Ödenecek Tutar:{aylikOdeme}\nToplam Geri Ödeme:{toplamGeriOdeme}")
                else:
                    print("Taşıt kredisi kredi tutarı min: 40.000 TL- max: 124.00 TL")
            else:
                print("Taşıt kredisi min: 1 Ay max:60 Ay")
        else:
            print("Taşıt kredisi gerekli puan min:2")
    def konutKredisi(self):
        faizOrani=1.24
        if(self.krediNotu>=3 and self.krediNotu<=10):
            if(self.vade>=36 and self.vade<=120):
                if(self.miktar<=350000 and self.miktar>=100000):
                    bankaKazanci=self.miktar*(faizOrani/100)*self.vade
                    toplamGeriOdeme=self.miktar+bankaKazanci
                    aylikOdeme=toplamGeriOdeme/self.vade
                    print(f"Kredi Tutarı:{self.miktar}\nVade:{self.vade} Aylık Ödenecek Tutar:{aylikOdeme}\nToplam Geri Ödeme:{toplamGeriOdeme}")
                else:
                    print("Konut kredisi kredi tutarı min: 100.000 TL- max: 350.000 TL")
            else:
                print("Konut kredisi min: 36 Ay max:120 Ay")
        else:
            print("Konut kredisi gerekli puan min:3")
    def dugunKredisi(self):
        faizOrani=1.78
        if(self.krediNotu>=1.8 and self.krediNotu<=10):
            if(self.vade>=12 and self.vade<=60):
                if(self.miktar<=350000 and self.miktar>=50000):
                    bankaKazanci=self.miktar*(faizOrani/100)*self.vade
                    toplamGeriOdeme=self.miktar+bankaKazanci
                    aylikOdeme=toplamGeriOdeme/self.vade
                    print(f"Kredi Tutarı:{self.miktar}\nVade:{self.vade} Aylık Ödenecek Tutar:{aylikOdeme}\nToplam Geri Ödeme:{toplamGeriOdeme}")
                else:
                    print("Düğün kredisi kredi tutarı min: 50.000 TL- max: 350.000 TL")
            else:
                print("Düğün kredisi min: 12 Ay max:60 Ay")
        else:
            print("Düğün kredisi gerekli puan min:1.8")
    def esnafKredisi(self):
        faizOrani=1.95
        if(self.krediNotu>=2 and self.krediNotu<=10):
            if(self.vade>=12 and self.vade<=60):
                if(self.miktar<=350000 and self.miktar>=50000):
                    bankaKazanci=self.miktar*(faizOrani/100)*self.vade
                    toplamGeriOdeme=self.miktar+bankaKazanci
                    aylikOdeme=toplamGeriOdeme/self.vade
                    print(f"Kredi Tutarı:{self.miktar}\nVade:{self.vade} Aylık Ödenecek Tutar:{aylikOdeme}\nToplam Geri Ödeme:{toplamGeriOdeme}")
                else:
                    print("Esnaf kredisi kredi tutarı min: 50.000 TL- max: 350.000 TL")
            else:
                print("Esnaf kredisi min: 12 Ay max:60 Ay")
        else:
            print("Esnaf kredisi gerekli puan min:3")
    def ogrenciKredisi(self):
        faizOrani=1.15
        if(self.krediNotu>=1.6 and self.krediNotu<=10):
            if(self.vade>=1 and self.vade<=12):
                if(self.miktar<=1000 and self.miktar>=1000):
                    bankaKazanci=self.miktar*(faizOrani/100)*self.vade
                    toplamGeriOdeme=self.miktar+bankaKazanci
                    aylikOdeme=toplamGeriOdeme/self.vade
                    print(f"Kredi Tutarı:{self.miktar}\nVade:{self.vade} Aylık Ödenecek Tutar:{aylikOdeme}\nToplam Geri Ödeme:{toplamGeriOdeme}")
                else:
                    print("Öğrenci kredisi kredi tutarı min: 1000 TL- max: 5.000 TL")
            else:
                print("Öğrenci kredisi min: 1 Ay max:12 Ay")
        else:
            print("Öğrenci kredisi gerekli puan min:1.6")

