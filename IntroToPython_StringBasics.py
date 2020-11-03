alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# A print statement to display the value of string variable alphabet along with its length, for which
#   we use function "len" 
print("length of {:s} is {:d}".format(alphabet,len(alphabet)))

# Problem #1:
#   Uncomment and run the code snippet below (3 lines) multiple times. What does it do???
#   Now, modify the code snippet to generate and store a random integer in variable "someNumber",
#   between 0 and one less than the length of string variable "alphabet". Display the
#   character at that location in string alphabet using indexing symbols [ ] and variable
#   "someNumber". You program should work for ANY string in variable alphabet.

#    Your program should work for ANY string in variable alphabet.

import random
someNumber = random.randint(0, len(alphabet)-1)
print(someNumber)


# Problem #2:
#   Uncomment and run the code snippet below. It displays the character at
#   the location input by the user into variable "char_location". For example,
#   alphabet[2] displays the THIRD character in variable "alphabet". What happens
#   if you input 50? -50? Modify it so that it works even when user enters an
#   invalid index. In such a case, display an error message to the user instead of
#   the character at the input location

#    Your program should work for ANY string in variable alphabet.

char_location=int(input('Enter number to use as a character location or index: '))
if -len(alphabet) <= char_location <= len(alphabet) - 1:
    print("letter at {:d} is {:s}".format(char_location,alphabet[char_location]))
else:
    print("error invalid index")
