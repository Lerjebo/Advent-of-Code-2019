# (.) = empty, (#) = asteroid
# x= distans från vänster kant, y = distans från top kant

import math
from numpy import add, subtract, divide, multiply
import collections
def iterating():
    asteroids = []
    with open(r'C:\Users\lerjebo\Python\Advent_of_code\Day10.txt') as f:
        file = f.read()
    lines = file.split('\n')
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if line[x] == '#':
                asteroids.append((x, y))
    print(asteroids)
    max_vis = []
    station = (26, 36)
    ast_num = []
    for origin in asteroids:
       vis, orig = visible(asteroids, origin)
       max_vis = max_vis, [vis, orig]
       ast_num.append(vis)
    print("Part1: ", station) # (26,36) är stationen på

    centered = []
    for asteroid in asteroids:
        centered.append(asteroid)
    centered.remove((26, 36))
    circulate(centered, station)

def sort_x(x):
    return x[0]
def sort_y(y):
    return y[1]
def circulate(centered, station):
    copied = centered.copy()
    quadrant1 = []
    quadrant2 = []
    quadrant3 = []
    quadrant4 = []
    x = station[0]
    y = station[1]
    for i in range(len(centered)):
        asteroid = copied.pop(0)
        if asteroid[0] >= x and asteroid[1] < y:
            quadrant1.append(asteroid)
        elif asteroid[0] > x and y <= asteroid[1]:
            quadrant2.append(asteroid)
        elif asteroid[0] <= x and y < asteroid[1]:
            quadrant3.append(asteroid)
        elif asteroid[0] < x and y >= asteroid[1]:
            quadrant4.append(asteroid)
    temp = []
    for asteroid in quadrant1:
        temp.append((asteroid[0] - x, y - asteroid[1]))
    quadrant1 = temp.copy()
    temp[:] = []
    for asteroid in quadrant2:
        temp.append((asteroid[0] - x, y - asteroid[1]))
    quadrant2 = temp.copy()
    temp[:] = []
    for asteroid in quadrant3:
        temp.append((asteroid[0] - x, y - asteroid[1]))
    quadrant3 = temp.copy()
    temp[:] = []
    for asteroid in quadrant4:
        temp.append((asteroid[0] - x, y - asteroid[1]))
    quadrant4 = temp.copy()
    temp[:] = []

    quadrant1 = sorted(quadrant1, key=sort_x)
    quadrant2 = sorted(quadrant2, key=sort_y, reverse=True)
    quadrant3 = sorted(quadrant3, key=sort_x, reverse=True)
    quadrant4 = sorted(quadrant4, key=sort_y)

    dydx1 = trig(quadrant1)
    dydx1 = collections.OrderedDict(sorted(dydx1.items(), reverse=True))
    dydx2 = trig(quadrant2)
    dydx2 = collections.OrderedDict(sorted(dydx2.items()))
    dydx3 = trig(sorted(quadrant3, key=sort_x, reverse=True))
    dydx3 = collections.OrderedDict(sorted(dydx3.items()))
    dydx4 = trig(sorted(quadrant4, key=sort_y))
    dydx4 = collections.OrderedDict(sorted(dydx4.items()))

    destroyed = 0
    while dydx1 and dydx2 and dydx3 and dydx4:
        dydx1, destroyed = lasered(dydx1, destroyed)
        dydx2, destroyed = lasered(dydx2, destroyed)
        dydx3, destroyed = lasered(dydx3, destroyed)
        dydx4, destroyed = lasered(dydx4, destroyed)




def lasered(dydx, destroyed):
    new_dict = {}
    zero_list = []
    index = 0
    for key_val in dydx:
        if key_val == 0:
            destroyed += 1
            zero_list = dydx.pop(key_val)
            ans = zero_list[0]
            for i in range(len(zero_list)):
                if (ans[0] + ans[1]) > (zero_list[i][0] + zero_list[i][1]):
                    ans = zero_list[i]
                    index = i
            zero_list.pop(index)
            if destroyed == 200:
                print("Part2: ", (26 - abs(ans[0])) * 100 + 36 - abs(ans[1]))
            break
    for key_value in dydx:
        destroyed += 1
        list = dydx[key_value]
        small = list[0]
        index = 0
        for i in range(len(list)):

            if (small[0] + small[1]) > (list[i][0] + list[i][1]):
                small = list[i]
                index = i
        if destroyed == 200:
            answer = (26 - abs(small[0])) * 100 + 36 - abs(small[1])
            print("Part2: ", answer)
            list.pop(index)
        else:
            list.pop(index)
        if len(list) > 0:
                new_dict.update({key_value: list})
    if len(zero_list) > 0:
        new_dict.update({0: zero_list})

    return new_dict, destroyed

def trig(quadrant):
    dydx = {}
    list = []
    # start = quadrant1.pop(0)
    # list.append(start)
    index = 0
    copied = quadrant.copy()
    for i in range(len(copied)):
        if copied[i][0] == 0 or copied[i][1] == 0:
            list.append(copied[i])
            delta = 0
            index = i + 1
    if len(list) > 0:
        dydx.update({delta: list.copy()})
        list[:] = []
    for i in range(index, len(copied)):
        if i == len(copied):
            break
        start = copied[i]
        list.append(start)
        delta = abs(float((start[1] * 10000) / (start[0] * 10000)) / 10000)
        #if start != copied[-1]:
        for x in range(i + 1, len(copied)):
            if x == len(copied):
                break
            second = copied[x]
            delta2 = abs(float((second[1] * 10000) / (second[0] * 10000)) / 10000)
            if delta == delta2:
                list.append(second)
                copied.remove(second)
        dydx.update({delta: list.copy()})
        list[:] = []

    return dydx



def visible(asteroids, origin):
    copied = asteroids.copy()
    max_y = max(map(lambda point: point[1], asteroids))
    max_x = max(map(lambda point: point[0], asteroids))
    for target in asteroids:
        if target == origin:
            copied.remove(target)
            continue

        diff = subtract(target, origin)
        step = divide(diff, math.gcd(*diff))
        for i in range(1, max_x):
            hidden_point = tuple(add(target, multiply(step, i)))
            if hidden_point in copied:
                copied.remove(hidden_point)

            x, y = hidden_point
            if x < 0 or y < 0 or x > max_x or y > max_y:
                break
    return len(copied), origin

iterating()
