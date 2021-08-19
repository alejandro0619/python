# every vowel become a 's'

def translator(phrase):
  result = " "
  for letter in phrase:
    if letter.lower() in 'aeiou':
      if letter.isupper():
        result = result + 'S'
      else:
       result = result + 's'
    else:
      result = result + letter
  return result


      