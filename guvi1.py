str=input()
if(len(str)<=100000):
    str=str[::-1]
    print(str)
else:
    print("Invalid input")
