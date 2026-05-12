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
        print(f"Check {a}^({p}-1) mod {p}")
        y = pow(a, p-1, p)
        print(f"{a}^({p}-1) mod {p} = {y}")
        if y != 1:
            print(f"{y} != 1, therefore {p} is composite")
        else:
            print(f"{y} = 1, {p} is probably a prime")

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
    print(f"Write p-1 as 2^k * m: {p-1} = 2^{k} * {m}")
    b = pow(a, m, p)
    print(f"Compute initial witness: {a}^{m} mod {p} = {b}")
    if b == 1 or b == p-1:
        if(b == 1):
            print(f"b = 1, therefore {p} is probably a prime")
        else:
            print(f"b = p-1, therefore {p} is probably a prime")
        return
    for i in range(k-1):
        b = pow(b, 2, p)
        if b == p-1:
            print(f"b = p-1, therefore {p} is probably a prime")
            return
    print(f"Did not find 1 or n-1. therefore{p} is composite")

def SolovayStrassenTest(p):
    a = 2
    if(gcd(a, p) != 1):
        print(f"gcd({a}, {p}) != 1, so {p} is composite")
        return
    x = 1 if (p**2 - 1) // 8 % 2 == 0 else -1
    print(f"Calculate Jacobi Symbol ({a}/{p}) = {x}")
    y = pow(a, (p-1) // 2, p)
    print(f"Compute a^((p-1)/2) mod p: {a}^{p-1} mod {p} = {y}")
    if x == 0:
        print(f"Jacobi symbol ({a}/{p}) = 0, so {p} is composite")
        return
    if y == x % p:
        print(f"{y} == {x} mod {p}, therefore {p} is probably a prime")
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