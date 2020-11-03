#PART 1:
#   Complete program to find the larger of the two input numbers and
#   **place the larger number in num1 and the smaller in num2.

#   e.g. 1: if input num1 = 15 and num2 = 13 ===> no change
#   e.g. 2: if input num1 = 13 and num2 = 15 ===> num1 = 15 and num2 = 13


num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))

if num2 > num1:
    # num1, num2 = num2, num1
    temp = num1
    num1 = num2
    num2 = temp

# DO NOT CHANGE PRINT STATEMENT BELOW
print('The larger of the two numbers is {:d} and the smaller is {:d}'
      .format(num1, num2))


#PART 2:
#   Complete program to find the largest of the three input numbers
#   below and store it in variable max
input1 = int(input('Enter the 1st number: '))
input2 = int(input('Enter the 2nd number: '))
input3 = int(input('Enter the 3rd number: '))

max = input1

if input2 > max:
    max = input2

if input3 > max:
    max = input3

# DO NOT CHANGE PRINT STATEMENT BELOW
print('The largest of the three numbers is {:d}' .format(max))





