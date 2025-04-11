def binary_search(list,n):
    left,right = 0,len(list) - 1
    while left <= right:
        mid = left + right // 2
        if list[mid] == n:
            return mid 
        elif list[mid] < n:
            mid = mid + 1
        else:
            mid = mid - 1
    return -1 
list = [1,2,3,4,5,6,7]
n = 5
print(binary_search(list,n))
