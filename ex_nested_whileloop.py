size = 5

outer_counter = 0

while outer_counter < size:
    inner_counter = 0

    while inner_counter < size:
        print("*", end=" ")
        inner_counter += 1

    print()  # move to the next line after printing a row
    outer_counter += 1
