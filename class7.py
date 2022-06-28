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
    def __str__(self):
        return "isim {}\nsoyisim: {}\nno {}\n".format(self.adi,self.soyadi,self.no)
        


kisi1 = öğrenci("sinan","kocaturk","2616")

print (kisi1)



