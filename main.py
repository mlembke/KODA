import os
import numpy as np
import matplotlib.pyplot as plt
import math
import collections
from PIL import Image

import HuffmanCodec.HuffmanCoder as Coder
import ImageGenerator
import PredictiveCodec

path = "data/"

def entropy(data):
    # Wyliczenie entropii. Przyjmuje tablice.
    freq_data = collections.Counter(data)
    probs = [float(x) / len(data) for x in freq_data.values()]
    return -1 * sum(a * b for a,b in zip(probs,[math.log2(x) for x in probs]))

def word_length(data,code):
    # Srednia dlugosc slowa kodowego.
    codes = code.code_book;
    freq_data = collections.Counter(data)
    freq_data = collections.OrderedDict(sorted(freq_data.items()))
    # tablica prawdopobienstw jest dzieki temu posortowana
    probs = [float(x) / len(data) for x in freq_data.values()]
    codes = [len(x) for x in codes.values()] # dlugosc slowa bitowego
    return sum(np.multiply(probs,codes))


def read_images():
    imgs = []
    names = []
    for filename in os.listdir(path):
        img = Image.open(path + filename)
        print(filename + ": " + img.mode, img.size)
        imgs.append(img);
        names.append(filename)
    return (imgs,names)

def get_data(images,idx):
    pix = []
    pix.append(np.array(images[idx], dtype='int64').flatten())
    for i in range(1,4):
        pix.append(PredictiveCodec.encode_predictive(images[idx],i))
    return pix  # Tablica: 0 - dane wejsciowe, 1 - lewy sasiad, 2 - gorny sasiad, 3 - mediana)


def histogram(data,names,idx):
    plt.suptitle('Histogramy danych roznicowych dla ' + names[idx])
    plt.subplot(1, 3, 1)
    plt.title('Lewy sasiad')
    plt.hist(data[1], bins = 20, color='blue')
    plt.subplot(1, 3, 2)
    plt.title('Gorny sasiad')
    plt.hist(data[2], bins = 20, color='red')
    plt.subplot(1, 3, 3)
    plt.title('Mediana')
    plt.hist(data[3], bins = 20, color='green')
    plt.show()


def information(data,names,idx):
    print(names[idx])

    print("Entropia danych wejsciowych: " + str(entropy(data[0])))
    code = Coder.encode(data[0])
    print("Srednia dlugosc slowa kodowego: " + str(word_length(data[0],code)))

    print("Entropia danych roznicowych (gorny sasiad): " + str(entropy(data[1])))
    code = Coder.encode(data[1])
    print("Srednia dlugosc slowa kodowego: " + str(word_length(data[1],code)))

    print("Entropia danych roznicowych (lewy sasiad): " + str(entropy(data[2])))
    code = Coder.encode(data[2])
    print("Srednia dlugosc slowa kodowego: " + str(word_length(data[2],code)))

    print("Entropia danych roznicowych (mediana): " + str(entropy(data[3])))
    code = Coder.encode(data[3])
    print("Srednia dlugosc slowa kodowego: " + str(word_length(data[3],code)))

def main():

    imgs, names = read_images()

    # ktory obrazek chcemy wczytac
    idx = 0
    data = get_data(imgs,idx)

    histogram(data,names,idx)
    information(data,names,idx)

    '''
    # Ksiazka przelaskowskiego (str. 81) entropia = 2.176
    test = np.array([1,1,1,1,1,1,
        2,2,2,2,2,2,
        2,2,2,2,2,2,
        3,3,3,3,
        4,4,4,4,4,
        5,5,5,5])
    print("Test: " + str(entropy(test))) # = 2.1755200043411453
    tcode = Coder.encode(test)
    print("Test2: " + str(word_length(test,tcode))) # = 2.22580645161
    '''

    '''
    image = ImageGenerator.generate_gaussian()
    data = np.array(image).flatten()
    code = Coder.encode_alt(data)
    print(code.code_book)
    print(code.encoded_data)
    '''


if __name__ == '__main__':
    main()
