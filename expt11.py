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

def is_numeric_input(text):
    return text.isdigit()

def convert_text_to_integer(text):
    msg = 0
    has_leading_a = text[0] == 'A'
    for c in text:
        i = alpha.index(c)
        msg = msg * 100 + i
    print("Plaintext in integer:", msg)
    return msg, has_leading_a

def pad_integer_input(numeric_str):
    if len(numeric_str) % 2 == 0:
        return numeric_str, False

    if int(numeric_str[0]) < 10:
        return numeric_str, True
    else:
        print("Error: Odd-length numeric input with first digit >= 10 is ambiguous.")
        print("Please enter even-length numeric input or text input.")
        return None, None

def process(text, key, mode):
    firstA = False
    first_digit_single = False
    if is_numeric_input(text):
        msg = text
        padded, first_digit_single = pad_integer_input(msg)
        if padded is None:
            return None
        msg = padded
    else:
        text = text.upper()
        msg_int, firstA = convert_text_to_integer(text)
        msg = str(msg_int)
    c = ""
    if firstA:
        c += "00"
    if first_digit_single:
        c += "0" + str(text[0])
        start_idx = 1
    else:
        start_idx = 0

    for i in range(start_idx, len(msg), 2):
        if i + 1 < len(msg):
            bits = int(msg[i:i+2])
        else:
            bits = int(msg[i])

        cBits = pow(bits, key[0], key[1])
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
        m = input("\nEnter the plaintext (letters or integers): ")
        c = process(m, (keys[0], n), 'encrypt')
        if c is not None:
            print(f"Ciphertext: {c}\n")
        else:
            print("Encryption failed. Please try again.\n")
    elif choice == 2:
        c = input("\nEnter the ciphertext (letters or integers): ")
        m = process(c, (keys[1], n), 'decrypt')
        if m is not None:
            print(f"Plaintext: {m}\n")
        else:
            print("Decryption failed. Please try again.\n")
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
            phi = (p - 1) * (q - 1)
            d = 1
            while (d * e) % phi != 1:
                d += 1
            print(f"Calculated private key d: {d}")
            main(n, (e, d))
    except KeyboardInterrupt:
        print("\nExiting the program...")
        exit(0)
