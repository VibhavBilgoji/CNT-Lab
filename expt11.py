import math
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def private_key(e, p, q):
    phi = (p - 1) * (q - 1)
    for d in range(1, phi):
        if (e * d) % phi == 1:
            print("\nPrivate key d:", d)
            return d

def process_text(key, n, encrypt):
    if encrypt:
        txt = input("\nEnter the plaintext: ").upper()
        processed_arr = []
        for c in txt:
            i = alpha.index(c)
            if i < 10:
                bit = '0' + str(pow(i, key, n))
            else:
                bit = str(pow(i, key, n))
            processed_arr.append(bit)
        processed_txt = ''.join(processed_arr)
        print("\nCiphertext:", processed_txt)
    else:
        txt = input("\nEnter the ciphertext: ").strip()
        if len(txt) % 2 == 1:
            txt = '0' + txt
        processed_arr = []
        for i in range(0, len(txt), 2):
            bit = int(txt[i:i+2])
            c = alpha[pow(bit, key, n)]
            processed_arr.append(c)
        processed_txt = ''.join(processed_arr)
        print("\nPlaintext:", processed_txt)

def input_text(p, q, e, d, n):
    print("\nChoose option: ")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    c = int(input("Enter your choice: "))
    if c == 1:
        process_text(e, n, True)
    elif c == 2:
        process_text(d, n, False)
    else:
        print("Invalid choice. Exiting...")
        exit(1)

if __name__ == "__main__":
    try:
        while True:
            e = int(input("\nEnter public key e: "))
            p = int(input("Enter p: "))
            q = int(input("Enter q: "))
            n = p * q
            d = private_key(e, p, q)
            while True:
                input_text(p, q, e, d, n)
                print("\nChoose option: ")
                print("1. Enter another txt")
                print("2. Enter keys and p,q")
                c = int(input("Enter your choice: "))
                if c == 1:
                    continue
                elif c == 2:
                    break
                else:
                    print("Invalid choice. Exiting...")
                    exit(1)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
