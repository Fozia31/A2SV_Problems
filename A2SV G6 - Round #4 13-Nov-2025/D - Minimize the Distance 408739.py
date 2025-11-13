# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
a = list(map(int, input().split()))

a.sort()  

if n % 2 != 0:
    print(a[n // 2]) 
else:
    print(a[n // 2 - 1])  
