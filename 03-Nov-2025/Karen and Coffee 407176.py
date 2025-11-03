# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q = map(int, input().split())

rep = [0]*200002
for _ in range(n):
    l, r = map(int, input().split())
    rep[l] += 1
    if r + 1 <= 200000:
        rep[r + 1] -= 1
for i in range(1, 200001):
    rep[i] += rep[i - 1]

good = [0]*200002
for i in range(1, 200001):
    if rep[i] >= k:
        good[i] = 1
    else:
        good[i] = 0
pref = [0]*200002
pref[0] = 0

for t in range(1 , 200001):
    pref[t] = pref[t-1] + good[t]
for _ in range(q):
    a ,b = map(int,input().split())
    
    ans = pref[b] - pref[a-1]

    print(ans)