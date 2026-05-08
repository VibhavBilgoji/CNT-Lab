import matplotlib.pyplot as plt

def setup_table(columns, rows):
    fig, ax = plt.subplots()
    ax.axis("tight")
    ax.axis("off")
    table = ax.table(cellText=rows, colLabels=columns, loc="center", cellLoc="center", colColours=["orange"] * len(columns), cellColours=[["lightblue"] * len(columns)] * len(rows))
    table.scale(1.2, 1.2)

def euclids(a, b):
    rows, columns, step = [], ["Step", "q", "r1", "r2", "r"], 0
    r1, r2 = (a, b) if (a > b) else (b, a)
    while r2 != 0:
        q = r1 // r2
        r = r1 - q * r2
        step += 1
        rows.append([step, q, r1, r2, r])
        r1 = r2
        r2 = r
    step += 1
    rows.append([step, "-", r1, r2, "-"])
    gcd = r1
    setup_table(columns, rows)
    plt.title("GCD using Euclid's Algorithm")
    plt.figtext(0.5, 0.02, f"GCD = {gcd}", ha="center", fontsize=12)
    plt.show()

def extended_euclids(a, b):
    rows, columns, step = [], ["Step", "q", "r1", "r2", "r", "s1", "s2", "s", "t1", "t2", "t"], 0
    r1, r2, s1, s2, t1, t2 = a, b, 1, 0, 0, 1
    while r2 != 0:
        q = r1 // r2
        r, s, t = r1 - q * r2, s1 - q * s2, t1 - q * t2
        step += 1
        rows.append([step, q, r1, r2, r, s1, s2, s, t1, t2, t])
        r1, s1, t1 = r2, s2, t2
        r2, s2, t2 = r, s, t
    step += 1
    rows.append([step, "-", r1, r2, "-", s1, s2, "-", t1, t2, "-"])
    gcd, x, y = r1, s1, t1
    setup_table(columns, rows)
    plt.title("GCD using Extended Euclid's Algorithm")
    plt.figtext(0.5, 0.02, f"GCD = {gcd}, x = {x}, y = {y}\nVerification: {a}*({x}) + {b}*({y}) = {gcd}", ha="center", fontsize=12)
    plt.show()

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
            print()
        elif choice == 2:
            extended_euclids(num1, num2)
            print()
        else:
            print("Invalid Choice!")
    except ValueError:
        print("Invalid Input!")
