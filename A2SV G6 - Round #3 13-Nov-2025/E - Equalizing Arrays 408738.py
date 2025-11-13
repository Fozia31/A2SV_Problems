# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

i = j = 0
sumA = sumB = 0
length = 0

while i < n or j < m:
    if sumA == sumB:
        if sumA != 0:
            length += 1
            sumA = sumB = 0
        if i < n:
            sumA += A[i]
            i += 1
        if j < m:
            sumB += B[j]
            j += 1
    elif sumA < sumB:
        if i < n:
            sumA += A[i]
            i += 1
        else:
            break
    else:
        if j < m:
            sumB += B[j]
            j += 1
        else:
            break

if sumA == sumB:
    if sumA != 0:
        length += 1
    print(length)
else:
    print(-1)
