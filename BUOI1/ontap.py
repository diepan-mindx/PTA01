# Bien + input/ print ----------------------------------------------------
# khởi tạo biến
# a = 10  # tạo biến a + gán giá trị 10 cho a

# input - nhập dữ liệu
# b = input("Nhap ten: ")
# print - xuất dữ liệu
# print("Ten ban la: ", b)

# Kiểu dữ liệu ------------------------------------------------------
# number (integer - số nguyên + float - số thực)
# x = 10
# y = 15.5
# print(type(x))
# print(type(y))
# sum = x + y  # float > int => float
# print(type(sum))
# # Chuyển đổi kiểu dữ liệu
# x = int(15.5) # đổi từ float => int
# y = float(10) # đổi từ int => float
# print(x) # 15
# print(y) # 10.0

# String ------------------------------------------------
# s = "Xin chao ban "
# m = "Au Ngoc Diep"
# z = "123"
# print(type(s))  # class str
# print(s + m)
# print(z*2) # phép nhân => gấp 2 str => '123123'
# # Hàm hỗ trợ
# ch = 'b'
# print(ch in m) # True - False (boolean)
# # find() - nếu không tìm thấy => -1
# print(s.find('-1')) # trả về index
# # replace()
# s = s.replace(' ', ',')
# print(s)
# # split - cắt chuỗi => danh sách
# my_s = m.split(" ")
# print(my_s)

# Boolean + logical + if - else -----------------------------------------
# a = 12 > 3
# b = 15 < 6
# c = 20 <= 15 + 5
# d = 20 != 0
# m = a and (b or c) and not (c or d)
# print(m)  # false
# # if re nhanh
# if m:
#     print("m la bieu thuc dung")
# elif m and not b:
#     print("m and not b la bieu thuc dung")
# else:
#     print("Tat ca bieu thuc deu sai")

# if a and c:
#     print('A')
# elif b or not d:
#     print('B')
# else:
#     print('C')

# for - while ---------------------------------------------
# for - vòng lặp hữu hạn
# sum = 0
# # range (start, stop (trừ 1), step)
# for i in range(1, 6, 2):
#     sum += i

# if sum > 10:
#     print("Sum > 10")
# else:
#     print("Sum <= 10")

# while - vòng lặp vô hạn
# sum = 0
# while sum <= 10:
#     sum += 1
#     print(sum)

# list -------------------------------------------
# khai bao danh sach
# lis = [12, 2.5, 250, "abc", "edf"]
# # remove(gia tri phan tu) - xoa phan tu
# lis.remove(250)
# print(lis)
# # append(gia tri moi) - chen phan tu moi vao phia cuoi cua list
# lis.append(int('36'))
# print(lis)
# # clear() - xoa het phan tu trong lis
# lis.clear()
# print(lis)
# # insert(index, gia tri moi) - them phan tu tai vi tri mong muon
# lis.insert(3, "b")
# print(lis)


# Function (hàm) -----------------------------------------
# Hàm có trả về giá trị cụ thể
# Đề: nhập vào list có n số nguyên, xóa số không chia hết cho 2 => in lại list
# def even_list(lis):  # lis: param => tham số truyền vào
#     # chay vong for => kiem tra tung phan tu
#     for i in lis:
#         if i % 2 != 0:
#             # xoa phan tu le
#             lis.remove(i)
#     return lis


# lis = [12, 45, 25, 47, 36, 10, 45]
# print(even_list(lis))  # lis: argument => đối số

# Hàm không trả về giá trị cụ thể
# Đề: hàm truyền vào tên 1 người, in ra "Hello bạn: " + tên người đó
def hello (name):
    print("Hello ban: " + name)

name = input("Your name ")
hello(name)

# Đề: viết hàm trả về danh sách số nguyên chia hết cho 3
# tham số: bắt đầu + kết thúc => chạy vòng for 