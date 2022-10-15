def binary(n):
    if(n>1):
        binary(n//2)
    x=n%2
    print(x,end="")

def octal(n):
    if(n>1):
        octal(n//8)
    x=n%8
    print(x,end="")


dec=int(input("Enter the Decimal Number:"))
print("Binary Number: ",end="")
binary(dec)
print()
print("Octal Number: ",end="")
octal(dec)
