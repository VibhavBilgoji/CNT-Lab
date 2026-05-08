def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes_till(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]
    num, primes = 5, [2,3]
    while num <= n:
        if is_prime(num):
            primes.append(num)
        num += 2
    return primes

def totient(n):
    if n == 1:
        return 1
    if is_prime(n):
        return n - 1
    primes, pfs, res = primes_till(n//2), [], 1
    for i in range(len(primes)):
        p = primes[i]
        while True:
            if n % p == 0:
                pfs.append(p)
                n //= p
            else:
                break
        count = pfs.count(p)
        if count:
            res *= (p ** count - p ** (count - 1))
    return res

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a,b):
    print(f"|Step|{"q":^6}|{"r1":^6}|{"r2":^6}|{"r":^6}|", end="")
    print(f"{"s1":^6}|{"s2":^6}|{"s":^6}|{"t1":^6}|{"t2":^6}|{"t":^6}|")
    step = 0
    r1, r2, s1, s2, t1, t2 = a, b, 1, 0, 0, 1
    while r2 != 0:
        q = r1 // r2
        r, s, t = r1 - q * r2, s1 - q * s2, t1 - q * t2
        step += 1
        print(f"|{step:^4}|{q:^6}|{r1:^6}|{r2:^6}|{r:^6}|", end="")
        print(f"{s1:^6}|{s2:^6}|{s:^6}|{t1:^6}|{t2:^6}|{t:^6}|")
        r1, s1, t1 = r2, s2, t2
        r2, s2, t2 = r, s, t
    step += 1
    print(f"|{step:^4}|{'_':^6}|{r1:^6}|{r2:^6}|{'_':^6}|", end="")
    print(f"{s1:^6}|{s2:^6}|{'_':^6}|{t1:^6}|{t2:^6}|{'_':^6}|")
    return s1, t1

def linear_congruence(a, b, n):
    a, b = a % n, b % n
    print(f"\nEquation: {a}x ≡ {b} (mod {n})")
    d = gcd(a, n)
    if b % d != 0:
        return print(f"{b} is not divisible by {d}, so no solutions exist.\n")
    else:
        print(f"Number of solutions is equal to GCD(a, n) = {d}\n")
    while True:
        print("Select method to solve the linear congruence: ")
        print("""
            1. Extended Euclidean Algorithm
            2. Euler's Totient function
            3. Modular Multiplicative Inverse
            4. Enter new equation
            0. Exit
            """)
        try:
            inp = int(input("Enter method: "))
            if(inp == 0):
                print("Exiting the program...")
                return True
            elif inp == 1:
                EEA_method(a, b, n, d)
            elif inp == 2:
                totient_method(a, b, n, d)
            elif inp == 3:
                MI_method(a, b, n, d)
            elif inp == 4:
                return False
            else:
                print("Invalid choice! Please try again.\n")
                continue
            print()
        except ValueError:
            print("Invalid Input! Please enter integers only.\n")

def EEA_method(a, b, n, d):
        print("Solving using Extended Euclidean Algorithm:\n")
        print(f"Simplify the equation by dividing by GCD({a}, {n}) = {d}")
        a, b, n = a // d, b // d, n // d
        print(f"Simplified equation: {a}x ≡ {b} (mod {n})")
        print(f"\nSolve for s and t in the equation {a}s + {n}t = 1")
        s, t  = extended_gcd(a, n)
        print(f"∴ s = {s}, t = {t}\n")
        x0 = (b * s) % n
        print(f"Particular solution is: x0 = ({b} * {s}) mod {n} = {x0}")
        for i in range(1, d):
            print(f"General solution {i} is: x{i} = ", end="")
            print(f"({x0} + {i} * {n * d}/{d}) mod {n * d} = {(x0 + i * n) % (n * d)}")

def totient_method(a, b, n, d):
    print("Solving using Euler's Totient function:\n")
    ϕ = totient(n)
    print(f"Euler's Totient function ϕ(n) = ϕ({n}) = {ϕ}\n")
    x0 = (a ** (ϕ - 1)) * b % n
    print(f"Particular solution is: x0 = ({a} ^ (ϕ({n}) - 1)) * {b} mod {n} = {x0}")
    for i in range(1, d):
        print(f"General solution {i} is: x{i} = ", end="")
        print(f"({x0} + {i} * {n}/{d}) mod {n} = {(x0 + i * (n // d)) % n}")

def MI_method(a, b, n, d):
    print("Solving using Modular Multiplicative Inverse:\n")
    print(f"Simplify the equation by dividing by GCD({a}, {n}) = {d}")
    a, b, n = a // d, b // d, n // d
    print(f"Simplified equation: {a}x ≡ {b} (mod {n})\n")
    print(f"Calculate the modular multiplicative inverse y in {a}y ≡ 1 (mod {n})")
    y = 1
    while True:
        if (a * y) % n == 1:
            break
        y += 1
    print(f"∴ y = {y}\n")
    x0 = (b * y) % n
    print(f"Particular solution is: x0 = ({b} * {y}) mod {n} = {x0}")
    for i in range(1, d):
        print(f"General solution {i} is: x{i} = ", end="")
        print(f"({x0} + {i} * {n * d}/{d}) mod {n * d} = {(x0 + i * n) % (n * d)}")

while True:
    print("Enter a equation in the form ax ≡ b (mod n) (Press Ctrl + C to exit): ")
    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        n = int(input("Enter the value of n: "))
    except ValueError:
        print("Invalid Input! Please enter integers only.\n")
        continue
    except KeyboardInterrupt:
        print("\nExiting the program...")
        break
    else:
        if linear_congruence(a, b, n):
            break
