#6 digit nummer
#minst 2 siffror bredvid varandra är samma
#siffrorna minskar aldrig från vänster till höger
#antal möjliga passwords i rangen 147981 till 691423

def criteria1(number):
    if 147981 <= number <= 691423:
        return True
    return False

def criteria2(number):
  number = str(number)
  #print(number)
  i = 1
  #if number[0] == number[1] == number[2]:
   #   i = 3
  check = [0]*10
  double_dig = 0
  test = number[0]
  while i < len(number):
      if test == number[i]:
         #return True 4.1
         check[int(test)] = check[int(test)] + 1
      else:
          test = number[i]
      i = i + 1
  for x in check:
      if x < 2 and x > 0:
          return True
  return False


def criteria3(number):
    number = str(number)
    i = 0
    while i < len(number)-1:
         if(number[i] > number[i+1]):
             return False
         i = i + 1
    return True

def possiblePasswords():
    passwords = 0
    for x in range(147981, 691423):
        if criteria1(x) == criteria2(x) == criteria3(x) == True:
           passwords = passwords + 1
    print(passwords)


possiblePasswords()