# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n =int(input())
s = input()
output = ""
output = ""
count = 0
i = 1
while count < len(s):
    output += s[count]
    count += i
    i += 1
print(output)