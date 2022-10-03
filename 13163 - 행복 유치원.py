n, k = map(int, input().split())
people = list(map(int, input().split()))
diff = sorted([people[i+1]-people[i] for i in range(0, n-1)], reverse=True)

answer = diff[k-1:]
print(sum(answer))