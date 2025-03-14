# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque

x = int(input())
for i in range(x):
   m = int(input())
   a = list(map(int,input().split()))
   que = deque()
   que.append(a[0])
   for i in range(1 , m):

       if a[i] < que[0]:
           que.appendleft(a[i])
       else:
           que.append(a[i])
   print(*(que))



