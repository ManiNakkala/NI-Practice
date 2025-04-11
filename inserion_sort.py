def inserton_sort(list):
    for i in range(1,len(list)):
        key = list[i]
        j = i - 1
        while j>=0 and key<list[j]:
            list[j+1] = list[j]
            j = j - 1
            list[j+1] = key
    return list
list=[1,4,7,9,2,3]
print(inserion_sort(list))