def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

while True:
    n = int(input("Enter the number of equations of the form x ≡ a mod m (Enter 0 to exit): "))
    if(n <= 0):
        print("Exiting the program...")
        break

    a, m, M, M_inv = [0] * n, [0] * n, [0] * n, [0] * n
    M_total = 1
    print("Enter the values of a and m: ")
    for i in range(n):
        a[i] = int(input(f"Enter a{i+1}: "))
        m[i] = int(input(f"Enter m{i+1}: "))
        M_total *= m[i]

    for i in range(n):
        for j in range(n):
            if i != j:
                gcd = get_gcd(m[i], m[j])
            else:
                gcd = 1

            if gcd != 1:
                print(f"m{i+1} and m{j+1} are not coprime (GCD = {gcd})")
                print("∴ CRT cannot be applied.")
                exit()

    for i in range(n):
        M[i] = M_total // m[i]
        M_inv[i] = M[i] % m[i]

        y = 1
        while((M_inv[i] * y) % m[i] != 1):
            y += 1
        M_inv[i] = y

    x = 0
    for i in range(n):
        x += (a[i] * M[i] * M_inv[i])

    x %= M_total
    print(f"The solution to the system of equations is: x ≡ {x} mod {M_total}\n")