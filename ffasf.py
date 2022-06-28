

liste= [1,32,34,32,53,2,33]
for eleman in liste:
    if eleman%2==0:
        print(eleman)

toplam=0
s= "sinan slşdfafsdfs"
for i in s:
    if (i=="a"):
        toplam+=1
print("toplam a sayisi",toplam)

if "ythan" in "Python": 
    print ("doğru")

i=0
while(i<10):
    print("i'nin değeri",i)
    i+=1

index=0
while(index<len(liste)):
    print("index {}. eleman karşılığı {}".format(index,liste[index]))
    index+=1
print(*range(20,0,-1))

for i in range(1,5):
    print (i)

for i in range(6):
    print("* " *i )

liste4 =[i*2 for i in liste]
print(liste4)

liste5 = [[2,32,52,32,423],[4234,23423,423,4],[23,4,324,2]]
for i in liste5:
    for x in i:
        print(x)