alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def toEncrypt():
    while True:
        choice = input("Do you want to encrypt or decrypt? (E/D): ").strip().upper()
        if choice in ('E', 'D'):
            if choice == 'E':
                return True
            else:
                return False
        print("Please enter 'E' for encrypt or 'D' for decrypt.")

def caesar_cipher(input_text):
    mode = toEncrypt()
    k = int(input("Enter the shift value (k): "))
    processed_arr = []
    if mode:
        for c in input_text:
            processed_arr += alpha[(alpha.index(c) + k) % 26]
        processed_text = ''.join(processed_arr)
        print("Ciphertext:", processed_text)
    else:
        for c in input_text:
            processed_arr += alpha[(alpha.index(c) - k) % 26]
        processed_text = ''.join(processed_arr)
        print("Plaintext:", processed_text)

def affine_cipher(input_text):
    mode = toEncrypt()
    a = int(input("Enter value of α: "))
    b = int(input("Enter value of β: "))
    processed_arr = []
    if mode:
        for c in input_text:
            processed_arr += alpha[(a * alpha.index(c) + b) % 26]
        processed_text = ''.join(processed_arr)
        print("Ciphertext:", processed_text)
    else:
        inv = 1
        while a * inv % 26 != 1:
            inv += 1
        a = inv
        b = (-b) * inv % 26
        for c in input_text:
            processed_arr += alpha[(a * alpha.index(c) + b) % 26]
        processed_text = ''.join(processed_arr)
        print("Plaintext:", processed_text)

def vigenere_cipher(input_text):
    mode = toEncrypt()
    key = input("Enter the key: ").replace(" ", "").upper()
    n = len(key)
    i = 0
    processed_arr = []
    if mode:
        for c in input_text:
            offset = alpha.index(key[i % n])
            processed_arr += alpha[(alpha.index(c) + offset) % 26]
            i += 1
        processed_text = ''.join(processed_arr)
        print("Ciphertext: " + processed_text)
    else:
        for c in input_text:
            offset = alpha.index(key[i % n])
            processed_arr += alpha[(alpha.index(c) - offset) % 26]
            i += 1
        processed_text = ''.join(processed_arr)
        print("Ciphertext: " + processed_text)

def playfair_cipher(input_text):
    mode = toEncrypt()
    key = input("Enter the key: ").replace(" ", "").upper().replace("J", "I")
    input_text = input_text.replace("J", "I")
    seen_chars = set('J')
    matrix = list()
    for c in key:
        if c not in seen_chars:
            seen_chars.add(c)
            matrix += c
    for c in alpha:
        if c not in seen_chars:
            seen_chars.add(c)
            matrix += c
    n = len(input_text)
    print("\nMatrix:")
    for i in range(5):
        for j in range(5):
            if(matrix[i*5 + j] == 'I'):
                print("Ĳ", end = " ")
            else:
                print(matrix[i*5 + j], end = " ")
        print()
    i = 0
    processed_arr = []
    if mode:
        while i < n:
            a = input_text[i]
            b = input_text[i+1] if i < (n-1) else 'X'
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
            xj = xk = yj = yk = 0
            for j in range(5):
                for k in range(5):
                    if matrix[j*5 + k] == a:
                        xj = j
                        xk = k
                    elif matrix[j*5 + k] == b:
                        yj = j
                        yk = k
            if xj == yj: #same row
                ao = matrix[xj*5 + ((xk+1) % 5)]
                bo = matrix[yj*5 + ((yk+1) % 5)]
            elif xk == yk: #same column
                ao = matrix[((xj+1) % 5)*5 + xk]
                bo = matrix[((yj+1) % 5)*5 + yk]
            else:
                ao = matrix[xj*5 + yk]
                bo = matrix[yj*5 + xk]
            processed_arr += f"{ao}{bo}"
        processed_text = ''.join(processed_arr)
        print("\nCiphertext: " + processed_text)
    else:
        while i < n:
            a = input_text[i]
            b = input_text[i+1]
            xj = xk = yj = yk = 0
            for j in range(5):
                for k in range(5):
                    if matrix[j*5 + k] == a:
                        xj = j
                        xk = k
                    elif matrix[j*5 + k] == b:
                        yj = j
                        yk = k
            if xj == yj: #same row
                ao = matrix[xj*5 + ((xk-1) % 5)]
                bo = matrix[yj*5 + ((yk-1) % 5)]
            elif xk == xk: #same column
                ao = matrix[((xj-1) % 5)*5 + xk]
                bo = matrix[((yj-1) % 5)*5 + yk]
            else:
                ao = matrix[xj*5 + yk]
                bo = matrix[yj*5 + xk]
            processed_arr += f"{ao}{bo}"
        processed_text = ''.join(processed_arr)
        print("\nPlaintext: " + processed_text)

def adfgx_cipher(input_text):
    # mode = toEncrypt()
    pass

def choose():
    print("\nChoose Cipher:\n1. Caesar\n2. Affine\n3. Vigenère\n4. Playfair\n5. ADFGX")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                return choice
            raise ValueError
        except ValueError:
            print("Please enter an integer between 1 and 5.")

def call_cipher(choice):
    input_text = input("\nEnter text: ").replace(" ", "").upper()
    if choice == 1:
        caesar_cipher(input_text)
    elif choice == 2:
        affine_cipher(input_text)
    elif choice == 3:
        vigenere_cipher(input_text)
    elif choice == 4:
        playfair_cipher(input_text)
    elif choice == 5:
        adfgx_cipher(input_text)

def choose_at_end():
    print("\nChoose option:\n1. Enter another text\n2. Choose another cipher")
    while True:
        try:
            option = int(input("Enter your choice: "))
            if option in (1, 2):
                return option
            raise ValueError
        except ValueError:
            print("Please enter 1 or 2.")

def run_program():
    while True:
        choice = choose()
        while True:
            call_cipher(choice)
            next_step = choose_at_end()
            if next_step == 2:
                break

if __name__ == "__main__":
    try:
        run_program()
    except KeyboardInterrupt:
        print("\nExiting the program...")
        exit()