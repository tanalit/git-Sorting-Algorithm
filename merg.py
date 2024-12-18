
arr = []
with open('Oamphoe.txt','r',encoding='utf-8') as op:
    for i in op:
        n1,n2,n3,n4 = i.split()
        arr.append(n1)

def spell(arr):
    my_array = []
    for j in arr:
        my_array.append(int(j))
    return my_array


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return my_array

my_array = []
data = []

for i in range(len(arr)):
    my_array.append(spell(arr[i]))

for i in range(len(my_array)):
    data.append(merge(my_array))

print(data)