# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

valid = True

for i in range(n):
    for j in range(m):
        if field[i][j] == '*':
            continue
        count = 0
        for k in range(8):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == '*':
                count += 1
        if field[i][j] == '.':
            if count != 0:
                valid = False
                break
        else:
            if int(field[i][j]) != count:
                valid = False
                break
    if not valid:
        break

print("YES" if valid else "NO")
