# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    import math
    ans = math.inf

    for c in set(s):
        left = 0
        right = n - 1
        cnt = 0
        possible = True

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] == c:
                cnt += 1
                left += 1
            elif s[right] == c:
                cnt += 1
                right -= 1
            else:
                possible = False
                break

        if possible:
            ans = min(ans, cnt)

    if ans == math.inf:
        print(-1)
    else:
        print(ans)
