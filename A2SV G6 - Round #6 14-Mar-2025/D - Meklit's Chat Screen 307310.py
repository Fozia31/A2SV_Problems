# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
n , k = map(int , input().split())
a = list(map(int , input().split()))
que= deque()
s =set()
for i in range(n):
    if que and a[i] in s :
        continue
    elif len(que) < k: 
        s.add(a[i])
        que.append(a[i])
    else:
        que.append(a[i])
        s.add(a[i])
        t = que.popleft()
        s.discard(t)
print(len(que))
res = []
for j in range(len(que) - 1 , -1 , -1 ):
    res.append(que[j])
print(*(res))