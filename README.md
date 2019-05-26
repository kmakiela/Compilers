## Compilers Directory

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
5. Interpreter
```
 Zadanie polega na stworzeniu interpretera języka wyspecyfikowanego w poprzednich zajęciach. Interpretacja powinna być wykonywana tylko wtedy, gdy poprzednie etapy zakończyły się sukcesem -- nie wystąpiły żadne błędy syntaktyczne lub semantyczne.
Implementacja

Do implementacji zadania należy wykorzystać wzorzec visitor. Tym razem nie będziemy używać implementacji z poprzednich zajęć (dla każdej klasy z AST definicja funkcji vistit_<classname> w odpowiednim wizytorze), lecz należy użyć implementacji opartej na dekoratorach. W tym celu w wizytorze Interpreter należy dla każdej klasy z AST zdefiniować metodę visit, dekorowaną nazwą tej klasy.
Pamięć interpretera

Poza trywialnym przypadkiem jednego, globalnego zakresu, bieżące wartości zmiennych nie mogą być przechowywane w tablicy symboli. W pozostałych przypadkach potrzebna jest osobna pamięć interpretera o strukturze stosu.

    Pamięć globalna globalMemory służy do przechowywania wartości zmiennych w zakresie globalnym i jego zakresach potomnych niefunkcyjnych. Pamięć ta możę zostać zaimplementowana jako instacja klasy MemoryStack. 

Przekazywanie sterowania

Do zaimplementowania przekazywania sterowania z instrukcji break, continue nie wystarczy użycie zwykłej instrukcji return, gdyż wspomniane instrukcje mogą być zagnieżdzone dowolnie głęboko w pętli. Zamiast tego należy posłużyć się mechanizmem wyjątków: zgłaszanie wyjątku przy interpretacji instrukcji break lub continue oraz jego przechwytywanie w funkcjach visit interpretujących pętle (oraz w funkcji visit interpretującej wywołanie funkcji, jeśli język umożliwia definiowanie i wywoływanie funkcji). 
```