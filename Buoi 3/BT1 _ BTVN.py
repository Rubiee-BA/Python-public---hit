# Bài tập 
s = input("Nhập chuỗi: ")
# 1. Đảo ngược chuỗi 
dao = ""
for i in range(len(s) - 1, -1, -1):
    dao += s[i]
print("Chuỗi đảo ngược:", dao)

# 2. Sắp xếp các ký tự theo thứ tự tăng dần
sap_xep = "".join(sorted(s))
print("Chuỗi sau khi sắp xếp:", sap_xep)

# 3. Kiểm tra chuỗi đối xứng
if s == dao:
    print("Đây là chuỗi đối xứng.")
else:
    print("Đây không phải là chuỗi đối xứng.")

# 4. Tìm ký tự xuất hiện nhiều nhất
tap_ky_tu = set(s)
max_dem = 0
for ky_tu in tap_ky_tu:
    if s.count(ky_tu) > max_dem:
        max_dem = s.count(ky_tu)
# Lấy tất cả ký tự có số lần xuất hiện lớn nhất
ds = []
for ky_tu in tap_ky_tu:
    if s.count(ky_tu) == max_dem:
        ds.append(ky_tu)
ds.sort()
print("Ký tự xuất hiện nhiều nhất:")
for ky_tu in ds:
    print(ky_tu, end=" ")
print()
print("Số lần xuất hiện:", max_dem)

# 5. Kiểm tra có đủ 5 nguyên âm
s_thuong = s.lower()
if ("a" in s_thuong and
    "e" in s_thuong and
    "i" in s_thuong and
    "o" in s_thuong and
    "u" in s_thuong):
    print("Chuỗi chứa đầy đủ 5 nguyên âm tiếng Anh.")
else:
    print("Chuỗi không chứa đầy đủ 5 nguyên âm tiếng Anh.")