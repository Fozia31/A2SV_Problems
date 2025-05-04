# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n=int(input())
a=list(map(int,input().split()))
even_checker = False
odd_checker = False
for x in a:
    if x%2 == 1:
        odd_checker =True
    else:
        even_checker = True
        
if even_checker and odd_checker:
    print(*(sorted(a)))
else:
    print(*a)
        
        
