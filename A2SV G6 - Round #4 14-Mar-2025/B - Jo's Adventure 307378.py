# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
arr = list(map(int, input().split()))
front_prefix = [0] * n
back_prefix = [0] * n
for i in range(1, n):
    front_prefix[i] = front_prefix[i - 1] + max(0, arr[i - 1] - arr[i])
        
for i in range(n - 2, -1, -1):
    back_prefix[i] = back_prefix[i + 1] + max(0, arr[i + 1] - arr[i])
    
for _ in range(m):
    a, b = map(int, input().split())
    
    if b > a:
        print(front_prefix[b - 1] - front_prefix[a - 1])
    else:
        print(back_prefix[b - 1] - back_prefix[a - 1])
 