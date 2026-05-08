def printFormatted(args):
    print(end="|")
    for arg in args:
        print(f" {arg:>7}", end=" |")


def printBorder(count):
    print("-", end="")
    for i in range(count):
        print("-" * 10, end="")  # 10 = width + 2 spaces + 1 border
    print()


def extendedEuclids(a, b):
    if a > b:
        r1, r2 = a, b
    else:
        r1, r2 = b, a

    s1, s2 = 1, 0
    t1, t2 = 0, 1

    printBorder(10)
    printFormatted(("q", "r1", "r2", "r", "s1", "s2", "s", "t1", "t2", "t"))
    while r2 != 0:
        q = r1 // r2
        r = r1 - q * r2
        s = s1 - q * s2
        t = t1 - q * t2

        input()
        printFormatted((q, r1, r2, r, s1, s2, s, t1, t2, t))

        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t

    input()
    printFormatted(("-", r1, r2, "-", s1, s2, "-", t1, t2, "-"))
    print()
    printBorder(10)

    gcd, x, y = r1, s1, t1
    print(f"\nGCD = {gcd}, x = {x}, y = {y}")
    print(f"Verification: {a}*({x}) + {b}*({y}) = {gcd}")


def euclids(a, b):
    if a > b:
        r1, r2 = a, b
    else:
        r1, r2 = b, a

    printBorder(4)
    printFormatted(("q", "r1", "r2", "r"))
    while r2 != 0:
        q = r1 // r2
        r = r1 - q * r2

        input()
        printFormatted((q, r1, r2, r))

        r1 = r2
        r2 = r

    input()
    printFormatted(("-", r1, r2, "-"))
    print()
    printBorder(4)
    gcd = r1
    print(f"\nGCD = {gcd}")


while True:
    print("Select a choice: ")
    print("1. Euclid's Algorithm")
    print("2. Extended Euclid's Algorithm")
    print("0. Exit")
    try:
        choice = int(input("Enter choice: "))

        if choice == 0:
            print("Exiting the program...")
            break

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == 1:
            euclids(num1, num2)
        elif choice == 2:
            extendedEuclids(num1, num2)
        else:
            print("Invalid Choice!")
    except ValueError:
        print("Invalid Input!")
