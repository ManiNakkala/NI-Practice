s = input()
length = 0
for _ in s:
    length += 1
is_pal = True
for i in range(length//2):
    if s[i] != s[length-i-1]:
        is_pal = False
        break
    
if(pal):
    print("Palindrome")
else:
    print("Not")