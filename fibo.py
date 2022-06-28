sayi= int (input("kaçinci fibo sayisini istediğinizi giriniz"))
a=1
b=1
sayac=2
while sayac<sayi:
    temp=b
    b=b+a
    a=temp
    sayac+=1
print(b)

    