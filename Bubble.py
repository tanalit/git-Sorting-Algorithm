import time
import apToList as ap

start_time = time.time()  # เริ่มจับเวลา

def bubble(my_array):
    n = len(my_array)
    for i in range(n-1):
        for j in range(n-i-1):
            if my_array[j] < my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

    return my_array

if __name__ == "__main__":
    data = ap.apTolist()
    my_array =[]
    for i in range(len(data)):
        my_array.append(bubble(data[i]))

    print("Sorted array:", my_array)

end_time = time.time()  # จับเวลาสิ้นสุด
elapsed_time = end_time - start_time  # ระยะเวลาที่ใช้

print(f"ใช้เวลา: {elapsed_time:.4f} วินาที")