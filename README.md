Michał Dobrzański, 04.04.2016:

# KOMPRESJA DANYCH
## Projekt: Kodowanie różnicowe + koder Huffmana

### Zespół:
* Piotr Chmielewski
* Michał Dobrzański
* Maciej Krasjman
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
