def primary():
    for i in range(2,20):
        for j in range(2 , i):
            if  i % j == 0:
                print(f"{i} number is not prime")
                break
        else:
            print(f"{i} number is prime ")

primary()
#example for "for else"