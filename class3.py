
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

kisi1= öğrenci("sinan","kocaturk","2616")

print(kisi1.göster())

kisi1.numaradeğiş(1613)
print(kisi1.göster())

