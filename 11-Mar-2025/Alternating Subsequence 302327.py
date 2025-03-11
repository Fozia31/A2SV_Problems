# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

n = int(input())
for i in range(n):
    m = int(input())
    a = list(map(int , input().split()))
    left , right= 0 , 0
    max_val , max_sum = 0,0
    while left < m:
        
        max_val = a[left]
        flag = a[left] > 0
        
        while right < m and (a[right] > 0) == flag:
            max_val = max(max_val , a[right])
            right += 1
        
        max_sum += max_val
        left = right
    print(max_sum)
         
        