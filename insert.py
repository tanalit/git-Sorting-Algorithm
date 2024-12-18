
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

def bubble(my_array):
    n = len(my_array)
    for i in range(1,n):
        insert_index = i
        current_value = my_array.pop(i)
        for j in range(i-1, -1, -1):
            if my_array[j] > current_value:
                insert_index = j
        my_array.insert(insert_index, current_value)
    return my_array

my_array = []
data = []

for i in range(len(arr)):
    my_array.append(spell(arr[i]))

for i in range(len(my_array)):
    data.append(bubble(my_array))

print(data)