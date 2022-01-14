s = input()
temp = ['U', 'C', 'P', 'C']
check = True

for i in range(4):
    if temp[i] in s:
        check = True
        idx = s.index(temp[i])
        s = s[idx+1:]
    else:
        check = False
        break

if check == True:
    print('I love UCPC')
else:
    print('I hate UCPC')