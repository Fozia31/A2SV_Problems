# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

n , m, a = map(int , input().split())
remining_width =(n + a - 1) // a
remining_height = (m + a - 1) // a
print(remining_height*remining_width)