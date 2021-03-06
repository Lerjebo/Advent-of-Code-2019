
def tot_fuel(fuel):
    tot_num = 0
    num_fuel = (int((fuel/3)) - 2)
    if num_fuel > 0:
       tot_num = num_fuel + tot_fuel(num_fuel)
    return tot_num


def main():
    file = open(r'C:\Python\Advent_of_code_2019\day1.txt')
    text = file.read()
    numbers = text.split('\n')
    numbers = list(map(int, numbers))
    fuel = 0
    for num in numbers:
       fuel = fuel + tot_fuel(num)
    print(fuel)
if __name__ == '__main__':
  main()