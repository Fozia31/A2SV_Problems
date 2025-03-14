# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

n , m = map(int,(input().split()))
if m/n > m//n :
    print((m//n) + 1)
else:
    print(m//n)