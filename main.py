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


# def convert(numbers):
#   roman = {
#            "thousands": 0, 
#            "r_thousands": 0, 
#            "f_hundred": 0, 
#            "r_f_hundred": 0, 
#            "hundred": 0, 
#            "r_hundred": 0, 
#            "fifty":0, 
#            "r_fifty":0, 
#            "ten":0, 
#            "r_ten":0, 
#            "five":0,
#            "r_five":0, 
#            "one":0
#           }
#   thousands = ""
#   n_thousands = 0
#   r_thousands = 0
#   hundred = 0
#   r_f_hundred = 0
#   for item in numbers:
#     item = int(item)
#     print()

#     if item//1000 > 0:
#       # n_thousands = item //1000
#       # r_thousands = item % 1000
#       # roman['thousands'] = n_thousands
#       # roman['r_thousands'] = r_thousands
#       print(item)
#       print(item%1000)
#       roman['thousands'] = item//1000
#       roman['r_thousands'] = item%1000

#     if r_thousands >= 500:
#       roman['f_hundred'] = r_thousands//500
#       roman['r_f_hundred'] = r_thousands%500

#     if roman['r_f_hundred'] >= 100:
#       roman['hundred'] = roman['r_f_hundred']//100
#       roman['r_hundred'] = roman['r_f_hundred']%100

#     if roman['r_hundred'] >= 50:
#       roman['fifty'] = roman["r_hundred"]//50
#       roman['r_fifty'] = roman['r_hundred']%50

#     if roman['r_fifty'] >=10:
#       roman['ten'] = roman['r_fifty']//10
#       roman['r_ten'] = roman['r_fifty']%10
#       print(roman['r_ten'])

#     if roman['r_ten'] >=5:
#       roman['five'] = roman['r_ten']//5
#       roman['r_five'] = roman['r_ten']%5

#     roman['one'] = roman['r_five']

#   return roman

# print(convert(numbers))
# roman = convert(numbers)

# converted = {}

# def toRoman(roman):
#   converted = {'thousands':"", 'f_hundred':"", 'hundred':"", 'fifty':"", 'ten': "", 'five': "", "one": ""}
#   converted['thousands'] = str(roman["thousands"]) + "xM" 

#   if roman['f_hundred']!="":
#     if roman['f_hundred']<9:
#       for i in range(roman['f_hundred']):
#         converted['f_hundred'] +="D"
#     else:
#       converted['f_hundred'] += "CM"
      
#   if roman['hundred']!="":
#     if roman['hundred']<4:
#       for i in range(roman['hundred']):
#         converted['hundred'] += "C"
#     else:
#       converted['hundred'] += "CD"
  
#   if roman['fifty']!= " ":
#     if roman['fifty']<9:
#       for i in range(roman['fifty']):
#         converted['fifty'] += "L"
#     else:
#       converted['fifty'] += "XC"
#   if roman['ten']!=" ":
#     if roman['ten']<4:
#       for i in range(roman['ten']):
#         converted['ten'] += "X"
#     else:
#       converted['ten']+= "XL"

#   if roman['five'] !=" ":
#     if roman['five']<9:
#       for i in range(roman['five']):
#         converted['five'] +="V"
#     else:
#       converted['five']+="IX"

#   if roman['one'] !=" ":
#     if roman['one']<4:
#       for i in range(roman['one']):
#         converted['one'] +="I"
#     else:
#       converted['one'] +="IV"

#   # converted['f_hundred']= str(roman['f_hundred'])
#   return converted
#   #print(converted)

# print(toRoman(roman))

# converted = toRoman(roman)
# print(converted['thousands'] + converted['f_hundred']+converted['hundred']+converted['fifty']+converted['ten']+converted['five']+converted['one'])
  




  
