sayi= int (input(" sayiyi giriniz"))
temp=sayi
sayac=0
while 0<sayi:
    sayac+=1
    sayi//=10

print(sayac)
tm=sayac
toplam = 0 
while 0<sayac: 
    x=sayi/10
    y=x**tm
    toplam+=y
    sayac-=1
print(sayac)