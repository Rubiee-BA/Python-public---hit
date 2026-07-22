# Bài 1
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
# Kiểm tra số ngày trong tháng
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif thang in [4, 6, 9, 11]:
    print(30)
elif thang == 2:
    # Kiểm tra năm nhuận
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        print(29)
    else:
        print(28)
else:
    print("Tháng không hợp lệ!")

# Bài 2: Cung hoàng đạo
ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))

# Kiểm tra tính hợp lệ cơ bản
if thang < 1 or thang > 12 or ngay < 1 or ngay > 31:
    print("Ngày hoặc tháng không hợp lệ")
elif (thang == 4 or thang == 6 or thang == 9 or thang == 11) and ngay > 30:
    print("Ngày hoặc tháng không hợp lệ")
elif thang == 2 and ngay > 29:
    print("Ngày hoặc tháng không hợp lệ")
else:
    # Xác định cung hoàng đạo
    if (thang == 3 and ngay >= 21) or (thang == 4 and ngay <= 19):
        print("Bạch Dương")
    elif (thang == 4 and ngay >= 20) or (thang == 5 and ngay <= 20):
        print("Kim Ngưu")
    elif (thang == 5 and ngay >= 21) or (thang == 6 and ngay <= 20):
        print("Song Tử")
    elif (thang == 6 and ngay >= 21) or (thang == 7 and ngay <= 22):
        print("Cự Giải")
    elif (thang == 7 and ngay >= 23) or (thang == 8 and ngay <= 22):
        print("Sư Tử")
    elif (thang == 8 and ngay >= 23) or (thang == 9 and ngay <= 22):
        print("Xử Nữ")
    elif (thang == 9 and ngay >= 23) or (thang == 10 and ngay <= 22):
        print("Thiên Bình")
    elif (thang == 10 and ngay >= 23) or (thang == 11 and ngay <= 21):
        print("Bọ Cạp")
    elif (thang == 11 and ngay >= 22) or (thang == 12 and ngay <= 21):
        print("Nhân Mã")
    elif (thang == 12 and ngay >= 22) or (thang == 1 and ngay <= 19):
        print("Ma Kết")
    elif (thang == 1 and ngay >= 20) or (thang == 2 and ngay <= 18):
        print("Bảo Bình")
    elif (thang == 2 and ngay >= 19) or (thang == 3 and ngay <= 20):
        print("Song Ngư")
    else:
        print("Ngày hoặc tháng không hợp lệ")
# Bài 3
n = int(input("Nhập số nguyên: "))
# Lấy giá trị tuyệt đối để đếm và tính tổng chữ số
temp = abs(n)
# Đếm số chữ số
so_chu_so = len(str(temp))
# Tính tổng các chữ số
tong = 0
while temp > 0:
    tong += temp % 10
    temp //= 10
# Trường hợp n = 0
if n == 0:
    tong = 0
# Kiểm tra số nguyên tố
if n < 2:
    la_so_nguyen_to = False
else:
    la_so_nguyen_to = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_so_nguyen_to = False
            break
# In kết quả
print("Số chữ số:", so_chu_so)
print("Tổng chữ số:", tong)
if la_so_nguyen_to:
    print(n, "là số nguyên tố.")
else:
    print(n, "không phải là số nguyên tố.")
