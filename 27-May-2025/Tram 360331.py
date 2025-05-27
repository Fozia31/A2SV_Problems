# Problem: Tram - https://codeforces.com/problemset/problem/116/A

n = int(input())
sum = 0
current = 0
for _ in range(n):
    a , b = map(int,input().split())
    current += b
    current -= a
    sum = max(sum, current)
    
print(sum)