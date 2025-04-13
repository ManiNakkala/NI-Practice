list = [1,2,4,7,9,3]
def largest(list):
    largest = list[0]
    for num in list:
        if num > largest:
            largest = num
    return largest
print(largest(list))