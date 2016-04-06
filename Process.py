# http://code.activestate.com/recipes/576603-huffman-coding-encoderdeconder/
import collections
import itertools

from PIL import Image

# ------------------------CZYTANIE-------------------------------------------
# imgs - uchwyty do wszystkich obrazow
# pixs - uchwyty do tablic pikseli zwiazanych z obrazami
imgs = []
pixs = []

imgs.append(Image.open('data/uniform.png'))
imgs.append(Image.open('data/gaussian.png'))
imgs.append(Image.open('data/laplace.png'))

i = 1;
for img in imgs:
    print(i, ") ", img.format, img.mode, img.size)
    pixs.append(img.load())  # http://effbot.org/imagingbook/image.htm#tag-Image.Image.load
    i += 1

# ------------------------KODOWANIE PREDYKCYJNE------------------------------
print("Kodowanie predykcyjne")

img = imgs[0]
pix = pixs[0]

width = img.size[0]
height = img.size[1]

# pix_diff - dane roznicowe do pozniejszego zakodowania huffmanem
pix_diff = [[0 for x in range(width)] for x in range(height)]
# opt - jedna z 3 opcji kodowania roznicowego
for opt in range(1, 2):
    for y in range(0, height):
        for x in range(0, width):
            # lewy sasiad
            if (opt == 1):
                if (y > 0):
                    pix_diff[x][y] = pix[x, y] - pix[x, y - 1]
                else:
                    pix_diff[x][y] = pix[x, y]
            # gorny sasiad
            if (opt == 2):
                if (x > 0):
                    pix_diff[x][y] = pix[x, y] - pix[x - 1, y]
                else:
                    pix_diff[x][y] = pix[x, y]
                    # mediana lewego, lewego-gornego i gornego
                    # TODO

# http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
# Konwersja danych 2D na liste
merged = list(itertools.chain(*pix_diff))
# Konwersja listy na czestotliwosci wystepowania (wagi)
# http://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-a-list
freq_diff = collections.Counter(merged)
print(freq_diff.keys())  # wartosci (symbole)
print(freq_diff.values())  # wagi


# ------------------------ALGORYTM HUFFMANA----------------------------------
