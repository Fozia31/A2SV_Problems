# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

n = int(input())
for i in range(n):
    m = int(input())
    arr = list(map(int , input().split()))
    b = [0]*m
    if arr[0] == 1:
        b[0] = 2
    else:
        b[0] = 1
        
    for i in range(1 , m):
        if (b[i -1] + 1) == arr[i]:
            b[i] = b[i - 1] + 2
        else:
            b[i] = b[i - 1] + 1
            
    print(b[-1])
    