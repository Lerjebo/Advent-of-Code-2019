
def find_between(s, start, end):
  return (s.split(start))[1].split(end)[0]

def start():
    file = open(r'C:\Users\lerjebo\Python\Advent_of_code\Day12.txt')
    text = file.read()
    lines = text.split('\n')
    # numbers = list(map(int, words))
    pos = []
    vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for line in lines:
        x = int(find_between(line, "x=", ","))
        y = int(find_between(line, "y=", ","))
        z = int(find_between(line, "z=", ">"))
        pos.append([x, y, z])
    #print(pos)
    #print(vel)

    x = 0
    while True:
    #for x in range(0, 1000):
        for j in range(len(vel)):
            vel[j][0] = calculate(vel[j][0], j, pos[0][0], pos[1][0], pos[2][0], pos[3][0])
            vel[j][1] = calculate(vel[j][1], j, pos[0][1], pos[1][1], pos[2][1], pos[3][1])
            vel[j][2] = calculate(vel[j][2], j, pos[0][2], pos[1][2], pos[2][2], pos[3][2])
        #print(vel, 'vel', x+1)
        for i in range(len(pos)):
            pos[i][0] = pos[i][0] + vel[i][0]
            pos[i][1] = pos[i][1] + vel[i][1]
            pos[i][2] = pos[i][2] + vel[i][2]
        #print(pos, 'pos', x+1)


        x += 1
    #energy = 0
    #for i in range(4):
    #    energy = energy + (abs(pos[i][0]) + abs(pos[i][1]) + abs(pos[i][2])) * (abs(vel[i][0]) + abs(vel[i][1]) + abs(vel[i][2]))
    #print('Part1:', energy)


def calculate(vel, index, coord1, coord2, coord3, coord4):
    compare = 0
    values = [coord1, coord2, coord3, coord4]
    if index == 0:
        compare = coord1
    elif index == 1:
        compare = coord2
    elif index == 2:
        compare = coord3
    elif index == 3:
        compare = coord4
    difference = coord_check(compare, values)
    return vel + difference

def coord_check(coord, values):
    difference = 0
    for key in values:
        if key > coord:
            difference += 1
        elif key < coord:
            difference -= 1
    return difference


start()