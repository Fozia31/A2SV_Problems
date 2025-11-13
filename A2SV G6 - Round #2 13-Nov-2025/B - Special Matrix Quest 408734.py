# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

good_sum = 0
mid = n // 2 

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1 or i == mid or j == mid:
            good_sum += matrix[i][j]

print(good_sum)
