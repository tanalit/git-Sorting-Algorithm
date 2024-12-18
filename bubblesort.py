def read_and_clean_file(input_file, output_file):
    """อ่านไฟล์ input ทำความสะอาดข้อมูลและเขียนผลลัพธ์ลงไฟล์ output"""
    with open(input_file, 'r', encoding='utf-8') as f:
        alist = list(f)
        aa = []
        for line in alist:
            a = line[64:]  # ตัดข้อมูลส่วนที่ไม่ต้องการ
            aa.append(a)

    # ทำความสะอาดข้อมูล
    Newaa = []
    for line in aa:
        na = line.replace("(", "").replace(")", "").replace("'", "").replace(",", "").replace(";", "")
        Newaa.append(na.strip())  # เอา \n ออก

    # เขียนข้อมูลที่ทำความสะอาดแล้วลงไฟล์ output
    with open(output_file, 'w', encoding='utf-8') as f:
        for output in Newaa:
            f.write(output + '\n')

    return Newaa  # คืนค่าข้อมูลเป็น list

def bubble_sort_desc(arr):
    """ฟังก์ชันสำหรับเรียงลำดับข้อมูลใน array โดยใช้ Bubble Sort"""
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Import ฟังก์ชัน
# from read_and_clean_file
# import read_and_clean_file
# from bubble_sort 
# import bubble_sort

# ---------------- Main Program ----------------
# กำหนดไฟล์ Input และ Output
input_file = 'Amphoe.txt'      # ไฟล์ข้อมูลต้นฉบับ
output_file = 'Oamphoe.txt'    # ไฟล์ผลลัพธ์ที่ทำความสะอาดแล้ว

# อ่านไฟล์และทำความสะอาดข้อมูล
cleaned_data = read_and_clean_file(input_file, output_file)

# แปลงข้อมูลเป็นตัวเลขสำหรับเรียงลำดับ (ถ้าข้อมูลเป็นตัวเลข)
numeric_data = [int(x) for x in cleaned_data if x.isdigit()]

# เรียงลำดับข้อมูลจากมากไปน้อย
sorted_data = bubble_sort_desc(numeric_data)

# แสดงผลลัพธ์ที่เรียงลำดับแล้ว
print("Sorted Data (Descending):", sorted_data)

# เขียนข้อมูลที่เรียงลำดับแล้วกลับลงไฟล์ Oamphoe.txt
with open(output_file, 'a', encoding='utf-8') as f:  # ใช้โหมด 'a' แทน 'w'
    for item in sorted_data:
        f.write(str(item) + '\n')

print(f"Sorted data has been written to {output_file}")