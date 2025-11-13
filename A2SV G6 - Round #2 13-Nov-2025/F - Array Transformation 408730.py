# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = list(Counter(a).values())
    freq.sort()
    prefix = [0]
    for f in freq:
        prefix.append(prefix[-1] + f)
    res = n
    for i, f in enumerate(freq):
        left = prefix[i]
        right = prefix[-1] - prefix[i+1]
        count_greater = len(freq) - i - 1
        res = min(res, left + right - count_greater * f)
    print(res)
