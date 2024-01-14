#Takes a lower case string, numbers pass through to convert roman
import regex as re


leet = {"a": "4", "b": "13", "c":"[", "d":"[)", "e":"3", "f":"|=","g": "6", "h":"#", "i": "|","j":".]", "k":"|<", "l":"1","m":"|y|", "n":"|\|", "o":"0", "p":"|>", "q":"o,","r":"I2", "s":"5", "t":"7", "u":"[_]", "v":"-v", "w":"|v|", "x":"}{", "y":"'/","z":"2", "1":"i", "2":"ii", "3":"iii", "4":"iv", "5":"v", "6":"vi", "7":"vii", "8":"viii", "9":"ix","0":".", " ":" ", "-":"3", ".":"3", ",":"3"}

input_string = "9WASHINGTON  Sen. Dianne Feinstein, D-Calif., a vocal advocate of gun control measures who was known for trying to find common 8418956 ground with Republicans during her three decades in the Senate, has died, her office confirmed on Friday She was 90 xx"

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
print(numbers)

for item in numbers:
  length = len(item)
  roman = ""
  while length > 0:
   
    
    # print(length)
    # print(str(item[-1]) + " last number")
    digit = item[length-1]
    roman += digit
    print(digit)
    length-=1
    print(str(length) + "length")
    print("roman" + roman)
    # if digit == 9:
    #   digit = "IX"
    #   roman+=digit
    #   print(roman)
      # print("length "+str(length))
      
      # length-=1
      # print("length - "+str(length))
      # print(item)

  # for num in item:
  #   length = len(num)
    
                 
  #   print(num[-len(num)])

