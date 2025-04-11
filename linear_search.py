def linear_search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            return i 
list = [1,3,5,7,9,10,22]
n = 9
print(linear_search(list,n))