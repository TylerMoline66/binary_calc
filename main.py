'''
Welcome to your second project of the course. This project is complex, so please read all of the instructions carefully!

Introduction (Read This!)
This project will use some of the code you have written previously, namely the dec_to_bin() function and the bin_to_dec() function. It will also require you to write additional functions to perform all of the binary calculations (Add, Subtract, Multiply, Divide).

Due to the challenging nature of this project, You will need to break it up into smaller segments. This project listing has some suggestions as to how to approach the project and take it one step at a time.

You are not allowed to use external modules, nor are you allowed to use base casting. Python has built-in functions for base casting a string to base-2 binary number or a decimal int to a binary number. For this, project, however, we will be building all of the functions the long way. 

For this assignment, you are NOT going to convert the binary numbers to decimal numbers, perform math and convert back to binary.

NOTE: You are, however, allowed to use bit-shifting operators, if you want to research those.

Off-limits:

Base casting
External Modules or Libraries
OK to Use:

Bit-shifting operators
Your teammates

The Project
You will be building a Binary Calculator. This calculator will be a console application and will support the following:

1. Binary to Decimal Conversion
2. Decimal to Binary Conversion
3. Binary Addition
4. Binary Subtraction (ONLY Positive results)
5. Binary Multiplication
6. Binary Division


Suggested Tasks
It will be much easier to build this project if you build the code one piece at a time. Here is a suggested task list you might use to break the project up into smaller tasks:

1. Make sure the bin_to_dec() function works and is returning an int result
2. Make sure the dec_to_bin() function is working and returns a String result.
3. Build a bin_add(bin_str_1, bin_str_2) function that adds two binary numbers together and returns a string representing the resulting binary number
4. Build a bin_sub(bin_str_1, bin_str_2) function that subtracts the second binary number from the first binary number and returns the result. If the first number is smaller than the second number, this would result in a negative result. Instead, your program should return an "Error: Negative result".
5. Build a bin_mul(bin_str_1, bin_str_2) function that multiplies two binary numbers together and returns the result as a String representing a binary number
6. Build a bin_div(bin_str_1, bin_str_2) function that divides the first number by the second number and returns the result as a String representing a binary number.
7. Build a menu for your program
8. Allow the user to enter a menu option and call the appropriate functions
9. Add a Quit function
10. Wrap the code in a while loop that breaks on Quit
11. Tie it all together
'''
import bin_to_dec


def add_binary(num1,num2):
    bin1 = num1[::-1] 
    bin2 = num2[::-1] 
    carry = []

    biggerLength = max(len(num1), len(num2)) + 1
    for num in range(0, biggerLength):
        carry.append('0')

    while(len(bin1) < biggerLength):
        bin1 += '0'
    while(len(bin2) < biggerLength):
        bin2 += '0'
        
    sum_binary = [] 

    for i in range(0, biggerLength): 

        if bin1[i] == '0' and bin2[i] == '0' and carry[i] == '0':
            sum_binary.append('0')
        elif bin1[i] == '0' and bin2[i] == '0' and carry[i] == '1':
            sum_binary.append('1')    
        elif bin1[i] == '1' and bin2[i] == '0' and carry[i] == '0':
            sum_binary.append('1')
        elif bin1[i] == '1' and bin2[i] == '0' and carry[i] == '1':
            sum_binary.append('0')
            carry[i + 1] = '1'
        elif bin1[i] == '0' and bin2[i] == '1' and carry[i] == '0':
            sum_binary.append('1')
        elif bin1[i] == '0' and bin2[i] == '1' and carry[i] == '1':
            sum_binary.append('0')
            carry[i + 1] = '1'
        elif bin1[i] == '1' and bin2[i] == '1' and carry[i] == '0':
            sum_binary.append('0')
            carry[i + 1] = '1'
        elif bin1[i] == '1' and bin2[i] == '1' and carry[i] == '1':
            sum_binary.append('1')
            carry[i + 1] = '1'

    while(sum_binary[-1] == '0'):
        if len(sum_binary) == 1:
            break
        sum_binary.pop(-1)
    sum_binary.reverse()   
    return ''.join(sum_binary)

    
print('ADDITION TESTS')
print(add_binary('10101','1001011'))
print(add_binary('10001', '100010'))
print(add_binary("10101010", "11001100"))
print(add_binary("101011010", "1000111100"))
print(add_binary("11111111", "1"))



def bin_multiply(num_1, num_2):
    addition_list = []

    for enum, digit in enumerate(num_2[::-1]):
      if digit == '1':
        addition_list.append(num_1 + ('0' * enum))
    sum = '00000000'
    for each in addition_list:
        sum = add_binary(sum, each)
    return sum

print('MULTIPLICATION TESTS')
print(bin_multiply('01000000','00010000'))



def bin_subtract(num_1, num_2):
    if bin_to_dec.bin_to_dec(num_1) < bin_to_dec.bin_to_dec(num_2):
      return None
  
    bin1 = []
    bin2 = []

    for i in num_1:
      bin1.append(i)
    bin1.reverse() 
    for i in num_2:
      bin2.append(i)
    bin2.reverse()

    biggerLength = max(len(num_1), len(num_2))

    while(len(bin1) < biggerLength):
        bin1.append('0')
    while(len(bin2) < biggerLength):
        bin2.append('0')



    final = []
    for i in range(0, biggerLength):
        if bin1[i] == '0' and bin2[i] == '0':
            final.append('0')
        elif bin1[i] == '1' and bin2[i] == '0':
            final.append('1')
        elif bin1[i] == '1' and bin2[i] == '1':
            final.append('0')
        elif bin1[i] == '0' and bin2[i] == '1':
            targetIndex = i + 1
            while bin1[targetIndex] == '0':
                bin1[targetIndex] = '1'
                targetIndex += 1
            bin1[targetIndex] = '0'
            final.append('1')
  
    while(final[-1] == '0'):
        if len(final) == 1:
            break
        final.pop(-1)
    final.reverse()
    return ''.join(final)
        
print('SUBTRACTION TESTS')
print(bin_subtract('10001', '000110'))



def bin_divide(num_1, num_2):
  if '1' not in num_2:
      return 'undefined'
  if '1' not in num_1:
      return '0'
  if bin_to_dec.bin_to_dec(num_1) < bin_to_dec.bin_to_dec(num_2):
      return f"0 r{num_1.lstrip('0')}"

  answer = []
  substring = ''

  for i, char in enumerate(num_1):
    substring += char
    if bin_subtract(substring, num_2) == None:
      answer.append('0')
    else:
      answer.append('1')
      substring = bin_subtract(substring, num_2) #WHAT?!?!?!

  while(answer[0] == '0'):
    if len(answer) == 1:
        break
    answer.pop(0)

  final_answer = ''.join(answer)
  if substring == '0':
    return final_answer
  return f"{final_answer} r{substring}"

print('DIVISION TESTS')
print(bin_divide('01', '011'))