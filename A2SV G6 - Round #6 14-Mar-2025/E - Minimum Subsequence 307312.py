# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

ts = int(input())
for _ in range(ts):
    n = int(input())
    s = input()
    sq = 1
    sequences = {"0": [], "1":[]}
    stack = []
    ans = [0] * n
    for i in range(n):
        if stack:
            if stack[-1] == s[i]:
                sequences[stack[-1]].append(ans[i-1])
                if s[i] == "0":
                    if sequences["1"]:
                        ans[i] = sequences["1"].pop()
                    else:
                        sq += 1
                        ans[i] = sq
                elif sequences["0"]:
                    ans[i] = sequences["0"].pop()
                else:
                    sq += 1
                    ans[i] = sq
            else:
                ans[i] = ans[i-1]
        else:
            ans[i] = sq
        stack.append(s[i])
    print(sq)
    print(*ans)
                