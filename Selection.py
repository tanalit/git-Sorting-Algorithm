import time
import apToList as ap

start_time = time.time()  # เริ่มจับเวลา
def select(my_array):
    n = len(my_array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if my_array[j] > my_array[min_index]:
                min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

    return my_array


if __name__ == "__main__":
    data = ap.apTolist()
    my_array =[]
    for i in range(len(data)):
        my_array.append(select(data[i]))

    print("Sorted array:", my_array)


end_time = time.time()  # จับเวลาสิ้นสุด
elapsed_time = end_time - start_time  # ระยะเวลาที่ใช้

print(f"ใช้เวลา: {elapsed_time:.4f} วินาที")