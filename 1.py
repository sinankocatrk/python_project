karar=input("ücgen mi dortgen mi girmek istiyorsunuz?")

if karar=="3":
    print("3 deger girin")
    a=int(input())
    b=int(input())
    c=int(input())
    if (not(a+b>c and b+c>a and c+a>b)):
        print("bu bir ucgen belirtmez")
    elif(a==b and b==c and a==c):
        print("bu bir eşkenar ücgen")
    elif (a==b and (a!=c or b!=c) or  b==c and(a!=b or a!=c) or a==c and (b!=a or b!=c)):
        print("bu bir ikizkenar ücgen")

        
elif karar=="4":
    print("4 deger girin")
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    if(a==b and b==c and c==d):
        print("bu bir kare")
    elif(a==b and c==d or a==c and b==d or a==d and b==c):
        print("bu bir dikdortgen")
    else:
        print("bu bir dortgendir")
	