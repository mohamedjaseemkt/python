numbers = [1,2,3,4,5,6,7,8,9,10,11]

a = int(input("enter a number"))

for num in numbers:
    if num == a:
        print(f"your searching element founded {num}")
        break
    print(num)

else:
    print("your searching element not founded")