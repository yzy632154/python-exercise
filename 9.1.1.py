number = 100
while number < 1000:
  a = number // 100
  b = number // 10 % 10
  c = number % 10
  if number == a**3 + b**3 + c**3:
    print (number)
  number += 1

  
