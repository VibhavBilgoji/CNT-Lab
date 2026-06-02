import math

def calcPower(a, b, n, p, q, sym):
    print(f"{a}^({q}x) ≡ {b}^{q} (mod {n})")
    print(f"{a}^({q}{sym}) × {a}^({p*q}a₁) ≡ {b}^{q} (mod {n})")
    print(f"{a}^({q}{sym}) ≡ {b}^{q} (mod {n})")
    aq = pow(a, q, n)
    print(f"{a}^{q} ≡ {aq} (mod {n})")
    bq = pow(b, q, n)
    print(f"{b}^{q} ≡ {bq} (mod {n})")
    print(f"{aq}^{sym} ≡ {bq} (mod {n})")
    if bq == 1:
        return 0
    elif aq == bq:
        return 1
    else:
        a0 = 2
        temp = aq
        while a0 < p:
            temp = (temp * aq) % n
            if temp == bq:
                return a0
            a0 += 1
        if a0 == p:
            return

def main():
    print("\nEnter equation in the form aˣ ≡ b (mod n)")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    n = int(input("Enter n: "))
    pohligHellman(a, b, n)

def pohligHellman(a, b, n):
    if math.gcd(a, n) != 1:
        print("a and n must be coprime for Pohlig-Hellman algorithm to work.")
        return
    n -= 1
    p = 1
    q = 1
    while p < n:
        p += 1
        if n % p == 0:
            q = n // p
            if math.gcd(p, q) == 1:
                break
    if(p == n):
        print("Failed to find coprime factors p and q.")
        return
    print(f"{n} = {p} × {q}")
    print(f"p = {p}, q = {q}\n")
    n += 1 #restore n
    print(f"let x = a₀ + {p}a₁")
    print("Calculating a₀...")
    a0 = calcPower(a, b, n, p, q, "a₀")
    if a0 is None:
        print("Failed to calculate a₀.")
        return
    print(f"x ≡ {a0} (mod {p})\n")

    print(f"let x = b₀ + {q}b₁")
    print("Calculating b₀...")
    b0 = calcPower(a, b, n, q, p, "b₀")
    if b0 is None:
        print("Failed to calculate b₀.")
        return
    print(f"x ≡ {b0} (mod {q})\n")
    print("Using CRT to combine results...")
    print(f"a₁ = {a0}, a₂ = {b0}, M₁ = {q}, M₂ = {p}")
    y1 = q % p
    y2 = p % q
    i = 1
    while i * y1 % p != 1:
        i += 1
    invM1 = i
    i = 1
    while i * y2 % q != 1:
        i += 1
    invM2 = i
    print(f"M₁⁻¹ = {invM1} (mod {p}), M₂⁻¹ = {invM2} (mod {q})")
    x = (a0 * q * invM1 + b0 * p * invM2) % (n-1)
    print("x = (a₀ × M₁ × M₁⁻¹ + b₀ × M₂ × M₂⁻¹) mod n")
    print(f"x = ({a0} × {q} × {invM1} + {b0} × {p} × {invM2}) mod {n-1}\n")
    print(f"The solution to the equation is: x ≡ {x} (mod {n-1})")

while True:
    main()
    cont = input("Do you want to solve another equation? (Enter y to continue): ")
    if cont.lower() != 'y':
        print("Exiting...")
        break