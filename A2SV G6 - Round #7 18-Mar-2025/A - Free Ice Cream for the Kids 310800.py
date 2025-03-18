# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

n  , m = map(int , input().split())
left = 0
rec = m
for i in range(n) :
    x , y = map(str , input().split())
    if x == "-":
        if rec >= int(y):
            rec -= int(y)
        else:
            left += 1
    elif x == "+":
        rec +=int( y)
print(*([rec , left]))
        