#Takes a lower case string, numbers pass through to convert roman
import regex as re


leet = {"a": "4", "b": "13", "c":"[", "d":"[)", "e":"3", "f":"|=","g": "6", "h":"#", "i": "|","j":".]", "k":"|<", "l":"1","m":"|y|", "n":"|\|", "o":"0", "p":"|>", "q":"o,","r":"I2", "s":"5", "t":"7", "u":"[_]", "v":"-v", "w":"|v|", "x":"}{", "y":"'/","z":"2", "1":"i", "2":"ii", "3":"iii", "4":"iv", "5":"v", "6":"vi", "7":"vii", "8":"viii", "9":"ix","0":".", " ":" ", "-":"3", ".":"3", ",":"3"}

input_string = "65WASHINGTON  Sen. Dianne Feinstein, D-Calif., a vocal advocate of gun control measures who was known for trying to find common 841895 ground with Republicans during her three decades in the Senate, has died, her office confirmed on Friday She was 999 xx"

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

roman = []

def to_roman():
  for item in numbers:
    # item = item[::-1]
    # roman = ""
    tens = ""
    hundreds = ""
    ones = item[-1]
    thousands = 0
  
    if len(item) > 1:
      tens = item[-2]
    
    if len(item) >2:
      hundreds = item[-3]
  
    if len(item)>3:
      thousands = item[:-3]
  
    r_numeral = ""
    
    
    
    
   
  
    if ones == "1":
      r_numeral = r_numeral + 1*"I"
  
    if ones == "2":
      r_numeral = r_numeral + 2*"I"
  
    if ones == "3":
      r_numeral = r_numeral + 3*"I"
  
    if ones == "4":
      r_numeral = r_numeral + "IV"
  
    if ones == "5":
      r_numeral = r_numeral + "V"
  
    if ones == "6":
      r_numeral = r_numeral + "VI"
  
    if ones == "7":
      r_numeral = r_numeral + "V" + 2*"I"
  
    if ones == "8":
      r_numeral = r_numeral + "V" + 3*"I"
  
    if ones == "9":
      r_numeral = r_numeral + "IX"
    
    
    # print(r_numeral)
    # print(tens)
  
    if tens == "1":
      r_numeral = "X" + r_numeral
  
    if tens == "2":
      r_numeral = 2*"X" + r_numeral
  
    if tens == "3":
      r_numeral = 3*"X" + r_numeral
  
    if tens == "4":
      r_numeral = "XL" + r_numeral
  
    if tens == "5":
      r_numeral = "L" + r_numeral
  
    if tens == "6":
      r_numeral = "LX" + r_numeral
  
    if tens == "7":
      r_numeral = "L" + 2*"X" + r_numeral
  
    if tens == "8":
      r_numeral = "L" + 3*"X" + r_numeral
  
    if tens == "9":
      r_numeral = "XC" + r_numeral
  
    if hundreds == "1":
      r_numeral = "C" + r_numeral
  
    if hundreds == "2":
      r_numeral = 2*"C" + r_numeral
  
    if hundreds == "3":
      r_numeral = 3*"C" + r_numeral
  
    if hundreds == "4":
      r_numeral = "CD" + r_numeral
  
    if hundreds == "5":
      r_numeral = "D"+ r_numeral
  
    if hundreds == "6":
      r_numeral = "D" + "C" + r_numeral
  
    if hundreds == "7":
      r_numeral = "D" + 2*"C" + r_numeral
  
    if hundreds == "8":
      r_numeral = "D" + 3*"C" + r_numeral
  
    if hundreds == "9":
      r_numeral = "CM" + r_numeral
  
  
    if int(thousands)>1:
      r_numeral = str(thousands) + "xM" + r_numeral  
    # print(r_numeral)
    roman.append(r_numeral)
    
    # return r_numeral
    # print(type(r_numeral))
to_roman()    
print(roman)
      