# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

n = int(input())
m = input()
stack = []
ans = n
for i in range(n):
    if stack and ((stack[-1] == "0" and m[i] == "1" ) or (m[i] == "0" and stack[-1] == "1")) :
        stack.pop()
        ans -= 2
    else:
        stack.append(m[i])
print(ans)