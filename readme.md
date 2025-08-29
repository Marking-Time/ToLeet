
# To Leet 
## Code is documented
This repo contains sveral branches to represent the different methods I used to solve the problem. All branches contain the same to_leet and find_numbers code, but the code for the to_roman changes with each branch.
1. The main branch is my best effort, because it seems most readable to me.
2. The bunch_of_ifs branch uses many if statements to convert the arabic numerals to Roman Numerals.
3. I have created a new branch named test.  I probably should have named it differently because I have tradtionaly used that name as a sort of throw away name when I was working on desktops and networks. The branch was created to try out unit testing, but in the process I found some bugs. This file will track the changes to on the test branch, which will prbably become the main branch. Status:
    - I keep getting an out of range error when I run the code for unit testing.  I think it may be due to the test filel being a single string as opposed to a list that the regular code processes.
    - I finished the day with some progress. I need to do some testing to check for functionality
4. depricated-initial is my first atempt ... it works but is kludgy

## to_leet - This code converts english to leet.
This is the refactored code. The original code, along with the readme, is in the depricated-initial branch as well as the main branch.

## find_numbers
Uses regx to find and extract the numbers from an input string. Returns a list.

## to_roman
### Works as expected
Returns a list of numbers found in the text converted to Roman Numberals.  Roman Numerals do not work above 4999, so I have used the convention of taking the number of thousands as a muliplier to the letter "M" and prepended that to the standard roman numeral

## Unit Testing
- I created four unit tests one for the ones, tens, hundreds and thousands places
- All run correctly with no errors

## To Do
- Add unit testing for to_roman
- Unit testing revealed some issues that I'm working on
  
##### 1/26/2024
- I had the code tested and running for a bit, but ended the day with three tests failing
- Not sure what is going on, but it has something to do with how the zeros are processed. It may need to be refactored at this point.
##### 1/27/2024
- Worked all day on testing in the test branch
- still having trouble in the logical program flow
- I need to diagram it out
##### 1/28/2024
- Unit testing complete
- Need to spruce up the code and repo
- Deleted test branch ... all changes are made in the main branch





