n, m = map(int, input().split())
card_list = list(map(int, input().split()))

for _ in range(m):
    card_list.sort()
    temp = card_list[0] + card_list[1]
    card_list[0] = temp
    card_list[1] = temp

print(sum(card_list))
