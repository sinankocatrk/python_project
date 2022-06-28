#Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

def bul(x,y):
    carpim=1
    for i in range(2,y,1):
        if(x%i==0 and y%i==0):
           carpim*=i 
    return carpim 
        


s1 = int (input("sayiyi giriniz "))
s2 = int (input("sayiyi giriniz "))

print(bul(s1,s2))



