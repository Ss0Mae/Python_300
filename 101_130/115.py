n=int(input())
n=n-20
if(n>=0 and n<=255):
    print(n)
else:
    if(n<0): print("0")
    elif (n>255): print("255")