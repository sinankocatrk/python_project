
class öğrenci: 
    def __init__ (self,adi="bilgi yok",soyadi="bilgi yok",no="bilgi yok"):
        self.adi=adi
        self.soyadi=soyadi
        self.no=no

kisi1= öğrenci("sinan","kocaturk","2616")
print(kisi1.adi)
kisi2= öğrenci()
print(kisi2.adi)