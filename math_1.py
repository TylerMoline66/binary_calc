import bin_to_dec


def add_binary(num_1,num_2):
    bin1 = num_1[::-1] 
    bin2 = num_2[::-1] 
    carry = []

    biggerLength = max(len(num_1), len(num_2)) + 1
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

    



def bin_multiply(num_1, num_2):
    addition_list = []

    for enum, digit in enumerate(num_2[::-1]):
      if digit == '1':
        addition_list.append(num_1 + ('0' * enum))
    sum = '00000000'
    for each in addition_list:
        sum = add_binary(sum, each)
    return sum



def bin_subtract(num_1, num_2):
    biggerLength = max(len(num_1), len(num_2))
    num_1 = num_1.zfill(biggerLength)
    num_2 = num_2.zfill(biggerLength)
    if num_2 > num_1:
     return None
  
    bin1 = []
    bin2 = []

    for i in num_1:
      bin1.append(i)
    bin1.reverse() 
    for i in num_2:
      bin2.append(i)
    bin2.reverse()

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
        

def bin_divide(num_1, num_2):
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
  if '0' in substring and '1' not in substring:
    return final_answer
  return f"{final_answer} r{substring}"
