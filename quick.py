
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


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)
    return my_array

my_array = []
data = []

for i in range(len(arr)):
    my_array.append(spell(arr[i]))

for i in range(len(my_array)):
    data.append(quicksort(my_array))

print(data)