
# To Leet
## This code converts english to leet.
### To Do:
- Roman Numeral Conversion - The existing code only converts the digits  and not into the roman numeral syntax
- Consider making this into an object based program with multiple output methods -  like into other character systems
- Worked on code to convert roman numerals into arabic
  - string to int conversions may require try except logic
  - Code doesn't work properly - exits with traceback
  - Consider breaking out roman2arabic untill it works
  - may need regx
- Got to_roman to work ouputting a tuple including a list of numbers and a string of the input text without numbers:
  - need to put individual numbers into list together
-  Put numbers into a string
### Regex yields a list of all the matches
- m is a list of all the matches
- each list member must be converted to roman numerals
- Broke list into individual numbers and calculated the length
### Code put into functions
- Roman numerals only go to 3999, so the calcualtor will compensate by:
  - multiplying the // (floor ) result by M
  - Logic problems 