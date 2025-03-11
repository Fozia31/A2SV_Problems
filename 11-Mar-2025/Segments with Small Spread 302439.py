# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
min_dq = deque()
max_dq = deque()
n , k = map(int,input().split())
a = list(map(int , input().split()))
left = 0
count = 0
for r in range(n):
    
    while min_dq and a[min_dq[-1]] >= a[r]:
        min_dq.pop()
    min_dq.append(r)
    
    while max_dq and a[max_dq[-1]] <= a[r]:
        max_dq.pop()
    max_dq.append(r)
    
    while a[max_dq[0]] - a[min_dq[0]] > k :
        left += 1
        if max_dq[0] < left:
            max_dq.popleft()
        if min_dq[0] < left:
            min_dq.popleft()
    
    count +=( r - left + 1)
        
print(count)

    