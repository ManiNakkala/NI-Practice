def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] >list[j+1]:
                list[j],list[j+1] == list[j+1],list[j]
    return list
list=[1,3,6,8,0,2,4,5]
print(bubble_sort(list))