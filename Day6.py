#AAA)BBB, bbb är i omloppsbana runt aaa
# c omloppar b som omloppar a, c indirekt omloppar a
#com = center of mass omloppar inget allt annat gör
#kanske kan leka med en rekursiv metod som kollar omlopp

def orbiting():
    file = open(r'C:\Users\lerjebo\Python\Advent_of_code\Day6.txt')
    text = file.read()
    words = text.split('\n')
    orbit = []
    for x in words:
        orbit = orbit + [x.split(')')] #index 1 omlöpper index 0
    count = 0
    orbits = dict(reversed(x) for x in orbit)
    for obj in orbits.keys():
        while obj in orbits:
            obj = orbits[obj]
            count = count + 1
    print('6.1, ' + str(count))

    obj = 'YOU'
    you = {}
    steps = 0
    while obj in orbits:
        obj = orbits[obj]
        you[obj] = steps
        steps = steps + 1
    print(you)
    obj = 'SAN'
    san = {}
    steps = 0
    while obj in orbits:
        obj = orbits[obj]
        san[obj] = steps
        steps = steps + 1
    print(san)
    steps = 0
    connections = []
    for i in you:
        for j in san:
            if i != j:
                steps = steps + 1
            else:
                connections = connections + [you[i] + san[j]]
    answer = sorted(connections)
    answer = answer[0]
    print('6.2, ' + str(answer))


orbiting()