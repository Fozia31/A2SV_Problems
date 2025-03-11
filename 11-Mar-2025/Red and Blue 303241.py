# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for i in range(t):
    m = int(input())
    a1 = list(map(int , input().split()))
    n = int(input())
    a2 = list(map(int , input().split()))
    pre_1 = [0]
    pre_2 = [0]
    prev = 0
    for i in range(m):
        prev += a1[i]
        pre_1.append(prev)
    prev = 0
    for i in range(n ):
        prev += a2[i]
        pre_2.append(prev)
    print(max(pre_1) + max(pre_2))

        
