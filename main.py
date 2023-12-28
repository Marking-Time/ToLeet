#Takes a lower case string, numbers pass through

leet = {"a": "4", "b": "13", "c":"[", "d":"[)", "e":"3", "f":"|=","g": "6", "h":"#", "i": "|","j":".]", "k":"|<", "l":"1","m":"|y|", "n":"|\|", "o":"0", "p":"|>", "q":"o,","r":"I2", "s":"5", "t":"7", "u":"[_]", "v":"-v", "w":"|v|", "x":"}{", "y":"'/","z":"2", "1":"i", "2":"ii", "3":"iii", "4":"iv", "5":"v", "6":"vi", "7":"vii", "8":"viii", "9":"ix","0":".", " ":" ", "-":"3", ".":"3", ",":"3"}

input_string = "WASHINGTON  Sen. Dianne Feinstein, D-Calif., a vocal advocate of gun control measures who was known for trying to find common ground with Republicans during her three decades in the Senate, has died, her office confirmed on Friday She was 90"

def to_leet(string):
  string = str(string)
  string = string.lower()
  new_string = ""
  for letter in string:   
    letter = leet[letter]
    new_string += letter
  return new_string
print(to_leet(input_string))

#def to_roman(number):


  
