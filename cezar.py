import sys
import os
import math

def read_file(filename):
    if not os.path.exists(filename):  # Sprawdza, czy plik istnieje
        return ""  # Jeśli nie istnieje, zwraca pusty ciąg znaków
    with open(filename, 'r') as file:  # Otwiera plik w trybie odczytu
        return file.read().strip()  # Zwraca zawartość pliku bez białych znaków na początku i końcu

def write_file(filename, content):
    with open(filename, 'w') as file:  # Otwiera plik w trybie zapisu
        file.write(content)  # Zapisuje podaną zawartość do pliku

# Sprawdza, czy liczba `a` jest względnie pierwsza z 26 (dla szyfru afinicznego)
def is_valid(a):
    return math.gcd(a, 26) == 1  # Sprawdza największy wspólny dzielnik `a` i 26, jeśli wynosi 1, zwraca True

def caesar_e(plain, shift):
    crypto = ''  # Inicjalizacja pustego ciągu znaków dla zaszyfrowanego tekstu
    for char in plain:  # Iteracja po każdym znaku w tekście jawnym
        if char.isalpha():  # Sprawdza, czy znak jest literą
            shift_amount = shift % 26  # Ogranicza przesunięcie do zakresu 0-25
            new_char = chr((ord(char) - 97 + shift_amount) % 26 + 97)  # Przesuwa literę w alfabecie
            crypto += new_char  # Dodaje zaszyfrowany znak do wyniku
        else:
            crypto += char  # Pozostawia niezmienione znaki inne niż litery
    return crypto

def caesar_d(crypto, shift):
    return caesar_e(crypto, -shift)  # Szyfruje z odwrotnym przesunięciem, co daje deszyfrowanie

def affine_e(plain, a, b):
    crypto = ''
    for char in plain:
        if char.isalpha():
            new_char = chr(((a * (ord(char) - 97) + b) % 26) + 97)  # Przekształca literę zgodnie z równaniem szyfru afinicznego
            crypto += new_char
        else:
            crypto += char
    return crypto

def affine_d(crypto, a, b):
    if not is_valid(a):  # Sprawdza, czy `a` ma odwrotność modularną
        raise ValueError("Klucz 'a' nie jest odwracalny modulo 26")  # Rzuca wyjątek, jeśli `a` nie jest odwracalne
    
    decrypt = ''
    a_inv = pow(a, -1, 26)  # Oblicza odwrotność modularną `a`
    for char in crypto:
        if char.isalpha():
            new_char = chr((a_inv * ((ord(char) - 97) - b) % 26) + 97)  # Odszyfrowuje znak
            decrypt += new_char
        else:
            decrypt += char
    return decrypt

def caesar_j(crypto, extra):
    shift = (ord(crypto[0]) - ord(extra[0])) % 26  # Oblicza przesunięcie porównując pierwsze litery
    return shift  # Zwraca klucz

# Odkrywa klucz szyfru afinicznego na podstawie dwóch pierwszych liter tekstu jawnego
def affine_j(crypto, extra):
    c1, p1 = ord(crypto[0]) - 97, ord(extra[0]) - 97  # Pobiera wartości pierwszych liter
    c2, p2 = ord(crypto[1]) - 97, ord(extra[1]) - 97  # Pobiera wartości drugich liter
    
    a = ((c1 - c2) * pow(p1 - p2, -1, 26)) % 26
    b = (c1 - a * p1) % 26
    return a, b

def caesar_k(crypto):
    results = [caesar_d(crypto, shift) for shift in range(1, 26)]  # Generuje wszystkie możliwe deszyfrowania
    return '\n'.join(results)  # Łączy wyniki w jeden tekst

def affine_k(crypto):
    results = []  # Inicjalizacja listy wyników
    for a in range(1, 26, 2):  # Sprawdza tylko nieparzyste `a`, które mogą być odwracalne
        if is_valid(a):
            for b in range(26):  # Iteruje przez wszystkie możliwe wartości `b`
                results.append(affine_d(crypto, a, b))  # Odszyfrowuje i dodaje wynik
    return '\n'.join(results)  # Łączy wyniki w jeden tekst

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