#super: miras aldığımız sınıfın metodlarını alt siniflardan kullanmamızı sağlar
class öğrenci: 
    def __init__ (self,adi="bilgi yok",soyadi="bilgi yok",no="bilgi yok"):
        print("öğrenci sinifininin initine girdi")
        self.adi=adi
        self.soyadi=soyadi
        self.no=no
    def göster(self):
        print(self.adi)
        print(self.soyadi)
        print(self.no)
    def numaradeğiş(self,yeninumara):
        self.no=yeninumara
        
class yönetici(öğrenci):
    def __init__ (self,adi="bilgi yok",soyadi="bilgi yok",no="bilgi yok",medenidurum="bilgi yok"):
        print("yönetici sinifininin initine girdi")
        super().__init__(adi,soyadi,no)

        self.medenidurum = medenidurum
    def numaradeğiş(self,yeninumara):
        self.no=yeninumara
    def med_değiş(self,medenidurum):
        if("evli"==self.medenidurum):
            self.medenidurum="bekar"
        if("bekar"==self.medenidurum):
            self.medenidurum="evli"

kisi1 = yönetici("sinan","kocaturk","2616","evli")

print(kisi1.medenidurum)
yönetici.med_değiş(kisi1.medenidurum)
print(kisi1.medenidurum)


