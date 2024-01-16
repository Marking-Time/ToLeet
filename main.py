#Takes a lower case string, numbers pass through to convert roman
import regex as re


leet = {"a": "4", "b": "13", "c":"[", "d":"[)", "e":"3", "f":"|=","g": "6", "h":"#", "i": "|","j":".]", "k":"|<", "l":"1","m":"|y|", "n":"|\|", "o":"0", "p":"|>", "q":"o,","r":"I2", "s":"5", "t":"7", "u":"[_]", "v":"-v", "w":"|v|", "x":"}{", "y":"'/","z":"2", "1":"i", "2":"ii", "3":"iii", "4":"iv", "5":"v", "6":"vi", "7":"vii", "8":"viii", "9":"ix","0":".", " ":" ", "-":"3", ".":"3", ",":"3"}

input_string = "95WASHINGTON  Sen. Dianne Feinstein, D-Calif., a vocal advocate of gun control measures who was known for trying to find common 8418955 ground with Republicans during her three decades in the Senate, has died, her office confirmed on Friday She was 90 xx"

def to_leet(string):
  string = str(string)
  string = string.lower()
  new_string = ""
  for letter in string:   
    letter = leet[letter]
    new_string += letter
  return new_string

print("input_string: "+input_string)
print("toleet: "+to_leet(input_string))
print()


#################################
################### Regex ###################
def find_numbers(input_string):
  m = re.findall(r"(\d+)", input_string)
  print("Numbers list as m: "+str(m))
  return m

numbers = find_numbers(input_string)
print()
print(numbers)


def to_Roman():
  roman = ""
  for item in numbers:
    print(item)
    # for digit in item:
    #   # print(digit)
    #   if digit == '9':
    #     roman += 'IX '
    #     # print(roman)
    return roman

# print(to_Roman())

print(numbers)
for item in numbers:
  # item = item[::-1]
  roman = ""
  print(item)
  for digit in item:
    print(digit)
    digit = digit[-1]
    if digit == '4':
      digit = 'IV'
    if digit == '5':
      digit = "V"
      roman+=digit
    if digit == '9':
      digit = "IX"
      roman+=digit
    if digit == '1':
      digit = 'I'
      roman+=digit
    if digit == '2':
      digit = 'II'
      roman+=digit
    if digit == '3':
      digit = 'III'
      roman+=digit
    if digit == '6':
      digit = 'VI'
      roman+=digit
    if digit == '7':
      digit = 'VII'
      roman+=digit
    if digit == '8':
      digit = 'VIII'
      roman+=digit
      
    
      

  print(roman)