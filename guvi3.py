r=0
try:
    n=int(input())
    while(n>0):
        rm=n%10
        r=r*10+rm
        n=n//10
    print(r)
except ValueError:
    print("Invalid input")
