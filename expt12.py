q = int(input("Enter a prime number (q): "))
g = int(input("Enter a alpha (α): "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = pow(g, a, q)
B = pow(g, b, q)

print("\nAlice's public key:", A)
print("Bob's public key:", B)

alice_secret = pow(B, a, q)
bob_secret = pow(A, b, q)

print("\nAlice's shared secret:", alice_secret)
print("Bob's shared secret:", bob_secret)

if alice_secret == bob_secret:
    print("Key exchange successful!")
else:
    print("Key exchange failed!")