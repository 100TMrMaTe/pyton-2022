import math
import sys

a=int(input("kérem az a változot?"))
while a==0:
    print("kérek egy számot ami nem 0-a")
    a=int(input("kérem az a változot?"))
b=int(input("kérem a b változot?"))
c=int(input("kérem a c változot?"))
try:
    x1=(-b - math.sqrt(b**2 -4 * a * c))/(2 * a)
    x2=(-b + math.sqrt(b**2 -4 * a * c))/(2 * a)
except ValueError:
    print("nincs megoldás!")
    sys.exit()
    
print(f"{x1:.2f}")
print(f"{x2:.2f}")

