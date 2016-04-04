Michał Dobrzański, 04.04.2016:

KODER
Kodowanie sugeruję następująco (do wyjściowego pliku binarnego):
[2 bity na sposób kodowania, bo 3 opcje (lewy sasiad, gorny sasaid, mediana)][ ciag danych(010101010111111......) ]

DEKODER
Dekodowanie z ksiażki Przelaskowskiego:
(0) Dekoder MUSI znać utworzoną strukturę drzewa
(a) Ustaw korzen drzerwa jako aktualny węzeł
(b) Pobierz bit z wejścia; jeśli wczytano 0, to przejdź do lewego syna aktualnego węzła, w przeciwnym razie przejdź do jego prawego syna;
(c) jeśli aktualny węzeł to liść, odczytaj przypisany mu symbol i prześlij na wyjście; w przeciwnym razie kontynuuj (b)
(d) porwtarzaj od (a) aż do wyczerpania zbioru danych wejściowych
