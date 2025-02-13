# # 1. Nhập vào một số nguyên, kiểm tra xem số đó là số âm, dương hay bằng 0 và in kết quả tương ứng.

# number = int(input("nhap so nguyen: "))
# if number > 0:
#     print("so duong")
# elif number < 0:
#     print("so am")

# # 2. Nhập vào tuổi của một người, nếu người đó từ 18 tuổi trở lên thì in "Adult", ngược lại in "Minor".

# age = int(input("nhap tuoi "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

# # 3. Nhập vào một số thực, chuyển nó thành số nguyên và in kết quả.
# number = float(input("nhap so thuc: "))
# print(int(number))

# # 4. Nhập vào một số nguyên từ người dùng, nếu không phải số nguyên thì in ra thông báo lỗi "Please enter a valid number."
# number = input("nhap so nguyen: ")
# if number.isdigit():
#     print(int(number))
# else:
#     print("Please enter a valid number.")
    
# # 5. Viết hàm kiểm tra xem một số có phải là số nguyên tố hay không.

# number = int(input("nhao 1 so "))
# def ktra_snt(number):
#     if number < 2:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
# if ktra_snt(number):
#     print("la snt")
# else:
#     print("khong la snt")
    
# # 6. Khai báo một danh sách và sử dụng hàm len() để in ra số phần tử trong danh sách.
# a = [1, 2, 3, 4, 5]
# print(len(a))

# # 7. Khai báo một danh sách số và sử dụng hàm max() để in ra giá trị lớn nhất trong danh sách.

# b = [1,6,2,7,2,9,8]
# print(max(b))

# # 8. Tạo một danh sách các số, sau đó thêm một số mới vào cuối danh sách và in kết quả.
# c = [4,6,8,3,2,7]
# c.append(9)
# print(c)
# # 9. Tạo một danh sách chứa tên của 5 người, in ra tên thứ ba trong danh sách.
# listt = ["pham", "minh", "tuan", "dep", "trai"]
# print(listt[2])

# # 10. Tạo một dictionary chứa thông tin tên và tuổi của một người, in ra tên và tuổi của người đó.
# dict = {"name": "tuan", "age": 20}
# print(dict["name"], dict["age"])


# # 11. Tạo một dictionary chứa tên các học sinh và điểm của họ, in ra điểm của một học sinh cụ thể.
# dictti = {"pham": 10, "minh": 9, "tuan": 8}
# print(dictti["pham"])


# # 12. Dùng vòng lặp for để in ra các số từ 1 đến 10.
# for i in range(1, 11):
#     print(i)

# # 13. Dùng vòng lặp while để in ra các số chẵn từ 0 đến 20.
# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1



# Viết một chương trình Python để đếm số lần xuất hiện của từng từ trong một đoạn văn bản
# 1. Loại bỏ dấu câu (ví dụ: .,!? không được tính là một phần của từ).
# 2. Không phân biệt chữ hoa, chữ thường ("Python" và "python" được coi là một).
# 3. Sắp xếp kết quả theo số lần xuất hiện giảm dần.
# 4. Hiển thị n từ xuất hiện nhiều nhất, với n là số do người dùng nhập.


a = [" => Viet 1 chuong trinh python. de dem ? so lan xuat hien. Cua tung tu? trong 1 van ban ?? ? dem so lan xuat hien...!!!!"]
b = a[0].split()
c = []
for i in b:
    if i.isalpha():
        c.append(i.lower())
dsach = {}
for i in c:
    if i in dsach:
        dsach[i] += 1
    else:
        dsach[i] = 1
        
# print(dsach)

dsach = sorted(dsach.items(), key=lambda x: x[1], reverse=True)
print(dsach)

n = int(input("nhap n: "))
for i in range(n):
    print(dsach[i])
                



            