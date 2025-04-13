num = int(input())
temp = num
length = len(str(num))
sum = 0
while temp > 0:
    rem = temp % 10
    sum = sum + (rem ** length)
    num = num  // 10
if num == sum:
    print("Armstrong")
else:
    print("Not Armstrong")