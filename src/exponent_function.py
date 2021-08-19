
def exponent_function(base_num, pow_num):
  result = 1
  for i in range(pow_num):
    result = result * base_num
  return result
  
print(exponent_function(2, 3))