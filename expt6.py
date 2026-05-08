def sub(i):
    subscript_map = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(i).translate(subscript_map)

def generator_LC():
    print("\n---Linear Congruential Generator---")
    a = int(input("Enter the multiplier (a): "))
    b = int(input("Enter the increment (b): "))
    n = int(input("Enter the modulus (n): "))
    seed = int(input("Enter the seed value (X₀): "))
    random_numbers = []
    for _ in range(b):
        seed = (a * seed + b) % n
        random_numbers.append(seed)
    print("Generated random numbers using Linear Congruential Generator:")
    for i in range(b):
        print(f"X{sub(i)}: {random_numbers[i]}")
    print("-----------------------------------", end="\n\n")

def generator_BBS():
    print("------Blum Blum Shub Generator------")
    p = int(input("Enter prime number p (p ≡ 3 mod 4): "))
    q = int(input("Enter prime number q (q ≡ 3 mod 4): "))
    s = int(input("Enter random seed value s: "))
    num_bits = int(input("Enter number of bits to generate: "))

    n = p * q
    x_prev = (s**2) % n
    bits = []

    print("\nSolution: ")
    print(f"n = {p} * {q} = {n}")
    print(f"X₀ = {s}\u00b2 mod {n} = {x_prev}\n")

    for i in range(num_bits):
        xi = (x_prev**2) % n
        bi = xi % 2
        bits.append(bi)
        print(f"X{sub(i+1)} = {xi},\tB{sub(i+1)} = {bi}")
        x_prev = xi

    print("\nNumber =", end=" ")
    for b in bits:
        print(b, end="")
    print("\n-----------------------------------", end="\n\n")

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