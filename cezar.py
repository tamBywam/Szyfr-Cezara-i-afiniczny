import sys
import os
import math

def read_file(filename):
    if not os.path.exists(filename):
        return ""
    with open(filename, 'r') as file:
        return file.read().strip()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def is_valid(a):
    return math.gcd(a, 26) == 1

def caesar_e(plain, shift):
    crypto = ''
    for char in plain:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) - 97 + shift_amount) % 26 + 97)
            crypto += new_char
        else:
            crypto += char
    return crypto

def caesar_d(crypto, shift):
    return caesar_e(crypto, -shift)

def affine_e(plain, a, b):
    crypto = ''
    for char in plain:
        if char.isalpha():
            new_char = chr(((a * (ord(char) - 97) + b) % 26) + 97)
            crypto += new_char
        else:
            crypto += char
    return crypto

def affine_d(crypto, a, b):
    if not is_valid(a):
        raise ValueError("Klucz 'a' nie jest odwracalny modulo 26")
    
    decrypt = ''
    a_inv = pow(a, -1, 26)
    for char in crypto:
        if char.isalpha():
            new_char = chr((a_inv * ((ord(char) - 97) - b) % 26) + 97)
            decrypt += new_char
        else:
            decrypt += char
    return decrypt

def caesar_j(crypto, extra):
    shift = (ord(crypto[0]) - ord(extra[0])) % 26
    return shift

def affine_j(crypto, extra):
    c1, p1 = ord(crypto[0]) - 97, ord(extra[0]) - 97
    c2, p2 = ord(crypto[1]) - 97, ord(extra[1]) - 97
    
    a = ((c1 - c2) * pow(p1 - p2, -1, 26)) % 26
    b = (c1 - a * p1) % 26
    return a, b

def caesar_k(crypto):
    results = [caesar_d(crypto, shift) for shift in range(1, 26)]
    return '\n'.join(results)

def affine_k(crypto):
    results = []
    for a in range(1, 26, 2):
        if is_valid(a):
            for b in range(26):
                results.append(affine_d(crypto, a, b))
    return '\n'.join(results)

def main():
    cipher_type = sys.argv[1]
    operation = sys.argv[2]

    if cipher_type == '-c':
        if operation == '-e':
            plain = read_file('plain.txt')
            key = int(read_file('key.txt').split()[0])
            if not is_valid(a):
                raise ValueError("Błędny klucz")
            write_file('crypto.txt', caesar_e(plain, key))
        elif operation == '-d':
            crypto = read_file('crypto.txt')
            key = int(read_file('key.txt').split()[0])
            if not is_valid(a):
                raise ValueError("Błędny klucz")
            write_file('decrypt.txt', caesar_d(crypto, key))
        elif operation == '-j':
            crypto = read_file('crypto.txt')
            extra = read_file('extra.txt')
            key = caesar_j(crypto, extra)
            if not key:
                raise ValueError("Nie można odgadnąć klucza")
            write_file('key-found.txt', str(key))
            write_file('decrypt.txt', caesar_d(crypto, key))
        elif operation == '-k':
            crypto = read_file('crypto.txt')
            write_file('decrypt.txt', caesar_k(crypto))
    
    elif cipher_type == '-a':
        if operation == '-e':
            plain = read_file('plain.txt')
            key = read_file('key.txt').split()
            a, b = int(key[0]), int(key[1])
            if not is_valid(a):
                raise ValueError("Błędny klucz")
            write_file('crypto.txt', affine_e(plain, a, b))
        elif operation == '-d':
            crypto = read_file('crypto.txt')
            key = read_file('key.txt').split()
            a, b = int(key[0]), int(key[1])
            if not is_valid(a):
                raise ValueError("Błędny klucz")
            write_file('decrypt.txt', affine_d(crypto, a, b))
        elif operation == '-j':
            crypto = read_file('crypto.txt')
            extra = read_file('extra.txt')
            a, b = affine_j(crypto, extra)
            if not a or not b:
                raise ValueError("Nie można odgadnąć klucza")
            write_file('key-found.txt', f"{a} {b}")
            write_file('decrypt.txt', affine_d(crypto, a, b))
        elif operation == '-k':
            crypto = read_file('crypto.txt')
            write_file('decrypt.txt', affine_k(crypto))

if __name__ == "__main__":
    main()
