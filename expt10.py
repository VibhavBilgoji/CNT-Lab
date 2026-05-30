alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt_or_decrypt():
    while True:
        choice = input("Do you want to encrypt or decrypt? (E/D): ").strip().upper()
        if choice in ('E', 'D'):
            return choice
        print("Please enter 'E' for encrypt or 'D' for decrypt.")

def caesar_cipher():
    mode = encrypt_or_decrypt()
    k = int(input("Enter the shift value (k): "))
    processed_arr = []
    if mode == 'E':
        for c in input_text:
            if c == ' ':
                continue
            processed_arr += alpha[(alpha.index(c) + k) % 26]
        processed_text = ''.join(processed_arr)
        print("Ciphertext:", processed_text)
    else:
        for c in input_text:
            if c == ' ':
                continue
            processed_arr += alpha[(alpha.index(c) - k) % 26]
        processed_text = ''.join(processed_arr)
        print("Plaintext:", processed_text)

def affine_cipher():
    mode = encrypt_or_decrypt()
    a = int(input("Enter value of α: "))
    b = int(input("Enter value of β: "))
    processed_arr = []
    if mode == 'E':
        for c in input_text:
            if c == ' ':
                continue
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
            if c == ' ':
                continue
            processed_arr += alpha[(a * alpha.index(c) + b) % 26]
        processed_text = ''.join(processed_arr)
        print("Plaintext:", processed_text)

def vigenere_cipher():
    mode = encrypt_or_decrypt()
    vector = input("Enter the vector: ").strip().upper()
    n = len(vector)
    i = 0
    processed_arr = []
    if mode == 'E':
        for c in input_text:
            if c == ' ':
                continue
            offset = alpha.index(vector[i % n])
            processed_arr += alpha[(alpha.index(c) + offset) % 26]
            i += 1
        processed_text = ''.join(processed_arr)
        print("Ciphertext: " + processed_text)
    else:
        for c in input_text:
            if c == ' ':
                continue
            offset = alpha.index(vector[i % n])
            processed_arr += alpha[(alpha.index(c) - offset) % 26]
            i += 1
        processed_text = ''.join(processed_arr)
        print("Ciphertext: " + processed_text)

def playfair_cipher():
    # mode = encrypt_or_decrypt()
    pass

def adfgx_cipher():
    # mode = encrypt_or_decrypt()
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
    if choice == 1:
        caesar_cipher()
    elif choice == 2:
        affine_cipher()
    elif choice == 3:
        vigenere_cipher()
    elif choice == 4:
        playfair_cipher()
    elif choice == 5:
        adfgx_cipher()

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
        global input_text
        input_text = input("\nEnter text: ").upper()
        while True:
            choice = choose()
            call_cipher(choice)
            next_step = choose_at_end()
            if next_step == 1:
                break

if __name__ == "__main__":
    try:
        run_program()
    except KeyboardInterrupt:
        print("\nExiting the program...")
        exit()