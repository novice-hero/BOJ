import sys
input = sys.stdin.readline

s, e, q = input().split()

def convertTime(s):
  hour, minute = s.split(":")
  return int(hour)*60+int(minute)

s = convertTime(s)
e = convertTime(e)
q = convertTime(q)
people = set()
answer = 0

while True:
  chat = input()
  if chat=="":
    break

  time, name = chat.split()
  time = convertTime(time)
  if time <= s:
    people.add(name)
  if e<=time<=q and name in people:
    people.remove(name)
    answer+=1

print(answer)