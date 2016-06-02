# KOMPRESJA DANYCH
## Projekt: Kodowanie różnicowe + koder Huffmana

### Zespół:
* Piotr Chmielewski
* Michał Dobrzański
* Maciej Janusz Krajsman
* Marcin Lembke

#### Zadanie:
 	
  Opracować algorytm kodowania predykcyjnego danych dwuwymiarowych wykorzystując do predykcji: 
lewego sąsiada, górnego sąsiada, medianę lewego, lewego-górnego, górnego sąsiada. Wyznaczyć histogramy danych różnicowych dla danych wejściowych o rozkładzie równomiernym, normalnym, Laplace'a oraz wybranych obrazów testowych. Zakodować dane różnicowe przy użyciu klasycznego algorytmu Huffmana. Wyznaczyć entropię danych wejściowych i różnicowych, porównać ze średnią długością bitową kodu wyjściowego. Ocenić efektywność algorytmu do kodowania obrazów naturalnych. 

#### Struktura projektu:

- HuffmanCodec/
  - *HuffmanCoder.py* - Koder stosujący **algorytm Huffmana**
  - *HuffmanDecoder.py* - Dekoder stosujący algorytm Huffmana
  - *HuffmanTree.py* - Klasa wspomagająca działanie kodeku Huffmana. Buduje drzewo kodowe dla algorytmu.
  
- *PredictiveCodec.py* - Klasa implementująca **koder oraz dekoder predykcyjny** wykorzystuja do predykcji: lewego sąsiada, górnego sąsiada, medianę lewego, lewego-górnego, górnego sąsiada

- *ImageGenerator.py* - generowanie obrazów 2D z pikselami o wartościach pochodzących z rozkładów: normalnego, równomiernego, Laplace'a

- *data/* - folder z obrazami 2D wejściowymi

- *main.py* - punkt startowy programu. Skrypt ten umożliwia przeprowadzenie kompresji oraz dekompresji dla wejściowych obrazów. Steruje algorytmem predykcyjnym i algorytmem Huffmana. Zawiera funkcje do wyznaczania **entropii** oraz **średniej długości słowa bitowego**. Wyznacza również **histogramy** dla wczytanych obrazów. Umożliwia **zapisanie zakodowanych obrazów** oraz ich **wczytanie oraz zdekodowanie**.

- *encoded/* - folder z zakodowanymi obrazami

- *decoded/* - folder ze zdekodowanymi obrazami

- *histograms/* - zbiorcze **histogramy** dla danych wejściowych

- *latex/* - **dokumentacja** projektu

- *output.txt* - **wyjściowe wyniki entropii oraz średniej długości słowa kodowego** dla wczytanych obrazów

#### Wykorzystane narzędzia programistyczne:

Algorytm kodowania/dekodowania predykcyjnego zrealizowany został w języku Python. 

Użyte biblioteki:
- *PIL (Pillow)* - operacje na plikach graficznych
- *Numpy* - część operacji obliczeniowych i generowanie obrazów o zadanym rozkładzie intensywności pikseli
- *Matplotlib* - generowanie histogramów

#### Kodowanie i dekodowanie:

Kodowanie i dekodowanie danych w projekcie można podzielić na 4 etapy: 

- *Kodowanie różnicowe* - by zmniejszyć rozmiar słownika (ilość słów)
- *Kodowanie Huffmana* - by zminimalizować miejsce zajmowane przez słowa (średnią długość słowa kodowego)
- *Dekodowanie Huffmana*
- *Dekodowanie różnicowe*

Kodowanie różnicowe realizowane jest przez procedurę *encode_predictive()* w pliku *PredictiveCodec.py*. Dane wejściowe stanowią obrazy (wczytane przez bibliotekę *Pillow*), w formie dwuwymiarowych tablic wartości intensywności pikseli. Algorytm tworzy kopię tablicy, a następnie zmienia jej wartości odpowiednio, zgodnie z ideą kodowania różnicowego (wartość piksela zakodowanego to różnica wartości piksela poprzedzającego i wartości piksela kodowanego przed kodowaniem). Jako odniesienie wykorzystywany jest jeden piksel poprzedzający (ustalony jako, odpowiednio dla wybranej opcji: 0: brak 1: lewy, 2: górny, albo 3: będący medianą - z punktu widzenia intensywności - piksela lewego, górnego oraz lewego-górnego). Na koniec tablice są serializowane i przechowywane w formie jednowymiarowej, w celu ułatwienia dalszego przetwarzania. 
Należy zwrócić uwagę na dwa fakty:
- Dla pierwszych kodowanych pikseli, jako wartość poprzednią ustalono 128, czyli środek przedziału 0-255, w którym znajdują się wartości natężeń pikseli,
- Zamiast gotowej funkcji median (z pakietu *numpy*) użyto funkcji własnej, która (kosztem redukcji uniwersalności - zastosowanie tylko i wyłącznie dla trzech liczb) jest dużo wydajniejsza obliczeniowo.

Kodowanie Huffmana realizowane jest w pliku *HuffmanCodec/HuffmanCoder.py*. Wejście stanowią dane pochodzące z opisanego wyżej kodowania różnicowego. Algorytm zapisuje je w formie kodu Huffmana, czyli optymalnego kodu przedrostkowego. Słowa kodowane są z użyciem drzewa (*HuffmanCodec/HuffmanTree.py*) - słowo kodowe powstaje od strony liścia, po przejściu do korzenia (i zapisaniu kolejno wartości 0/1). Zgodnie z teorią, najdłuższe słowa kodowe otrzymują słowa występujące najrzadziej, a dwa najdłuższe z nich są równej długości.

Dekodowanie Huffmana (*HuffmanCodec/HuffmanDecoder.py*) odtwarza z kodu Huffmana pierwotnie kodowane słowa (procedura odwrotna od poprzedniej)

Dekodowanie różnicowe polega na odtworzeniu obrazu o takich samych wartościach natężeń pikseli, jakie występowały w obrazach pierwotnych. Niezbędne jest dostarczenie informacji o tym, który piksel wykorzystywany był jako piksel poprzedzający (*opt*: wartości 0-3). Uzyskane obrazy są czarno-białe, ponieważ nie kodowano informacji o kolorach. 

W trakcie działania programu wyświetlane są informacje o uzyskanych wartościach entropii oraz średniej długości słowa kodowego w obrazie, które mogą służyć do oceny efektywności zastosowanych algorytmów. Zapisywane są również histogramy danych oryginalnych oraz z kodowania różnicowego (generowane przez pakiet *matplotlib*). 