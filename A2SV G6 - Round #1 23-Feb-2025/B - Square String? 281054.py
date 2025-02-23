# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

N=int(input())
for i in range(N):
    strr=input()
    if len(strr)==1 or len(strr)%2!=0:
        print("NO")
    else:
        x=len(strr)
        x=x//2
        if strr[:x]==strr[x:]:
            print("YES")
        else:
            print("NO")
       