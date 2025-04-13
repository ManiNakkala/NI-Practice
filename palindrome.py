num = int(input())
def palindrome(num):
    org = num
    rev = 0
    while num > 0:
        rem = rem % 10
        rev = rev * 10 + rem
        num = num // 10
    return org == rev 
print(palindrome(num))