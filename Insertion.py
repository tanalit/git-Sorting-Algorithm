import time
import apToList as ap

start_time = time.time()  # เริ่มจับเวลา
def insertion(my_array):
    n = len(my_array)
    for i in range(1,n):
        insert_index = i
        current_value = my_array.pop(i)
        for j in range(i-1, -1, -1):
            if my_array[j] > current_value:
                insert_index = j
    my_array.insert(insert_index, current_value)

    return my_array

if __name__ == "__main__":
    data = ap.apTolist()
    my_array =[]
    for i in range(len(data)):
        my_array.append(insertion(data[i]))

    print("Sorted array:", my_array)


end_time = time.time()  # จับเวลาสิ้นสุด
elapsed_time = end_time - start_time  # ระยะเวลาที่ใช้

print(f"ใช้เวลา: {elapsed_time:.4f} วินาที")