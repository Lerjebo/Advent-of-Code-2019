#påbyggnad på dag 2
#opcodesen är ex [1002,4,3,4] börja läs från höger första 2 siffor = 02 = multiplikation, 01 hade gett addition
#siffra 3 är 0 = position mode, så samma som uppgift 2 ta värdet som är på index 4 i listan
#siffra 4 är 1 = immediate mode, ta då bara 3 i detta fall inte det som är på index 3
#siffra 5 är 0 = position spara då number[number[i+1]]*number[i+2] på plats number[number[i+3]]
#ints kan vara negativt
#kan inte alltid öka med 4 nu om opcoden är 3 så ett input värde och sätter i indexet så 3,50 resulterar i att number[50] = index, INPUT
#opcode 4 är OUTPUT så 4,50 gör number[50] till en output
#stoppa fortfarande vid 99,3,0,4,0,99 skickar ut värdet den får som input till en output sen stoppar programmet

def choose_op(input):
    file = open(r'C:\Users\lerjebo\Python\Advent_of_code\Day5.txt')
    text = file.read()
    words = text.split(',')
    numbers = list(map(int, words))
   # print(len(numbers))
    output = -1
    i = 0
    while i < len(numbers):
        #print(i)
        if numbers[i] == 1:
            print(numbers[i+1], numbers[i+2])
            numbers[numbers[i + 3]] = (numbers[numbers[i + 1]] + numbers[numbers[i + 2]])
            i = i + 4
        elif numbers[i] == 2:
            numbers[numbers[i + 3]] = (numbers[numbers[i + 1]] * numbers[numbers[i + 2]])
            i = i + 4
        elif numbers[i] == 3:
            numbers[numbers[i + 1]] = input
            i = i + 2
        elif numbers[i] == 4:
            output = numbers[numbers[i + 1]]
            i = i + 2
        elif numbers[i] == 5:
            if numbers[numbers[i + 1]] != 0:
                i = numbers[numbers[i + 2]]

            else:
                i = i + 3
        elif numbers[i] == 6:
            if numbers[numbers[i + 1]] == 0:
                i = numbers[numbers[i + 2]]
            else:
                i = i + 3
        if numbers[i] == 7:
            if numbers[numbers[i + 1]] < numbers[numbers[i + 2]]:
                numbers[numbers[i + 3]] = 1
            else:
                numbers[numbers[i + 3]] = 0
            i = i + 4
        if numbers[i] == 8:
            if numbers[numbers[i + 1]] == numbers[numbers[i + 2]]:
                numbers[numbers[i + 3]] = 1
            else:
                numbers[numbers[i + 3]] = 0
            i = i + 4
        elif numbers[i] == 99:
            break
        else:
            separated = str(numbers[i])
            de = ''
            c = numbers[i + 1]
            b = numbers[i + 2]
            a = numbers[i + 3]
            opcode = [c, b, a]
            index = 0
            if separated[-2:] == '01':
               de = 'add'
            elif separated[-2:] == '02':
                de = 'multiple'
            elif separated[-2:] == '03':
                de = 'input'
            elif separated[-2:] == '04':
                de = 'output'
            elif separated[-2:] == '05':
                de = 'jump-if-true'
            elif separated[-2:] == '06':
                de = 'jump-if-false'
            elif separated[-2:] == '07':
                de = 'less than'
            elif separated[-2:] == '08':
                de = 'equals'

            for dig in range(len(separated)-3, -1, -1):
                if separated[dig] == '0':
                    opcode[index] = numbers[i + 1 + index]
                    index = index + 1
                elif separated[dig] == '1':
                    opcode[index] = i + 1 + index
                    index = index + 1
            if de == 'add':
                #print(opcode, c, b, a)
                numbers[opcode[2]] = numbers[opcode[0]] + numbers[opcode[1]]
                i = i + 4
            elif de == 'multiple':
                numbers[opcode[2]] = numbers[opcode[0]] * numbers[opcode[1]]
                i = i + 4
            elif de == 'input':
                numbers[opcode[0]] = input
                i = i + 2
            elif de == 'output':
                output = numbers[opcode[0]]
                i = i + 2
            elif de == 'jump-if-true':
                if numbers[opcode[0]] != 0:
                    i = numbers[opcode[1]]
                else:
                    i = i + 3
            elif de == 'jump-if-false':
                if numbers[opcode[0]] == 0:
                    i = numbers[opcode[1]]
                else:
                    i = i + 3
            elif de == 'less than':
                if numbers[opcode[0]] < numbers[opcode[1]]:
                    numbers[opcode[2]] = 1
                else:
                    numbers[opcode[2]] = 0
                i = i + 4
            elif de == 'equals':
                if numbers[opcode[0]] == numbers[opcode[1]]:
                    numbers[opcode[2]] = 1
                else:
                    numbers[opcode[2]] = 0
                i = i + 4
    return output


print(choose_op(5))





















