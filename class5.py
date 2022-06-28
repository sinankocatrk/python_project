#overriding: dış class üzerinde yenilikler
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
        self.adi=adi
        self.soyadi=soyadi
        self.no=no
        self.medenidurum = medenidurum
    def numaradeğiş(self,yeninumara):
        self.no=yeninumara

kisi1= yönetici("sinan","kocaturk","2616")

print(kisi1.adi)



