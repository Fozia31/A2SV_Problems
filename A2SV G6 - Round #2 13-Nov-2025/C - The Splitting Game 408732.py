# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter


n = int(input())

for _ in range(n):
    t = int(input())
    s = input()

    counter = Counter(s)
    counter_left = {}
    res = 0
    for st in s:
        counter[st] -= 1
        if st not in counter_left:
            counter_left[st] = 1
        else:
            counter_left[st] += 1
        if counter[st] == 0:
            del counter[st]
        res = max(res, len(counter_left) + len(counter))

    print(res)
