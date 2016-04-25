import os
import numpy as np
import matplotlib.pyplot as plt
import math
import collections
from PIL import Image

import HuffmanCodec.HuffmanCoder as coder
import HuffmanCodec.HuffmanDecoder as decoder
# import ImageGenerator
import PredictiveCodec

np.set_printoptions(threshold=np.nan)

path = "data/"
output = "histograms/"
output_encode = "encoded/"

def entropy(data):
    # Wyliczenie entropii. Przyjmuje tablice.
    freq_data = collections.Counter(data)
    probs = [float(x) / len(data) for x in freq_data.values()]
    return -1 * sum(a * b for a,b in zip(probs,[math.log2(x) for x in probs]))

def word_length(data,code):
    # Srednia dlugosc slowa kodowego.
    codes = code
    codes = collections.OrderedDict(sorted(codes.items()))
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
        #print(filename + ": " + img.mode, img.size)
        imgs.append(img);
        names.append(filename)
    return (imgs,names)

def encode_predictive_data(images,idx):
    pix = []
    pix.append(np.array(images[idx], dtype='int64').flatten())
    for i in range(1,4):
        pix.append(PredictiveCodec.encode_predictive(images[idx],i))
    return pix  # Tablica: 0 - dane wejsciowe, 1 - lewy sasiad, 2 - gorny sasiad, 3 - mediana)

# TODO
# Input: zdekodowane dane algorytmem kompresji Hufmana
# [0] - normal
# [1] - left diff
# [2] - upper diff
# [3] - median
def decode_predictive_data(decoded_huf_data):
    return 0

def histogram(data,names,idx):
    plt.suptitle('Histogramy danych roznicowych dla ' + names[idx])
    plt.subplot(1, 4, 1)
    plt.title('Oryginal')
    plt.hist(data[0], bins = 20, color='grey')
    plt.subplot(1, 4, 2)
    plt.title('Lewy sasiad')
    plt.hist(data[1], bins = 20, color='blue')
    plt.subplot(1, 4, 3)
    plt.title('Gorny sasiad')
    plt.hist(data[2], bins = 20, color='red')
    plt.subplot(1, 4, 4)
    plt.title('Mediana')
    plt.hist(data[3], bins = 20, color='green')
    #plt.show()
    plt.savefig(output + names[idx])
    plt.close()


def encode_huffman_data(data,names,idx):
    print(names[idx])
    code = []

    print("Entropia danych wejsciowych: " + str(entropy(data[0])))
    code.append(coder.encode(data[0]))
    print("Srednia dlugosc slowa kodowego: " + str(word_length(data[0],code[0].code_book)))

    print("Entropia danych roznicowych (gorny sasiad): " + str(entropy(data[1])))
    code.append(coder.encode(data[1]))
    print("Srednia dlugosc slowa kodowego: " + str(word_length(data[1],code[1].code_book)))

    print("Entropia danych roznicowych (lewy sasiad): " + str(entropy(data[2])))
    code.append(coder.encode(data[2]))
    print("Srednia dlugosc slowa kodowego: " + str(word_length(data[2],code[2].code_book)))

    print("Entropia danych roznicowych (mediana): " + str(entropy(data[3])))
    code.append(coder.encode(data[3]))
    print("Srednia dlugosc slowa kodowego: " + str(word_length(data[3],code[3].code_book)))

    # zwraca obiekt typu HuffmanCode
    return code

def decode_huffman_data(codes):
    decoded_huf_data = []

    # Normal:
    decoded_huf_data.append(decoder.decode(codes[0]))

    # Left diff:
    decoded_huf_data.append(decoder.decode(codes[1]))

    # Upper diff:
    decoded_huf_data.append(decoder.decode(codes[2]))

    # Median:
    decoded_huf_data.append(decoder.decode(codes[3]))

    # zwraca tablice zdekodowanych wartosci
    return decoded_huf_data


# MJK: Problem z rozmiarem plikow. Moze ktos ma lepszy pomysl, jak to zapisac
#- do dekodowania warto jakies dane jednak miec ;)
def save_code(codes,names,idx):

    with open(output_encode+names[idx]+"_normal_code.txt", 'wb') as f:
        f.write(codes[0].encoded_data)
        f.close()

    with open(output_encode+names[idx]+"_left_code.txt", 'wb') as f:
        f.write(codes[1].encoded_data)
        f.close()

    with open(output_encode+names[idx]+"_upper_code.txt", 'wb') as f:
        f.write(codes[2].encoded_data)
        f.close()

    with open(output_encode+names[idx]+"_median_code.txt", 'wb') as f:
        f.write(codes[3].encoded_data)
        f.close()

def main():

    imgs, names = read_images()


    # ktory obrazek chcemy wczytac
    idx = 0
    #for idx in range(0,len(imgs)):

    print("Predictive encoding: " + names[idx])
    pred_data = encode_predictive_data(imgs,idx)

    #histogram(data,names,idx)

    print("Huffmann encoding: " + names[idx])
    huff_data = encode_huffman_data(pred_data,names,idx)

    print("Saving: " + names[idx])
    save_code(huff_data,names,idx)

    print("Huffmann decoding: " + names[idx])
    decoded_huf_data = decode_huffman_data(huff_data)

    print("Predictive decoding: " + names[idx])
    decoded_pred_data = decode_predictive_data(decoded_huf_data);

    # test:
    print("Normal data to be compressed: "  + names[idx])
    for i in range(0,10):
        print(int(pred_data[0][i]),  ", ")

    print("\n")
    print("Normal data uncompressed: "  + names[idx])
    for i in range(0,10):
        print(int(decoded_huf_data[0][i]), ", ")
    print("\n")



    ''''
    data = (PredictiveCodec.encode_predictive(imgs[idx],1))
    code = Coder.encode(data)
    print("Dlugosc slowa Pred: " + str(word_length(data,code)))
    '''

    '''
    # Ksiazka przelaskowskiego (str. 81) entropia = 2.176
    test = np.array([1,1,1,1,1,1,
        2,2,2,2,2,2,
        2,2,2,2,2,2,
        3,3,3,3,
        4,4,4,4,4,
        5,5,5,5])
    test_pred = ([1,0,0,0,0,0,
        1,0,0,0,0,0,
        0,0,0,0,0,0,
        1,0,0,0,
        1,0,0,0,0,
        1,0,0,0])
    print("Entropia: " + str(entropy(test))) # = 2.1755200043411453
    tcode = Coder.encode(test)
    print("Dlugosc slowa " + str(word_length(test,tcode))) # = 2.22580645161

    print("Entropia Pred: " + str(entropy(test_pred))) # = 0.6373874992221911
    tcodet = Coder.encode(test_pred)
    print("Dlugosc slowa Pred: " + str(word_length(test_pred,tcodet))) # = 1.0
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
