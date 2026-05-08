while True:
    print("Select Main Choice:\n1. Arithmetic Operations\n2. Theorems\n0. Exit ")
    main_choice = int(input("Enter Choice: "))
    print()
    if main_choice == 0:
        print("Exiting the program...")
        break
    if main_choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(
            "\nSelect operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponentiation\n0. Exit "
        )
        operation = int(input("Enter operation: "))
        print()
        if operation == 0:
            print("Returning to main menu...\n\n")
            continue
        if operation == 1:
            result = num1 + num2
            print(f"The sum is: {result}\n")
        elif operation == 2:
            result = num1 - num2
            print(f"The difference is: {result}\n")
        elif operation == 3:
            result = num1 * num2
            print(f"The product is: {result}\n")
        elif operation == 4:
            if num2 != 0:
                result = num1 // num2
                print(f"The quotient is: {result}\n")
            else:
                print("Error: Division by zero is not allowed.\n")
        elif operation == 5:
            if num2 != 0:
                result = num1 % num2
                print(f"The modulus is: {result}\n")
            else:
                print("Error: Division by zero is not allowed.\n")
        elif operation == 6:
            result = num1**num2
            print(f"The result of {num1} raised to the power of {num2} is: {result}\n")
        else:
            print("Invalid choice. Please try again.\n\n")
    elif main_choice == 2:
        print("Select operation: ")
        print("1. Divisibility Theorem\n2. a | b and b | c imply a | c ")
        print("3. a | b and a | c imply a | (bx + cy) for any integer x and y")
        print("0. Exit")
        operation = int(input("Enter operation: "))
        print()
        if operation == 0:
            print("Returning to main menu...\n\n")
            continue
        if operation == 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            if b == 0:
                print("Error: Division by zero is not allowed.\n")
            else:
                q = 0
                r = a
                while r >= b:
                    r -= b
                    q += 1
                print(f"{a} = {b} * {q} + {r}")
                if r != 0:
                    print(f"{a} is not divisible by {b}.\n")
                else:
                    print(f"{a} is divisible by {b}.\n")
        elif operation == 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            c = int(input("Enter third number: "))
            print()
            if a != 0 and b != 0 and c != 0:
                if b % a == 0:
                    print(f"{b} is divisible by {a}, so {a} | {b}.")
                else:
                    print(f"{b} is not divisible by {a}, so {a} does not divide {b}.")
                if c % b == 0:
                    print(f"{c} is divisible by {b}, so {b} | {c}.")
                else:
                    print(f"{c} is not divisible by {b}, so {b} does not divide {c}.")
                if c % a == 0:
                    print(
                        f"{c} is divisible by {a}, so {a} | {c}.\n Therefore, the theorem holds.\n "
                    )
            else:
                print("Error: all numbers must be non-zero for this theorem.\n")
        elif operation == 3:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            c = int(input("Enter third number: "))
            x = int(input("Enter integer x: "))
            y = int(input("Enter integer y: "))
            print()
            if a != 0 and b != 0 and c != 0:
                if b % a == 0:
                    print(f"{b} is divisible by {a}, so {a} | {b}.")
                else:
                    print(f"{b} is not divisible by {a}, so {a} does not divide {b}.")
                if c % a == 0:
                    print(f"{c} is divisible by {a}, so {a} | {c}.")
                else:
                    print(f"{c} is not divisible by {a}, so {a} does not divide {c}.")
                if (b * x + c * y) % a == 0:
                    print(
                        f"{b}*{x} + {c}*{y} is divisible by {a}, so {a} | ({b}*{x} + {c}*{y})."
                    )
                    print("Therefore, the theorem holds.\n")
                else:
                    print(
                        f"{b}*{x} + {c}*{y} is not divisible by {a}, so {a} does not divide ({b}*{x} + {c}*{y})."
                    )
            else:
                print("Error: all numbers must be non-zero for this theorem.\n")
        else:
            print("Invalid choice. Please try again.\n\n")
    else:
        print("Invalid choice. Please try again.\n\n")
