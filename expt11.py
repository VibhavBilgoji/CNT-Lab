import math
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_key(n):
    i = 1
    while i < n:
        if n % i == 0 and isPrime(i):
            break
        i += 2
    j = i + 2
    while j < n:
        if n % j == 0 and isPrime(j):
            break
        j += 2
    if i == n or j == n:
        print(f"{n} is a prime number, so it cannot be factored further.")
        exit(1)
    phi_n = (i-1) * (j-1)
    e = 2
    while e < phi_n:
        if math.gcd(e, phi_n) == 1:
            break
        e += 1
    d = 1
    while (d * e) % phi_n != 1:
        d += 1
    return e, d

def process(text, key):
    firstA = False
    try:
        msg = int(text)
        if text[0] == '0' and text[1] == '0':
            firstA = True
    except ValueError:
        msg = 0
        if text[0] == 'A':
            firstA = True
        for c in text.replace(" ", "").upper():
            i = alpha.index(c)
            msg = msg * 100 + i
        print("Plaintext in integer:", msg)
    c = ""
    msg = str(msg)
    if firstA:
        c += "00"
    for i in range(0, len(msg), 2):
        bits = int(msg[i:i+2])
        cBits = pow(bits, key[0], key[1]) % 26
        if cBits < 10:
            c += "0"
        c += str(cBits)
    return c

def getN():
    n = int(input("Enter an integer n (Ctrl + C to exit): "))
    keys: tuple[int, int] = generate_key(n)
    print(f"Public key (e, n): ({keys[0]}, {n})")
    print(f"Private key (d, n): ({keys[1]}, {n})")
    return n, keys

def main(n, keys):
    print("\nChoose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        m = input("\nEnter the plaintext: ")
        c = process(m.upper(), (keys[0], n))
        print(f"Ciphertext: {c}\n")
    elif choice == 2:
        c = input("\nEnter the ciphertext: ")
        m = process(c.upper(), (keys[1], n))
        print(f"Plaintext: {m}\n")
    else:
        print("\nInvalid choice. Exiting.")
        raise KeyboardInterrupt
    print("Choose an option:")
    print("1. Enter another text")
    print("2. Enter different keys")
    choice = int(input("Choose option: "))
    if choice == 1:
        main(n, keys)
    elif choice == 2:
        return

if __name__ == "__main__":
    try:
        while True:
            e = int(input("\nEnter public key e: "))
            p = int(input("Enter p: "))
            q = int(input("Enter q: "))
            n = p * q
            keys = generate_key(n)
            d = 0
            if keys[0] == e:
                d = keys[1]
            else:
                d = keys[0]
            print(f"Calculated private key d: {d}")
            main(n, (e, d))
    except KeyboardInterrupt:
        print("\nExiting the program...")
        exit(0)