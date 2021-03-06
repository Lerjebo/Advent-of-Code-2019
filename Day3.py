# spara alla sträckor hur ena sladden gått sen jämnför alla steg med andra och spara korsningar
# 4d array? ger dock bara slut distans... hmmm, antar man kan spara x,y koordinat efter varje steg för se vart den gått men är ju
#rätt mycket data så kanske inte så snyggt
from collections import defaultdict

def yeet(wire):
    i = 0
    board = defaultdict(lambda: defaultdict(int))
    x = 0
    y = 0
    for coordinate in wire:
        steps = int(coordinate[1:])
        if coordinate[0] == 'R':
            board = swag(board, coordinate[0], steps, x, y)
            x = x + steps
        elif coordinate[0] == 'L':
            board = swag(board, coordinate[0], steps, x, y)
            x = x - steps
        elif coordinate[0] == 'U':
            board = swag(board, coordinate[0], steps, x, y)
            y = y + steps
        elif coordinate[0] == 'D':
            board = swag(board, coordinate[0], steps, x, y)
            y = y - steps
        i = i + 1
    return board

def yought(wire, target):
    x = 0
    y = 0
    cross = []
    for coordinate in wire:
        steps = int(coordinate[1:])
        dir = coordinate[0]
        for step in range(steps):
            if dir == 'R':
                x = x + 1
            elif dir == 'L':
                x = x - 1
            elif dir == 'U':
                y = y + 1
            elif dir == 'D':
                y = y - 1
            if target[x][y] == 1:
                cross = cross +[(x, y)]
    return cross

def swag(board, dir, steps, x, y):
    for step in range(steps):
        if dir == 'R':
            board[x + 1][y] = 1
            x = x + 1
        elif dir == 'L':
            board[x - 1][y] = 1
            x = x - 1
        elif dir == 'U':
            board[x][y + 1] = 1
            y = y + 1
        elif dir == 'D':
            board[x][y - 1] = 1
            y = y - 1
    return board
def memes(intersections, wire):
    s = []
    for inter in intersections:
       # print(inter[0])
        i = 0
        x = 0
        y = 0
        for coordinate in wire:
            steps = int(coordinate[1:])
            dir = coordinate[0]
            for step in range(steps):
                if dir == 'R':
                    i = i + 1
                    x = x + 1
                elif dir == 'L':
                    i = i + 1
                    x = x - 1
                elif dir == 'U':
                    i = i + 1
                    y = y + 1
                elif dir == 'D':
                    i = i + 1
                    y = y - 1
                if inter[0] == x and inter[1] == y:
                    s = s + [i]
                    i = 0
                    break
    return s

def mainYeet():
    file = open(r'C:\Users\lerjebo\Python\Advent_of_code\Day3.txt')
    text = file.read()
    wires = text.split('\n')
    wire1 = wires[0].split(',')
    wire2 = wires[1].split(',')

    wire1_mapped = yeet(wire1)
    intersections = yought(wire2, wire1_mapped)
    #print(intersections)
    distance = []
    for inter in intersections:
        distance = distance + [abs(inter[0]) + abs(inter[1])]
    print('3.1:', sorted(distance)[0])

    steps1 = memes(intersections, wire1)
    steps2 = memes(intersections, wire2)
    steps = []
    for x in range(len(steps1)):
        steps = steps + [steps1[x] + steps2[x]]
    print('3.2:', sorted(steps)[0])







mainYeet()


