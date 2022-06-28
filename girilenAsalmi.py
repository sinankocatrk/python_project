
def bul(x):
    
    for i in range(2,x):
        if (x%i==0):
            return 0
    return 1




sayi = int (input("sayi giriniz"))

y=bul(sayi)

if (y==1):
    print("sayi asaldir")
elif(y==0):
    print("sayi asal değildir")
