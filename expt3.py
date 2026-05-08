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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lde(a, b, c):
    print(f"\nEquation: {a}x + {b}y = {c}")
    d = gcd(a, b)
    print(f"GCD ({a}, {b}) = {d}\n")

    if (c % d != 0):
        return print(f"{c} is not divisible by {d}, so no solutions exist.\n")
    else:
        print(f"{c} is divisible by {d}, so solutions exist.\n")

    print(f"Step 1: Simplify the equation by dividing by GCD({a}, {b})")
    a, b, c = a // d, b // d, c // d
    print(f"Simplified equation: {a}x + {b}y = {c}\n")

    print(f"Step 2: Solve for s and t in the equation {a}s + {b}t = 1\n")
    s, t  = extended_gcd(a, b)
    print(f"∴ s = {s}, t = {t}\n")

    x, y = (c // d) * s, (c // d) * t
    print(f"\nParticular solution is: x = ({c}/{d}) * ({s}) = {x}, y = ({c}/{d}) * ({t}) = {y}")
    print(f"General Solution is: x0 = {x} + {b // d}K, y0 = {y} - {a // d}K\n")

    k = int(input("Enter an integer value for K to find a specific solution: "))
    x0, y0 = x + (b // d) * k, y - (a // d) * k
    return print(f"Specific solution for K = {k} is: x0 = {x0}, y0 = {y0}\n")

while True:
    print("Enter equation in the form ax + by = c (Press Ctrl + C to exit)")
    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
    except ValueError:
        print("Invalid Input! Please enter integers only.\n")
        continue
    except KeyboardInterrupt:
        print("\nExiting the program...")
        break
    else:
        lde(a, b, c)
