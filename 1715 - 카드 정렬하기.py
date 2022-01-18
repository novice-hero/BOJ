import heapq

n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

answer = 0
while len(card) != 1:
    n1 = heapq.heappop(card)
    n2 = heapq.heappop(card)
    sum1 = n1 + n2
    answer += sum1
    heapq.heappush(card, sum1)

print(answer)