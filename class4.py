
class öğrenci: 
    def __init__ (self,adi="bilgi yok",soyadi="bilgi yok",no="bilgi yok"):
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
    pass

kisi1= yönetici("sinan","kocaturk","2616")

print(kisi1.göster())



