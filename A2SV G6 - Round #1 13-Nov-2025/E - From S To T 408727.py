# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

def solve():
    s = input()
    t = input()
    p = input()

    i, j = 0, 0  
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1  

    if i != len(s):
        print("NO")
        return

    freq_t = {}
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1

    freq_s_p = {}
    for char in s + p:
        freq_s_p[char] = freq_s_p.get(char, 0) + 1

    for char, required_count in freq_t.items():
        available_count = freq_s_p.get(char, 0)
        if required_count > available_count:
            print("NO")
            return

    print("YES")


q = int(input())  
for _ in range(q):
    solve()
