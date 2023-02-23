def bin_to_dec(bin_str):
  returnNum = 0
  currentPower = pow(2, len(bin_str) - 1)
  for char in bin_str:
    if char == '1':
      returnNum += currentPower
    currentPower //= 2
  return returnNum
