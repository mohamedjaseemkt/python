def primary():
    for i in range(2, 20):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{i} is a prime number")

primary()
