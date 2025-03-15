# Szyfrowanie i odszyfrowywanie wiadomości

## Opis projektu
Projekt implementuje szyfrowanie i odszyfrowywanie wiadomości przy użyciu:
- **Szyfru Cezara**
- **Szyfru afinicznego**

Program pozwala na szyfrowanie, deszyfrowanie oraz analizę kryptograficzną w oparciu o tekst jawny lub sam kryptogram.

## Uruchamianie programu
Program o nazwie `cezar` może być uruchamiany z linii poleceń z następującymi opcjami:

### 1. Wybór szyfru:
- `-c` - szyfr Cezara
- `-a` - szyfr afiniczny

### 2. Wybór operacji:
- `-e` - szyfrowanie
- `-d` - odszyfrowywanie
- `-j` - kryptoanaliza z tekstem jawnym
- `-k` - kryptoanaliza wyłącznie w oparciu o kryptogram

Przykładowe wywołania:
```
./cezar -c -e
./cezar -a -d
./cezar -c -j
./cezar -a -k
```

## Pliki wejściowe i wyjściowe
Program operuje na następujących plikach:

| Plik           | Opis |
|---------------|------|
| `plain.txt`   | Plik z tekstem jawnym (jeden wiersz, litery i spacje) |
| `crypto.txt`  | Plik z tekstem zaszyfrowanym |
| `decrypt.txt` | Plik z tekstem odszyfrowanym |
| `key.txt`     | Plik zawierający klucz (pierwsza liczba - przesunięcie, druga - współczynnik dla szyfru afinicznego, liczby oddzielone spacją) |
| `extra.txt`   | Plik zawierający początek tekstu jawnego w przypadku kryptoanalizy z tekstem jawnym |
| `key-found.txt` | Plik zawierający znaleziony klucz w przypadku kryptoanalizy |

## Zasady działania
- **Szyfrowanie**:
  - Odczytuje tekst jawny z `plain.txt` i klucz z `key.txt`
  - Zapisuje zaszyfrowany tekst do `crypto.txt`
  - W przypadku błędnego klucza zgłasza błąd

- **Odszyfrowywanie**:
  - Odczytuje zaszyfrowany tekst z `crypto.txt` i klucz z `key.txt`
  - Zapisuje odszyfrowany tekst do `decrypt.txt`
  - W przypadku błędnego klucza zgłasza błąd
  - Dla szyfru afinicznego program musi samodzielnie obliczyć odwrotność liczby `a`

- **Kryptoanaliza z tekstem jawnym**:
  - Odczytuje tekst zaszyfrowany z `crypto.txt` oraz tekst pomocniczy z `extra.txt`
  - Zapisuje znaleziony klucz do `key-found.txt` oraz odszyfrowany tekst do `decrypt.txt`
  - W przypadku niemożności znalezienia klucza zgłasza błąd

- **Kryptoanaliza bez tekstu jawnego**:
  - Odczytuje tekst zaszyfrowany z `crypto.txt`
  - Zapisuje wszystkie możliwe odszyfrowane teksty do `decrypt.txt`
  - Generuje 25 możliwych rozwiązań dla szyfru Cezara i 311 dla szyfru afinicznego

## Wymagania
Program może być napisany w dowolnym języku programowania, np.:
- Python, C, C++, C#, Java, Rust, JavaScript, Ruby, Scala, Golang, Racket, AWK, Bash, PHP, Perl, Pascal, Tcl, Assembler, Lisp, Scheme, Haskell, Smalltalk, Prolog itp.
- Opcjonalnie można dostarczyć skompilowaną wersję programu dla Javy lub C# w środowisku Windows

## Zasady techniczne
- Program nie może wymagać istnienia plików, które nie są potrzebne dla danej operacji
- Program musi tworzyć brakujące pliki wyjściowe

## Struktura pakietu
Gotowe rozwiązanie powinno być przesłane w archiwum `.tar` lub `.zip` i zawierać:
- **Kod źródłowy** programu
- **Opcjonalnie skompilowaną wersję** (dla Javy lub C#)
- **Przykładowe pliki wejściowe**:
  - `plain.txt` (tekst jawny)
  - `crypto.txt` (tekst zaszyfrowany)
  - `key.txt` (poprawny klucz dla szyfru afinicznego)

## Autor
Wpisz tutaj swoje imię i nazwisko lub pseudonim.

