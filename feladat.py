a=0
a=int(input("hány számot szeretnél összeadni? "))
while a <2 or a >5:
    print("Hiba! Kérek, egy 2 és 5 közötti számot adj meg.")
    a=int(input("Hány számot szeretnél összeadni? "))
if a==2:
    szam1 = int(input("1. szám: "))
    szam2 = int(input("2. szám: "))
    print("A megadott 2 szám összege: "+str(szam1+szam2))
elif a==3:
    szam1 = int(input("1. szám: "))
    szam2 = int(input("2. szám: "))
    szam3 = int(input("3. szám: "))
    print("A megadott 3 szám összege: "+str(szam1+szam2+szam3))
elif a==4:
    szam1 = int(input("1. szám: "))
    szam2 = int(input("2. szám: "))
    szam3 = int(input("3. szám: "))
    szam4 = int(input("4. szám: "))
    print("A megadott 4 szám összege: "+str(szam1+szam2+szam3+szam4))
elif a==5:
    szam1 = int(input("1. szám: "))
    szam2 = int(input("2. szám: "))
    szam3 = int(input("3. szám: "))
    szam4 = int(input("4. szám: "))
    szam5 = int(input("5. szám: "))
    print("A megadott 5 szám összege: "+str(szam1+szam2+szam3+szam4+szam5))
