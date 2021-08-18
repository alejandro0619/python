is_male = False
is_over_eighteen = False

def is_a_male(is_male, is_over_eighteen):
  if is_male and (is_over_eighteen):
    print("Is male and over 18")
  elif is_male and not(is_over_eighteen):
    print("Male but not over 18")
  elif is_male or is_over_eighteen:
    return print("May be male or over 18")
  elif not(is_male) and is_over_eighteen:
    print("Not male but over 18")
  else:
    return print("he's neither male nor over 18")

#  Comparisons:

def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    print(str(num1))
  elif num2 >= num1 and num2 >= num3:
    print(str(num2))
  elif num3 >= num1 and num3 >= num2:
    print(str(num3))

max_num(1, 2, 3)