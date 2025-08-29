#Takes a lower case string, numbers pass through to convert roman
#from typing import final
import re as re

# ==== arabic to leet dictinary ===
leet = {"a": "4", "b": "13", "c":"[", "d":"[)", "e":"3", "f":"|=","g": "6", "h":"#", "i": "|","j":".]", "k":"|<", "l":"1","m":"|y|", "n":"^", "o":"0", "p":"|>", "q":"o,","r":"I2", "s":"5", "t":"7", "u":"[_]", "v":"-v", "w":"|v|", "x":"}{", "y":"'/","z":"2", "1":"i", "2":"ii", "3":"iii", "4":"iv", "5":"v", "6":"vi", "7":"vii", "8":"viii", "9":"ix","0":".", " ":" ", "-":"3", ".":"3", ",":"3",".":"..."}

# ==== gets text from user ===
input_string = input("Enter the text and or number to convert to Leet and Roman Numerals: \n")

# =========== Code to convert to leet ============
# == Numbers converted to roman numeral DIGITS ===
def to_leet(string):
  string = str(string)
  string = string.lower()
  new_string = ""
  for letter in string:   
    letter = leet[letter]
    new_string += letter
  return new_string

# === Printing Output === 
print("======= Prints ======= ")
print("1. Input String") 
print("2. The Leet for the Input String")
print()

print("input_string: "+input_string)
print("toleet: "+to_leet(input_string))
print()


################### Regex used to convert to roman numerals ###################
m=[]
def find_numbers(input_string):
  m = re.findall(r"(\d+)", input_string)
  # print("Numbers list as m: "+str(m))
  return m

print("RegEx output: ")
print(find_numbers(input_string))
print()

  
numbers = find_numbers(input_string)
# print(numbers)


# =========== Dictinary  for Roman Numerals======
romanD = {
  'ones': {
    '0': "",
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
      '0': "",
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
    '0': "",
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

# ========= Code to convert Arabic to Roman ======== 
roman = []
def to_roman(numbers):
  # print(numbers)
  ones =''
  tens = ''
  hundreds = ''
  thousands = ''
  rnumber = ''
  
  for item in numbers:
    if len(item) == 1:
      ones = romanD['ones'][item[0]]
      
      rnumber = ones
      roman.append(rnumber)
   
    if len(item) == 2:
      ones = romanD['ones'][item[-1]]
      tens = romanD['tens'][item[-2]]
      
      rnumber = tens+ones     
      roman.append(rnumber)

    if len(item) == 3:
      ones = romanD['ones'][item[-1]]
      tens = romanD['tens'][item[-2]]
      hundreds = romanD['hundreds'][item[-3]]
     
      rnumber = hundreds+tens+ones
      roman.append(rnumber)

    if len(item)>3:
      ones = romanD['ones'][item[-1]]
      tens = romanD['tens'][item[-2]]
      hundreds = romanD['hundreds'][item[-3]]
      thousands = item[:-3]
      thousands = thousands+'xM'

      rnumber = thousands+hundreds+tens+ones
      roman.append(rnumber)
      # print('thousands --> '+thousands)
      # return rnumber
  
  return rnumber
# ========= End of For Loop & to_roman() =======

print("Numbers converted to Roman: "+ to_roman(numbers))
