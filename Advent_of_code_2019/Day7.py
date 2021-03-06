# https://www.reddit.com/r/adventofcode/comments/e7aqcb/2019_day_7_part_2_confused_with_the_question/
from itertools import permutations
def choose_op(data, inputs, feedback=False, index=0):
    numbers = data
    output = -1
    i = index
    flag = True
    while i < len(numbers):
        opcode = op_decode(numbers[i])
        de = opcode[0] + 10*opcode[1]
        if de == 1:
            c = get_op1(numbers, i, opcode[2])
            b = get_op2(numbers, i, opcode[3])
            numbers[numbers[i + 3]] = c + b
            i = i + 4
        elif de == 2:
            c = get_op1(numbers, i, opcode[2])
            b = get_op2(numbers, i, opcode[3])
            numbers[numbers[i + 3]] = c * b
            i = i + 4
        elif de == 3:
            numbers[numbers[i + 1]] = inputs.pop(0)
            i = i + 2
        elif de == 4:
            c = get_op1(numbers, i, opcode[2])
            output = c
            i = i + 2
            if feedback:
                return output, i
        elif de == 5:
            c = get_op1(numbers, i, opcode[2])
            b = get_op2(numbers, i, opcode[3])
            if c != 0:
                i = b
            else:
                i = i + 3
        elif de == 6:
            c = get_op1(numbers, i, opcode[2])
            b = get_op2(numbers, i, opcode[3])
            if c == 0:
                i = b
            else:
                i = i + 3
        elif de == 7:
            c = get_op1(numbers, i, opcode[2])
            b = get_op2(numbers, i, opcode[3])
            if c < b:
                numbers[numbers[i + 3]] = 1
            else:
                numbers[numbers[i + 3]] = 0
            i = i + 4
        elif de == 8:
            c = get_op1(numbers, i, opcode[2])
            b = get_op2(numbers, i, opcode[3])
            if c == b:
               numbers[numbers[i + 3]] = 1
            else:
                numbers[numbers[i + 3]] = 0
            i = i + 4
        elif de == 99:
            if feedback:
                return output, None
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

def get_op1(numbers, index, mode):
    return numbers[numbers[index + 1]] if mode == 0 else numbers[index + 1]


def get_op2(numbers, index, mode):
    return numbers[numbers[index + 2]] if mode == 0 else numbers[index + 2]

def start():
    outputs = []
    for phases in permutations(range(5,10)):
        outputs = outputs + [find_input(phases)]
    print(max(outputs))
    return 0


def find_input(phase):
    programs, index, inputs = [], [], []
    file = open(r'C:\Users\lerjebo\Python\Advent_of_code\Day7.txt')
    text = file.read()
    words = text.split(',')
    numbers = list(map(int, words))
    output = 0
    for i in range(0, 5):
        programs.append(numbers.copy())
        index.append(0)
        inputs.append([phase[i]])
    while index[0] is not None:
        for i in range(0, 5):
            inputs[i].append(output)
            output, ind = choose_op(programs[i], inputs[i], True, index[i])
            index[i] = ind


    return inputs[0][0]

start()
