# https://www.reddit.com/r/adventofcode/comments/e7aqcb/2019_day_7_part_2_confused_with_the_question/
from itertools import permutations
#https://github.com/kresimir-lukin/AdventOfCode2019/blob/master/day11.py
#  registration = [[' ']*40 for _ in range(6)] 2d array med bestämd size
def choose_op(data, index, rel_base, inputs=0):
    numbers = data
    relative_base = rel_base
    output = 0
    i = index
    while True:
        opcode = op_decode(numbers[i])
        de = opcode[0] + 10 * opcode[1]
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
            break
        elif de == 4:
            c = numbers[get_op1(numbers, i, opcode[2], relative_base)]
            output = c
            i = i + 2
            break
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
            output = 99
            break
    return numbers, output, i, relative_base



def painting(start):
    index = 0
    data = indata()
    memory = [0]*10000
    data = data + memory

    output1 = 0 #color
    output2 = 0 #direction
    color = start
    dx = {0: 0, 90: 1, 180: 0, 270: -1}
    dy = {0: 1, 90: 0, 180: -1, 270: 0}
    x = y = direction = 0
    panel = {(x, y): color}
    #print(panel)
    rel_base = 0
    while True:
        if (x, y) in panel:
            data, color, index, rel_base = choose_op(data, index, rel_base, panel[(x, y)])
        else:
            data, color, index, rel_base = choose_op(data, index, rel_base, 0)

        data, output1, index, rel_base = choose_op(data, index, rel_base)
        data, output2, index, rel_base = choose_op(data, index, rel_base)
        if output1 != 99 or output2 != 99 or color != 99:
            panel.update({(x, y): output1})
            if output2 == 1:
                direction += 90
                direction = direction % 360
            elif output2 == 0:
                direction -= 90
                if direction < 0:
                    direction += 360
            x = x + dx[direction]
            y = y + dy[direction]
        else:
            break
    if start == 0:
        return len(panel)
    elif start == 1:
        return panel
    else:
        return print('FEL')
def print_reg():
    panel = painting(1)
    for row in range(6):
        for col in range(42):
            if panel.get((col, -row)) == 1:
                print("\u2588", end="")
            else:
                print(" ", end="")
        print()

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



def indata():
    file = open(r'C:\Users\lerjebo\Python\Advent_of_code\Day11.txt')
    text = file.read()
    words = text.split(',')
    numbers = list(map(int, words))
    return numbers


def start():
    print('Part1:', painting(0))
    print_reg()

start()
