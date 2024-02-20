

def primary():
    a = int(input("enter number: "))
    for j in range(2 , a):
        if  a % j == 0:
            print(f"{a} number is not prime")
            break
    else:
        print(f"{a} number is prime ")

primary()