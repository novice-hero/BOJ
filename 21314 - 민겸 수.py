word = input()
answer_min = ''
answer_max = ''

m = 0
for i in range(len(word)):
  if word[i] == 'M':
    m+=1
  elif word[i] == 'K':
    if m:
      answer_min += str(pow(10, m)+5)
      answer_max += str(pow(10, m)*5)
    else:
      answer_min += '5'
      answer_max += '5'
    m=0
  
if m:
  answer_min += str(pow(10, m-1))
  while m:
    answer_max += '1'
    m -= 1

print(answer_max)
print(answer_min)