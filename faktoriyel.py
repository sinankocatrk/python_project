
sayi= int (input("faktoriyeli alinacak sayiyi giriniz"))
carpim=1
a=1
while a<=sayi:
    carpim*=a
    a+=1

print("girilen deger: {} faktöriyeli {}".format(sayi,carpim))
