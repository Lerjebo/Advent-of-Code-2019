#25 pixlar bred 6 pixlar hög per layer
from array import *


def split_layers():
    file = open(r'C:\Users\lerjebo\Python\Advent_of_code\Day8.txt')
    text = file.read()
    width = 25
    length = 6
    layer_size = width*length
    layer_amount = int(len(text)/layer_size)
    layers = []
    zero = []
    one = []
    two = []
    for i in range(layer_amount):
        layers.append(text[layer_size*i:layer_size*(i+1)])

    for i in range(layer_size):
        for j in range(layer_amount):

            if int(text[i+j*layer_size]) != 2:
               print("\u2588" if int(text[i+j*layer_size]) == 1 else " ", end="") # end="" gör så den inte hoppar ner en line \n är standard
               break
        if (i + 1) % width == 0:
            print()

    for layer in layers:
        z, o, t = data(layer)
        zero.append(z)
        one.append(o)
        two.append(t)
    multiplied = one[0]*two[0]
    fewest = zero[0]
    for i in range(len(zero)):
        if zero[i] < fewest:
            fewest = zero[i]
            multiplied = one[i]*two[i]
    print("8.1,", multiplied)

def data(layer):
    zero = 0
    one = 0
    two = 0
    for i in range(len(layer)):
        l = int(layer[i])
        if l == 0:
            zero += 1
        elif l == 1:
            one += 1
        elif l == 2:
            two += 1

    return zero, one, two


split_layers()
