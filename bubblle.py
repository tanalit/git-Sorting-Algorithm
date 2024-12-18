
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
    for i in range(n-1):
        for j in range(n-i-1):
            if my_array[j] >= my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    return my_array

my_array = []
data = []

for i in range(len(arr)):
    my_array.append(spell(arr[i]))

for i in range(len(my_array)):
    data.append(bubble(my_array))

print(data)