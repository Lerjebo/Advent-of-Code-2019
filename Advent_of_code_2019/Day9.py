# https://www.reddit.com/r/adventofcode/comments/e7aqcb/2019_day_7_part_2_confused_with_the_question/
from itertools import permutations
def choose_op(data, inputs):
    numbers = data
    relative_base = 0
    output = 0
    i = 0
    memory = [0]*10000
    numbers = numbers + memory
    #print(numbers)
    while i < len(numbers):
        opcode = op_decode(numbers[i])
        #print(opcode)
        de = opcode[0] + 10*opcode[1]
        if de == 1:
            c = numbers[get_op1(numbers, i, opcode[2], relative_base)]
            b = numbers[get_op2(numbers, i, opcode[3], relative_base)]
            a = get_op3(numbers, i, opcode[4], relative_base)
            numbers[a] = c + b
            i = i + 4
        elif de == 2:
            c = numbers[get_op1(numbers, i, opcode[2], relative_base)]
            b = numbers[get_op2(numbers, i, opcode[3], relative_base)]
            a = get_op3(numbers, i, opcode[4], relative_base)
            numbers[a] = c * b
            i = i + 4
        elif de == 3:
            c = get_op1(numbers, i, opcode[2], relative_base)
            numbers[c] = inputs
            i = i + 2
        elif de == 4:
            c = numbers[get_op1(numbers, i, opcode[2], relative_base)]
            output = c
            i = i + 2
        elif de == 5:
            c = numbers[get_op1(numbers, i, opcode[2], relative_base)]
            b = numbers[get_op2(numbers, i, opcode[3], relative_base)]
            if c != 0:
                i = b
            else:
                i = i + 3
        elif de == 6:
            c = numbers[get_op1(numbers, i, opcode[2], relative_base)]
            b = numbers[get_op2(numbers, i, opcode[3], relative_base)]
            if c == 0:
                i = b
            else:
                i = i + 3
        elif de == 7:
            c = numbers[get_op1(numbers, i, opcode[2], relative_base)]
            b = numbers[get_op2(numbers, i, opcode[3], relative_base)]
            a = get_op3(numbers, i, opcode[4], relative_base)
            if c < b:
                numbers[a] = 1
            else:
                numbers[a] = 0
            i = i + 4
        elif de == 8:
            c = numbers[get_op1(numbers, i, opcode[2], relative_base)]
            b = numbers[get_op2(numbers, i, opcode[3], relative_base)]
            a = get_op3(numbers, i, opcode[4], relative_base)
            if c == b:
               numbers[a] = 1
            else:
                numbers[a] = 0
            i = i + 4
        elif de == 9:
            c = numbers[get_op1(numbers, i, opcode[2], relative_base)]
            relative_base = relative_base + c
            i = i + 2
        elif de == 99:
            break

    return output

def op_decode(code):
    digits = [0]*5
    position = len(digits)-1
    while code > 0 and position >= 0:
        digits[len(digits)-1 - position] = code % 10
        code = int(code / 10)
        position = position - 1
    return digits

def get_op1(numbers, index, mode, relative_base):

    if mode == 0:
        return numbers[index + 1]
    elif mode == 1:
        return index + 1
    elif mode == 2:
        return relative_base + numbers[index + 1]



def get_op2(numbers, index, mode, relative_base):

    if mode == 0:
        return numbers[index + 2]
    elif mode == 1:
        return index + 2
    elif mode == 2:
        return relative_base + numbers[index + 2]

def get_op3(numbers, index, mode, relative_base):

    if mode == 0:
        return numbers[index + 3]
    elif mode == 1:
        return index + 3
    elif mode == 2:
        return relative_base + numbers[index + 3]

def start():
    print('9.1,',choose_op(indata(), 1))
    print('9.2,',choose_op(indata(), 2))
    return 0

def indata():
    file = open(r'C:\Users\lerjebo\Python\Advent_of_code\Day9.txt')
    text = file.read()
    words = text.split(',')
    numbers = list(map(int, words))
    return numbers


start()
