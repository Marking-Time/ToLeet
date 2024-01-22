#Takes a lower case string, numbers pass through to convert roman
from typing import final
import regex as re


leet = {"a": "4", "b": "13", "c":"[", "d":"[)", "e":"3", "f":"|=","g": "6", "h":"#", "i": "|","j":".]", "k":"|<", "l":"1","m":"|y|", "n":"|\|", "o":"0", "p":"|>", "q":"o,","r":"I2", "s":"5", "t":"7", "u":"[_]", "v":"-v", "w":"|v|", "x":"}{", "y":"'/","z":"2", "1":"i", "2":"ii", "3":"iii", "4":"iv", "5":"v", "6":"vi", "7":"vii", "8":"viii", "9":"ix","0":".", " ":" ", "-":"3", ".":"3", ",":"3"}

input_string = "65WASHINGTON  Sen. Dianne Feinstein, D-Calif., a vocal advocate of gun control measures who was known for trying to find common 841895 ground with Republicans during her three decades in the Senate, has died, her office confirmed on Friday She was 999 xx23"

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
m=[]
def find_numbers(input_string):
  m = re.findall(r"(\d+)", input_string)
  print("Numbers list as m: "+str(m))
  return m

# print(find_numbers(input_string))
# print(m)

  
numbers = find_numbers(input_string)
print(numbers)

roman = []

romanD = {
  'ones': {
    '1': "I",
    '2': "II",
    '3': "III",
    '4': "IV",
    '5': "V",
    '6': "VI",
    '7': "VII",
    '8': "VII",
    '9': "IX"  
  }, 
  'tens': {
      '1': "X",
      '2': "XX",
      '3': "XXX",
      '4': "XL",
      '5': "L",
      '6': "LX",
      '7': "LXX",
      '8': "LXXX",
      '9': "XC"
        },
  'hundreds': {
    '1': "C",
    '2': "CC",
    '3': "CCC",
    '4': "CD",
    '5': "D",
    '6': "DC",
    '7': "DCC",
    '8': "DCCC",
    '9': "CM",
  }
  
}

def to_roman(numbers):
  # print(numbers)
  ones =''
  tens = ''
  hundreds = ''
  rnumber = ''
  for item in numbers:
    # print("test item: "  +item)
    ones = item[-1]
    rnumber = romanD['ones'][ones]
        
    if len(item[-2])>0:
      tens = item[-2]
      rnumber = romanD['tens'][tens] + rnumber

    
    if len(item) >2:
      hundreds= item[-3]
      print("hundreds: " + hundreds)
      rnumber = romanD['hundreds'][hundreds] + rnumber

    roman.append(rnumber)
  return rnumber
    # contunue

to_roman(numbers)
print(roman)
# to_roman(numbers)
# print(romanD['ones'][ones])