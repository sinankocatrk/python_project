sayi = int (input("sayiyi giriniz"))
toplam=0
for i in range(1,sayi):
    if (sayi%i==0):
        toplam+=i

if(toplam==sayi):
    print("{} sayisi bir mükemmel sayidir".format(sayi))
else:
    print("{} sayisi bir mükemmel sayi değildir".format(sayi))