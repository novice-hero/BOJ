N, M = map(int, input().split())
words = {}
for _ in range(N):
  word = input()
  if len(word) < M:
    continue
  
  if word not in words:
    words[word] = 1
  else:
    words[word] += 1

result = list(zip(words.keys(), words.values()))
result.sort(key=lambda x:(-x[1], -len(x[0]), x[0]))
for res in result:
  print(res[0])