
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
  - Multiplying the // (floor ) result by M - Returns whole number division
  - Multiplying the % result by M - Returns remainder of whole number division
  - Logic problems

#### Convert pseudo logic
  - number // 1000 - gets number of 1000s
  - number % 1000 - gets *remainder* of 1000s division
  - remainder is divided by 500 to get the "D" number in roman

#### Begin Day with data cleaning 
- remove depricated code
- add labels to print to show var names

### Code breaks arabic into dictionary at roman intervals 
- Still some problems -  code doesn't trigger untill over 1000. This stops it from running when the number is less.
  - Need to remove the 0-9 digits from the toleet code and allow it to be converted in to_roman
### Arabic to Roman Complete

## To Do:
  - Need to fix fours and nines
  - Need to ensure all numbers in list are processed
# LOL .... This might be right
### Need to run some tests, but toRoman() seems to be feature complete
- Fails on fours
- Problem with convert
  - The convert() function doesn't work correctly with all numbers
  - Need to rework the logic

