# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

left = 0
max_left, max_right = 0, 0
freq = defaultdict(int)

for right in range(n):
    freq[a[right]] += 1  

    while len(freq) > m:  
        freq[a[left]] -= 1  
        if freq[a[left]] == 0:
            del freq[a[left]]  
        left += 1  

    if right - left > max_right - max_left:
        max_left, max_right = left, right

print(max_left + 1, max_right + 1)
