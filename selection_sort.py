def selection_sort(list):
    for i in range(0,len(list)-1):
        curr_min = i
        for j in range(i+1,len(list)):
            if list[j] < list[curr_min]:
                curr_min = j
        list[i],list[curr_min] = list[curr_min],list[i]
    return list
list=[1,3,5,9,2,3]
print(selection_sort(list))
