## Compilers Dircetory

1. Scanner
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
2. Parser
```
 Zadanie polega na stworzeniu parsera, który powinien akceptować kod źródłowy w formie tokenów i tworzyć drzewo syntaktyczne. Parser powinien rozpoznawać następujące konstrukcje:

    wyrażenia binarne, w tym operacje macierzowe 'element po elemencie'
    wyrażenia relacyjne,
    negację unarną,
    transpozycję macierzy,
    inicjalizację macierzy konkretnymi wartościami,
    macierzowe funkcje specjalne,
    instrukcję przypisania, w tym różne operatory przypisania
    instrukcję warunkową if-else,
    pętle: while and for,
    instrukcje break, continue oraz return,
    instrukcję print,
    instrukcje złożone,
    tablice oraz ich zakresy. 
```
3. Drzewo syntaktyczne
```
 Zadanie polega na stworzeniu i wypisaniu abstrakcyjnego drzewa składni (ang. abstract syntax tree, AST). Drzewo składni powinno uwzględniać w swoich węzłach następujące konstrukcje:

    wyrażenia binarne,
    wyrażenia relacyjne,
    instrukcje przypisania,
    instrukcje warunkowe if-else,
    pętle: while oraz for,
    instrukcje break, continue oraz return,
    instrukcje print,
    instrukcje złożone,
    tablice oraz ich zakresy. 
```
4. Analiza semantyczna
```
Zadanie jest kontynuacją poprzedniego zadania.

Zadanie polega na stworzeniu analizatora błędów semantycznych.

Analizator semantyczny powinien wykrywać m.in. następujące błędy semantyczne:

    inicjalizacja macierzy przy użyciu wektorów o różnych rozmiarach
    odwołania poza zakres macierzy (w przypadku indeksów będących stałymi)
    dla danej operacji binarnej użycie stałej, skalara, wektora lub macierzy o niekompatybilnych typach lub rozmiarze, np.
        dodawanie skalara lub wektora do macierzy
        operacje binarne na wektorach lub macierzach o niekompatybilnych wymiarach 
    użycie funkcji inicjalizujących (funkcje eye, zeros, ones) z niepoprawnymi parametrami
    niepoprawne użycie instrukcji:
        instrukcje break lub continue poza pętlą 

Analiza błędów semantycznych nie powinna być przerywana po napotkaniu pierwszego błędu, lecz wykrywać jak największą liczbę błędów. Z każdym błędem powinna być skojarzona informacja o miejscu wystąpienia błędu (nr linii, ew. numer kolumny). 
```
