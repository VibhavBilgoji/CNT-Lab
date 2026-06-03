def key_exchange():
    q = int(input("Enter a prime number (q): "))
    g = int(input("Enter a alpha (α): "))

    xa = int(input("Enter Alice's private key: "))
    xb = int(input("Enter Bob's private key: "))

    ya = pow(g, xa, q)
    yb = pow(g, xb, q)

    print("\nAlice's public key:", ya)
    print("Bob's public key:", yb)

    ka = pow(yb, xa, q)
    kb = pow(ya, xb, q)

    print("\nAlice's shared secret:", ka)
    print("Bob's shared secret:", kb)

    print("Key exchange " + "Successful!" if ka == kb else "Failed!")

if __name__ == "__main__":
    try:
        while True:
            key_exchange()
            choice = input("\nDo you want to perform another key exchange? (y/n): ")
            if choice.lower() != 'y':
                break
    except KeyboardInterrupt:
        print("\nExiting...")