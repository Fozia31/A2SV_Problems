# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

m , n = map(int , input().split())
a = list(map(int , input().split()))
ans = [] 
for i in range(1 ,len(a)):
    ans.append(a[i] - a[i - 1])
ans.sort(reverse= True)
sum_ = sum(ans)  - sum(ans[:n-1])

print(sum_)
     