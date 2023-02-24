def dec_to_bin(num):
  place = 1
  result = ''

  while place<num:
    place *= 2

  while True:
    if not num and not place:
      if result[0] == '0':
        result = result[1::]
      return result

    if num >= place:
      result += '1'
      num -= place

    else:
      result +='0'

    place//=2
    
    

