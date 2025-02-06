# 1. Khai báo biến và in giá trị
x = 10
y = 5
print("Giá trị của x:", x)
print("Giá trị của y:", y)

# 2. Cộng 2 số
a = 8
b = 12
sum_result = a + b
print("Tổng của a và b là:", sum_result)

# 3. So sánh 2 số
num1 = 10
num2 = 15
if num1 > num2:
    print("num1 lớn hơn num2")
elif num1 < num2:
    print("num1 nhỏ hơn num2")
else:
    print("num1 bằng num2")

# 4. Sử dụng kiểu float
float_num = 3.14
print("Giá trị kiểu float:", float_num)

# 5. Kiểm tra số chẵn hay lẻ
number = 17
if number % 2 == 0:
    print(f"{number} là số chẵn")
else:
    print(f"{number} là số lẻ")

# 6. Tính diện tích hình vuông
side_length = 4
area = side_length ** 2
print("Diện tích hình vuông là:", area)

# 7. Sử dụng chuỗi (string)
name = "Tuan"
print("Chào bạn:", name)

# 8. Nhập và tính tổng
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
total = num1 + num2
print("Tổng của hai số là:", total)

# 9. Chuyển đổi kiểu dữ liệu
str_num = "123"
int_num = int(str_num)  # Chuyển đổi chuỗi thành số nguyên
print("Kiểu dữ liệu sau khi chuyển đổi:", type(int_num))

# 10. Kiểm tra số âm hay dương
num = -7
if num > 0:
    print(f"{num} là số dương")
elif num < 0:
    print(f"{num} là số âm")
else:
    print("Đây là số 0")
