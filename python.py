tab
shift tab
a,b=b,a
i=+=i
yorum # tekli
"""
fsdfs
"""
4**3             64 bastırır

a[4:10] 4 ten 9a alır
a[:-1] sonuncu karakteri almaz	
a[::2] 	2şer atlar 
a[::-1] tersten yazar
len(a)

str()
float()
int()

print(35,"merhaba",32)
type(35)
a= "sinan"
print(type(a))
print(35,45,23,523,sep="/")
print("T","B","M","M",sep=".")
print(*"TBMM",sep=".")
 
a=3
b=4
print("{} + {} 'nin toplami {} dir".format(a,b,a+b))

liste.pop()
liste.append() sona karakter ekler
liste.sort() sıralama
liste.sort(reverse= True)

liste= ["abi",nba,faf,fsvs]
liste.sort()

liste= [[1,2],[3,4],[5,6]]

liste [1] 
[3,4]

liste [2][1]
3

Demetler (Tupplelar) : değiştirilemezler define
demet= (1,2,3,4,5,6)
demet[4]
5
demet.count(1) #demet içinde kaç tane 1 var onu bulur
demet.index(3) # demet demetinin içindeki 3'ün yerini gösterir
2


sozluk :dictionary
sozluk1={"bir":1,"iki":2}

sozluk1={"bir":1,"iki":2}
print(sozluk1["bir"])

sozluk1.keys()
sozluk1.values()
sozluk1.items() #demetler olarak verir

a=input("değer giirniz")
print("kulanicinin girdigi deger",a)

a=int(input("lutfen deger giriniz"))

print("toplamları",a+b+c)





a=input("isim girinz")

b=input("soy girinz")

c=input("takim girinz")

liste=[a,b,c]

print("isminiz {}\nsoyisim {}\ntakiminiz {}\n".format(liste[0],liste[1],liste[2]))





a=int(input("a girinz"))

b=int(input("b girinz"))

c=int(input("c girinz"))

d=(b*b)-(4*a*c)

print("sonuc:d",d)



Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

a=int(input("ilk deger"))
b=int(input("2.deger"))
c=int(input("3. deger"))


print("{} x {} x {} = {}".format(a,b,c,a*b*c))


Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
a= int(input("aracınız km de ne kdar yakıyor)"))
b= int(input("kaç km yol gittiniz)"))

c=(a**2+b**2)**0.5
print("deger",c)



print("{} x {} x {} = {} dir".format(a,b,c,çarpım))

a = None

1<2 and "Murat" == "Murat"
True

1<2 or "Murat" != "Murat"
True

not 2==2
False


yas=int(input("yas girin"))

if yas<18:
    print("yasiniz 18den gücük ")
elif yas>=18:
    print("hg knk")
	
a=int(input("1. girin"))
b=int(input("2. girin"))
c=int(input("3. girin"))

if a>b and a>c:
    print("en büyük",a)
elif b>c and b>a:
    print("en büyük",b)
elif c>a and c>b:
    print("en büyük",b)
	
5 in [1,2,3,4]
false

4 in [1,2,3,4]
true

"p" in "python"
true



liste = [1,2,3]

for eleman in liste:
	print(eleman)
1
2
3

for eleman in veri_yapisi(liste,demetvs):
	yapilacak işlemler


i=0
while(i<10):
    print("i'nin değeri",i)
    i+=1

index=0
while(index<len(liste)):
    print("index {}. eleman karşılığı {}".format(index,liste[index]))
    index+=1
	
print(*range(0,100))

print(*range(1,100,2))

print(*range(20,0,-1))

liste= list(range(11))

list comprehension 
liste4 =[i*2 for i in liste]
print(liste4)

liste2= list[x for i in liste for x in i]


liste5 = [[2,32,52,32,423],[4234,23423,423,4],[23,4,324,2]]
for i in liste5:
    for x in i:
        print(x)



sayi= int (input("faktoriyeli alinacak sayiyi giriniz"))
carpim=1
for i in range(1,sayi+1):
    carpim*=i
print(carpim)



sayi= int (input("faktoriyeli alinacak sayiyi giriniz"))
carpim=1
a=1
while a<=sayi:
    carpim*=a
    a+=1

print("girilen deger: {} faktöriyeli {}".format(sayi,carpim))


#recursive rakam toplama bulma
def bul(x):
    if x<=0:
        return 0
    return x%10 + bul(x//10)

x=131
print(bul(x))


def bul(isim="isimsiz"):
    print("selam",isim)
bul()


def topla (*a):
    toplam=0
    for i in a:
        toplam+=i
    print(toplam)

topla(1,32,25,325,235,2,523,5,23,32)




c=10
def topla ():
    global c
    c=5
topla()
print (c)


def ikiylecarp(x):
	return x*2
print(ikiylecarp(3))




