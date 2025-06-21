# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

import math

q = int(input())
for _ in range(q):
a = int(input())
if (a & (a + 1)) == 0:
print(a)
else:
k = a.bit_length()
print((1 << k) - 1)

