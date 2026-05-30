def caesar_cipher():
    pass

def affine_cipher():
    pass

def vigenere_cipher():
    pass

def playfair_cipher():
    pass

def adfgx_cipher():
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
    print("\nChoose option:\n1. Enter another ciphertext\n2. Choose another cipher")
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
        global ct
        ct = input("\nEnter ciphertext: ")
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