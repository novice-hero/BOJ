doc = input()
word = input()
idx = 0
cnt = 0
while True:
  idx = doc.find(word)

  if idx == -1:
    print(cnt)
    break

  cnt += 1
  doc = doc[idx+len(word):]