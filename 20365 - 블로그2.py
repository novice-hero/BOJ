n = int(input())
word = input()

color = {'B':0, 'R':0}
color[word[0]]+=1

for i in range(1,n):
  if word[i]!=word[i-1]:
    color[word[i]] += 1

print(min(color['B'], color['R'])+1)