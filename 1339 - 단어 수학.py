n = int(input())
word = []
for _ in range(n):
    word.append(input())

alphabet = [0] * 26

for w in word:
    for i, alp in enumerate(w):
        n = len(w) - i - 1
        alphabet[ord(alp) - ord('A')] += 10 ** n
alphabet.sort(reverse=True)

total = 0
a = 9
for i in range(0, 9):
    total += alphabet[i] * a
    a -= 1

print(total)
