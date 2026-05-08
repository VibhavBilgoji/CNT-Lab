def generator_LC():
    print("\n---Linear Congruential Generator---")
    a = int(input("Enter the multiplier (a): "))
    b = int(input("Enter the increment (b): "))
    n = int(input("Enter the modulus (n): "))
    seed = int(input("Enter the seed value (x0): "))
    random_numbers = []
    for _ in range(b):
        seed = (a * seed + b) % n
        random_numbers.append(seed)
    print("Generated random numbers using Linear Congruential Generator:")
    for i in range(b):
        print(f"x{i+1}: {random_numbers[i]}")
    print()

def generator_BBS():
    print("BBS Generator")
    p = int(input("Enter prime p (p=3 mod 4): "))
    q = int(input("Enter prime q (q=3 mod 4): "))
    s = int(input("Enter random number s: "))
    num_bits = int(input("Enter number of bits to generate: "))

    n = p * q
    x_prev = (s**2) % n
    bits = []

    print("\nsolution:")
    print(f"n = {p} * {q} = {n}")
    print(f"X0 = {s}^2 mod {n} = {x_prev}")

    for i in range(1, num_bits + 1):
        xi = (x_prev**2) % n
        bi = xi % 2
        bits.append(bi)
        print(f"X{i} = (X{i-1}^2) mod {n} = ({x_prev}^2) mod {n} = {xi}")
        print(f"B{i} = X{i} mod 2 = {xi} mod 2 = {bi}")
        x_prev = xi

    print("number=", end="")
    for b in bits:
        print(b, end="")
    print()

while(True):
    print("1. Linear Congruential Generator")
    print("2. Blum Blum Shub Generator")
    print("0. Exit")
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    else:
        if choice == 1:
            generator_LC()
        elif choice == 2:
            generator_BBS()
        elif choice == 0:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")