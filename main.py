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

# TODO: Sprawdzic dla jakis malych tablic, czy dobrze to liczy.
def entropy(data):
    # Wyliczenie entropii. Przyjmuje tablice.
    freq_data = collections.Counter(data)
    probs = [float(x) / len(data) for x in freq_data.values()]
    return -1 * sum(a * b for a,b in zip(probs,[math.log2(x) for x in probs]))

def word_length(data):
    # srednia dlugosc slowa kodowego

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
    for i in range(1,3):
        pix.append(PredictiveCodec.encode_predictive(images[idx],i))
    return pix  # Tablica: 0 - dane wejsciowe, 1 - lewy sasiad, 2 - gorny sasiad, 3 - mediana)


def main():

    imgs, names = read_images()

    # ktory obrazek chcemy wczytac
    idx = 0
    data = get_data(imgs,idx)

    plt.suptitle('Histogramy danych roznicowych dla ' + names[idx])
    plt.subplot(1, 3, 1)
    plt.title('Lewy sasiad')
    plt.hist(data[0], bins = 20, color='blue')
    plt.subplot(1, 3, 2)
    plt.title('Gorny sasiad')
    plt.hist(data[1], bins = 20, color='red')
    plt.subplot(1, 3, 2)
    #plt.title('Mediana')
    # TODO
    #plt.show()

    print("Entropia dla " + names[idx])
    print("danych wejsciowych: " + str(entropy(data[0])))
    print("danych roznicowych (gorny sasiad): " + str(entropy(data[1])))
    print("danych roznicowych (lewy sasiad): " + str(entropy(data[2])))

    code_data = Coder.encode(data)

    # TODO: Srednia dlugosc bitowa kodu wyjsciowego


    '''
    image = ImageGenerator.generate_gaussian()
    data = np.array(image).flatten()
    code = Coder.encode_alt(data)
    print(code.code_book)
    print(code.encoded_data)
    '''


if __name__ == '__main__':
    main()
