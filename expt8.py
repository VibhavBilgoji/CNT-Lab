import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_factors(p):
    factors = {}
    for i in range(2, p + 1):
        if isPrime(i) and p % i == 0:
            try:
                factors[i] += 1
            except KeyError:
                factors[i] = 1
            p //= i
            while p % i == 0:
                factors[i] += 1
                p //= i
    return factors

def fermatFact(n):
    i = 1
    while True:
        x = math.sqrt(n + i ** 2)
        if(x % 1 == 0):
            break
        i += 1
    x = int(x)
    print(f"n = {x}² - {i}² = ({x} + {i}) × ({x} - {i})")
    print(f"Factors of {n} are: {x+i} and {x-i}")

def pollardFact(n):
    a = 2
    b = int(input("Enter the bound (b): "))
    print(f"a = 2, b = {b}")
    g = math.gcd(a,n)
    print(f"gcd(a, n) is {g}")
    if(g > 1 and g < n):
        print(f"gcd(a, n) > 1, ∴ Factors of {n} are: {g} and {n//g}")
        return
    print("gcd(a, n) == 1, continuing...\n")
    print("Calculating aʲ mod n, for all primes j = 2 to b...")
    for j in range(2, b+1):
        if not isPrime(j):
            continue
        print(f"j = {j}    a = {a}", end = "    ")
        a = (a ** j) % n
        d = math.gcd(a-1, n)
        print(f"a = aʲ mod n = {a}    d = gcd(a-1, n) = {d}")
        if d > 1:
            print(f"gcd(a-1, n) > 1, ∴ Factors of {n} are: {d} and {n//d}")
            return
        print(f"No factors found for j = {j}, moving to the next prime...\n")
    print("No factors found using Pollard's p-1 method with the given bound.")

def findPairOfSquares(og, ini):
    b = ini
    prime_factors_set: list[dict[int, int]] = []
    while True:
        p = b ** 2 % og
        current_factors: dict[int, int] = generate_prime_factors(p)
        print(f"Prime factors of {b}² mod {og} are: ", end = "")
        for k, v in current_factors.items():
            print(f"({k} ^ {v}) * ", end = "")
        print("\b\b ")
        ptr = 0
        for f in prime_factors_set:
            all_even = True
            for i in current_factors.keys():
                try:
                    t = f[i]
                except KeyError:
                    t = 0
                if((t + current_factors[i]) % 2 != 0):
                    all_even = False
                    break
            for i in f.keys():
                try:
                    t = current_factors[i]
                except KeyError:
                    t = 0
                if((t + f[i]) % 2 != 0):
                    all_even = False
                    break
            if all_even:
                q = ini + ptr
                a = int(math.sqrt((q ** 2 % og) * p))
                return [b, q, a]
            ptr += 1
        prime_factors_set.append(current_factors)
        b += 1

def quadraticSieveFact(n):
    sqrt = math.sqrt(n)
    print(f"√n = {sqrt:.2f}", end = " ")
    sqrt = math.ceil(sqrt)
    print(f"Calculating squares from {sqrt}²...\n")
    #numbers starting from b
    [p, q, a] = findPairOfSquares(n, sqrt)
    print(f"\nFound a pair of squares: {p}² and {q}²")
    # a = int(math.sqrt((p**2) * (q**2)))
    print(f"Calculating a = √({p}² mod {n} * {q}² mod {n}) = {a}")
    b = p * q % n
    print(f"Calculating b = ({p} * {q}) mod n = {b}")
    x = math.gcd(a-b, n)
    y = math.gcd(a+b, n)
    print("\nCalculating factors using the pair of squares...")
    print(f"gcd(a-b, n) = {x}\ngcd(a+b, n) = {y}")
    if x > 1 and x < n:
        print(f"Factors of {n} are: {x} and {n//x}")
    elif y > 1 and y < n:
        print(f"Factors of {n} are: {y} and {n//y}")
    else:
        print("No factors found using the pair of squares.")

def main():
    n = int(input("Enter the integer to be factored (n): "))
    if(n <= 1):
        print("Please enter an integer greater than 1.")
        return main()
    while True:
        print("\nChoose the method to factor n:")
        print("1. Fermat's Factorization")
        print("2. Pollard's p-1 Algorithm")
        print("3. Quadratic Sieve Method")
        print("4. Enter another integer")
        print("0. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        else:
            if choice == 1:
                fermatFact(n)
            elif choice == 2:
                pollardFact(n)
            elif choice == 3:
                quadraticSieveFact(n)
            elif choice == 4:
                return main()
            elif choice == 0:
                print("Exiting the program...")
                return
            else:
                print("Invalid choice. Please select a valid option.")

main()