#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
def bul(x):
    toplam=0
    for i in range(1,x):
        if(x%i==0):
            toplam+=i
    return toplam

        
for i in range(1,1000,1):
    if bul(i)==i:
        print("bir mükodur",i)


