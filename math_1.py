import bin_to_dec

# This is the addition function
def add_binary(num_1,num_2):
    bin1 = num_1[::-1] #slicing to reverse and create a list
    bin2 = num_2[::-1] 
    carry = []

    biggerLength = max(len(num_1), len(num_2)) + 1 #finding the longest number
    for num in range(0, biggerLength):
        carry.append('0')               #making carry list the same length as the longest number

    while(len(bin1) < biggerLength):    #making the 2 numbers the same length by adding zeros at the end
        bin1 += '0'
    while(len(bin2) < biggerLength):
        bin2 += '0'
        
    sum_binary = [] 

    for i in range(0, biggerLength):    #iterating over the numbers and adding and carrying

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

    while(sum_binary[-1] == '0'):   #if the last number is 0 and the length is 1 break
        if len(sum_binary) == 1:
            break
        sum_binary.pop(-1)          #otherwise remove the zeros from the end
    sum_binary.reverse()            #reverse the number
    return ''.join(sum_binary)      #join the list into a string again

    


#This is the multiply function
def bin_multiply(num_1, num_2):
    addition_list = []

    for enum, digit in enumerate(num_2[::-1]):  #enumerating so we can look at each individual digit
      if digit == '1':                          
        addition_list.append(num_1 + ('0' * enum))  #if the digit is 1 then append num_1 plus the required number of zeros to addition_list
    sum = '00000000'
    for each in addition_list:                  #for every digit in addition_list, we are running the add_binary function on the sum
        sum = add_binary(sum, each)
    return sum


# This is the subtract function
def bin_subtract(num_1, num_2):
# This section will make sure the first number is not smaller than the second number. just to make sure the answer is not negative
    biggerLength = max(len(num_1), len(num_2))
    num_1 = num_1.zfill(biggerLength)
    num_2 = num_2.zfill(biggerLength)
    if num_2 > num_1:
     return None
  
    bin1 = []
    bin2 = []
# This section will create a list from the binary strings passed into the function and 
    for i in num_1:
      bin1.append(i)
    bin1.reverse() 
    for i in num_2:
      bin2.append(i)
    bin2.reverse()

    final = []
# This is where the math happens, it evaluates num_1 and num_2 at the same index and subtracts or borrows if needed 
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
  
# removes extra zeros at the end, reverses the numbers then joins them to a string
    while(final[-1] == '0'):
        if len(final) == 1:
            break
        final.pop(-1)
    final.reverse()
    return ''.join(final)

        
# This is the divide function, it depends on the subtract function
def bin_divide(num_1, num_2):
# This first section checks that the first number is not smaller than the second number
  if '1' not in num_2:
      return 'undefined'
  if '1' not in num_1:
      return '0'

  biggerLength = max(len(num_1), len(num_2))
  num_1 = num_1.zfill(biggerLength)
  num_2 = num_2.zfill(biggerLength)
  if num_2 > num_1:
     return "Invalid"

  answer = []
  substring = ''
# This will look through num_1 and do long division on it?
  for i, char in enumerate(num_1):
    substring += char
    if bin_subtract(substring, num_2) == None:
      answer.append('0')
    else:
      answer.append('1')
      substring = bin_subtract(substring, num_2) #WHAT?!?!?!
      
# This will remove the leading zeros
  while(answer[0] == '0'):
    if len(answer) == 1:
        break
    answer.pop(0)
# This section determines if the remainder is returned in the result
  final_answer = ''.join(answer)
  if '0' in substring and '1' not in substring:
    return final_answer
  return f"{final_answer} r{substring}"
