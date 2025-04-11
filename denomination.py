n = 560
count_100 = n // 100
remainder = n % 100 
count_50 = remainder // 50
remainder = n % 50 
count_10 = remainder // 10 
remainder = n % 10 
print(count_100,count_50,count_10)