def search():
    arr = [12,14,16,18,20,22,24,26,27,28]

    a = int(input("enter your number: "))

    for i in range(len(arr)):
        if a == arr[i]:
            print(f"found element {a} at {i}th position")
            break

        else:
            print(f"{a}is not the {i}th element")
            

search()
