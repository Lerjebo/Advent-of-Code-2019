def yeet(n, v):
    file = open(r'C:\Users\lerjebo\Python\Advent_of_code\day2.TXT')
    text = file.read()
    words = text.split(',')
    numbers = list(map(int, words))
    numbers[1] = n
    numbers[2] = v
    i = 0
    while i < len(numbers):
        if numbers[i] == 1:
            numbers[numbers[i + 3]] = (numbers[numbers[i + 1]] + numbers[numbers[i + 2]])
        elif numbers[i] == 2:
            numbers[numbers[i + 3]] = (numbers[numbers[i + 1]] * numbers[numbers[i + 2]])
        elif numbers[i] == 99:
            break
        i = i + 4
    return numbers[0]

def input_var():
    for noun in range(99):
        for verb in range(99):
          num = yeet(noun, verb)
          if num == 19690720:
              print(noun*100+verb)
              break



input_var()


