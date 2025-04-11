s = input()
result = ""
for i in range(len(s)):
    if s[i].islower():
        result = result + s[i].upper()
    else:
        result = result + s[i].lower()
print(result)