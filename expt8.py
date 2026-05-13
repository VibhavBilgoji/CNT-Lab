import math
from operator import indexOf

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
    print(f"Prime factors of {p} are: {factors}")
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
    print("Calculating a^j mod n, for all primes j = 2 to b...")
    for j in range(2, b+1):
        if not isPrime(j):
            continue
        print(f"j = {j}\ta = {a}")
        a = (a ** j) % n
        d = math.gcd(a-1, n)
        print(f"a =  aʲ mod n = {a}\td = gcd(a-1, n) = {d}")
        if d > 1:
            print(f"gcd(a-1, n) > 1, ∴ Factors of {n} are: {d} and {n//d}")
            return
        print(f"No factors found for j = {j}, moving to the next prime...")
    print("No factors found using Pollard's p-1 method with the given bound.")

def quadraticSieveFact(n):
    b = math.sqrt(n);
    print(f"√n = {b:.2f}", end = " ")
    b = math.ceil(b)
    print(f"Calculating squares from {b}²...")
    #numbers starting from b
    prime_factors_set = []
    found = False
    ogB = b
    x = 0
    y = 0
    while not found:
        p = b ** b
        current_factors = generate_prime_factors(p)
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
            if all_even:
                idx = indexOf(prime_factors_set, f)
                x = b
                y = ogB+idx
                found = True
                break
        if found:
            break
        prime_factors_set += [current_factors]
        b += 1

    print(f"Found a pair of squares: {x}² and {y}²")
    #TODO: find the factors using x and y

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