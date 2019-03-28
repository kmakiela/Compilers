## Compilers Dircetory

1st etap
```
 Zadanie polega na stworzeniu analizatora leksykalnego (skanera) dla prostego języka umożliwiającego obliczenia na macierzach. Analizator leksykalny powinien rozpoznawać następujące leksemy:

    operatory binare: +, -, *, /
    macierzowe operatory binarne (dla operacji element po elemencie): .+, .-, .*, ./
    operatory przypisania: =, +=, -=, *=, /=
    operatory relacyjne: <, >, <=, >=, !=, ==
    nawiasy: (,), [,], {,}
    operator zakresu: :
    transpozycja macierzy: '
    przecinek i średnik: , ;
    słowa kluczowe: if, else, for, while
    słowa kluczowe: break, continue oraz return
    słowa kluczowe: eye, zeros oraz ones
    słowa kluczowe: print
    identyfikatory (pierwszy znak identyfikatora to litera lub znak _, w kolejnych znakach mogą dodatkowo wystąpić cyfry)
    liczby całkowite
    liczby zmiennoprzecinkowe
    stringi 

Dla rozpoznanych leksemów stworzony skaner powinien zwracać:

    odpowiadający token
    rozpoznany leksem
    numer linii
    opcjonalnie może być zwracany numer kolumny 

Następujące znaki powinny być pomijane:

    białe znaki: spacje, tabulatory, znaki nowej linii
    komentarze: komentarze rozpoczynające się znakiem # do znaku końca linii 
```
