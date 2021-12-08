# this program checsk valid position of bishop
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a-c) == abs(b-d):  # checks diagonal movement
    print("Yes")
else:
    print("No")
