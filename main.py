import math_1
import bin_to_dec
import dec_to_bin

while True:
    print('''\n        *** Binary Calculator ***
    ---------------------------------\n
    1:  Binary to Decimal Conversion
    2:  Decimal to Binary Conversion
    3:  Add two Binary Numbers
    4:  Subtract two Binary Numbers
    5:  Multiply two Binary Numbers
    6:  Divide two Binary Numbers\n
    (Q)uit
    ''')
    decision = input('what would you like to do?  ').lower()

    if decision == '1':
        user_num_1 = input('what binary number would you like to convert?  ')
        print(f"\nThat binary number is --> {bin_to_dec.bin_to_dec(user_num_1)}\n")
    elif decision == '2':
        user_num_1 = int(input('what decimal number would you like to convert?  '))
        print(f"\nThat binary number is --> {dec_to_bin.dec_to_bin(user_num_1)}\n")
    elif decision == '3':
        num_1 = input('What is the first binary number? ')
        num_2 = input('What is the second binary number? ')
        print(f'\nThe answer is: {math_1.add_binary(num_1, num_2)}\n')
    elif decision == '4':
        num_1 = input('What is the first binary number? ')
        num_2 = input('What is the second binary number? ')
        print(f'\nThe answer is: {math_1.bin_subtract(num_1, num_2)}\n')
    elif decision == '5':
        num_1 = input('What is the first binary number? ')
        num_2 = input('What is the second binary number? ')
        print(f'\nThe answer is: {math_1.bin_multiply(num_1, num_2)}\n')
    elif decision == '6':
        num_1 = input('What is the first binary number? ')
        num_2 = input('What is the second binary number? ')
        print(f'\nThe answer is: {math_1.bin_divide(num_1, num_2)}\n')
    elif decision == 'q':
        print('Goodbye')
        break