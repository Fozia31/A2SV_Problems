# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

n , m = map(int, input().split())

min_move = (n + 1)//2

if min_move%m == 0:
    ans = min_move
else:
    ans = ((min_move + m -1)//m)*m


if ans > n:
    print(-1)
else:
    print(ans)