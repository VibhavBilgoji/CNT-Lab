def gcd(a, p):
    while p != 0:
        a, p = p, a % p
    return a

def FermatTest(p):
    a = int(input("Enter a (2 <= a < p): "))
    if a < 2 or a >= p:
        print("Invalid input. Please enter a: 2 <= a < p.")
    elif gcd(a, p) != 1:
        print(f"gcd({a}, {p}) != 1, so {p} is composite")
    else:
        y = pow(a, p-1, p)
        if y % p != 1:
            print(f"{y} % {p} != 1, so {p} is composite")
        else:
            print(f"{p} is probably prime")

def MillerRabinTest(p):
    a = 2
    if gcd(a, p) != 1:
        print(f"gcd({a}, {p}) != 1, so {p} is composite")
        return
    k = 0
    p_minus_1 = p-1
    while(p_minus_1 % 2 == 0):
        k+=1
        p_minus_1 /= 2
    m = (p-1) // (2 ** k)
    b = pow(a, m, p)
    if b == 1 or b == p-1:
        print(f"{p} is probably prime")
        return
    for i in range(k-1):
        b = pow(b, 2, p)
        if b % p == p-1:
            print(f"{p} is probably prime")
            return
    print(f"{p} is composite")

def SolovayStrassenTest(p):
    a = 2
    if(gcd(a, p) != 1):
        print(f"gcd({a}, {p}) != 1, so {p} is composite")
        return
    x = 1 if (p**2 - 1) // 8 % 2 == 0 else -1
    y = pow(a, (p-1) // 2, p)
    if x == 0:
        print(f"Jacobi symbol ({a}/{p}) = 0, so {p} is composite")
        return
    if y == x % p:
        print(f"{p} is probably prime")
    else:
        print(f"{y} != {x} mod {p}, so {p} is composite")

if __name__ == "__main__":
    p = int(input("Enter a number (p): "))

    while True:
        print("\n------Primality Test------")
        print("1. Fermat's Primality Test")
        print("2. Miller-Rabin Primality Test")
        print("3. Solovay-Strassen Primality Test")
        print("4. Enter another number")
        print("0. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        else:
            if choice == 1:
                FermatTest(p)
            elif choice == 2:
                MillerRabinTest(p)
            elif choice == 3:
                SolovayStrassenTest(p)
            elif choice == 4:
                p = int(input("\nEnter a number (p): "))
            elif choice == 0:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")