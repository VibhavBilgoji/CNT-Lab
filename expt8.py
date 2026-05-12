import math

def fermatFact(n):
    i = 1
    while True:
        x = math.sqrt(n + i ** 2)
        if(x % 1 == 0):
            break
        i += 1
    x = int(x)
    a = x - i
    b = x + i
    print(f"n = {x}² - {i}² = ({x} + {i}) × ({x} - {i})")
    print(f"Factors of {n} are: {a} and {b}")
    # return a, b

def main():
    # Get user input for the random integer
    n = int(input("Enter the integer to be factored (n): "))
    if(n <= 1):
        print("Please enter an integer greater than 1.")
        return main()
    while True:
        print("\nChoose the method to factor n:")
        print("1. Fermat's Factorization")
        print("2. Pollard's p-1 Algorithm")
        print("3. Quadratic Sieve Method")
        print("4. Enter another integer")
        print("0. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        else:
            if choice == 1:
                fermatFact(n)
            elif choice == 2:
                # pollardFact(n)
                pass
            elif choice == 3:
                # quadraticSieveFact(n)
                pass
            elif choice == 4:
                return main()
            elif choice == 0:
                print("Exiting the program...")
                return
            else:
                print("Invalid choice. Please select a valid option.")

main()