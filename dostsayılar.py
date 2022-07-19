def dost(sayi1,sayi2):
    bolenler1=bolenler2=1
    for i in range(2,sayi1//2+1):
        if sayi1%i==0:
            bolenler1+=i
    for i in range(2,sayi2//2+1):
        if sayi2%i==0:
            bolenler2+=i
    if bolenler1==sayi2 and bolenler2==sayi1:
       return True
    else: return False    
    



sayi1=int(input("sayı 1i giriniz: "))
sayi2=int(input("sayi 2yi giriniz: "))

          
                
if dost(sayi1, sayi2):
    print("sayılar dost sayılardır")
else:
    print("sayı dost sayılar değildir")
