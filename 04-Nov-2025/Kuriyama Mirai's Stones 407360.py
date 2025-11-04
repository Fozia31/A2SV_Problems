# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
lst1 = list(map(int, input().split()))
t = int(input())
lst2 = sorted(lst1)
pre1 = [0]*(n+1)
pre2 = [0]*(n+1)

for i in range(1 , n+1):
    pre1[i] = pre1[i-1] + lst1[i-1]

for i in range(1 , n+1):
    pre2[i] = pre2[i-1] + lst2[i-1]


for _ in range(t):
    type , l , r = map(int , input().split())
    if type == 1:
        print(pre1[r] - pre1[l-1])
    else:
        print(pre2[r] - pre2[l-1])
