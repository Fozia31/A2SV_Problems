# Problem: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

n = int(input())

for _ in range(n):
    a , b = map(int , input().split())
    if a == b:
        print(a//2)
    else:
        team = (a + b)//4
        if a < b:
            if team > a:
                print(a)
            else:
                print(team)
        else:
            if team > b:
                print(b)
            else:
                print(team)

