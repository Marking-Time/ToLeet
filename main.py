#Takes a lower case string, numbers pass through
import regex as re


leet = {"a": "4", "b": "13", "c":"[", "d":"[)", "e":"3", "f":"|=","g": "6", "h":"#", "i": "|","j":".]", "k":"|<", "l":"1","m":"|y|", "n":"|\|", "o":"0", "p":"|>", "q":"o,","r":"I2", "s":"5", "t":"7", "u":"[_]", "v":"-v", "w":"|v|", "x":"}{", "y":"'/","z":"2", "1":"i", "2":"ii", "3":"iii", "4":"iv", "5":"v", "6":"vi", "7":"vii", "8":"viii", "9":"ix","0":".", " ":" ", "-":"3", ".":"3", ",":"3"}

input_string = "9WASHINGTON  Sen. Dianne Feinstein, D-Calif., a vocal advocate of gun control measures who was known for trying to find common 5641650 ground with Republicans during her three decades in the Senate, has died, her office confirmed on Friday She was 90 "

def to_leet(string):
  string = str(string)
  string = string.lower()
  new_string = ""
  for letter in string:   
    letter = leet[letter]
    new_string += letter
  return new_string

print(input_string)
print(to_leet(input_string))
print()

def to_roman(number):
  number1 = ""
  text = ""
  for letter in input_string:
    try:
      letter =  int(letter)
    except:
      letter = letter
    if type(letter) == int:
      number1+= str(letter)
    else:
      text += str(letter)
   
  return number1, text

print(to_roman(input_string))


#################################
################### Regex ###################
m = re.findall(r"(\d+)", input_string)
# print(m.group(0,1))
# print(m.groups())
print(m)

for item in m:
  print()
  print(item)
  # print("length: " + str(len(item)))
  length = len(item)
  print("length: " + str(length))
  for number in item:
    print(number)



  
