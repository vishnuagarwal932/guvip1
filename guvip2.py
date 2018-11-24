a=1
try:
    n=int(input())
    if(0<=n<=20):
        for i in range(1,n+1):
            a=a*i
        print(a)
    else:
        print("Invalid input")
except ValueError:
    print("Invalid input")
