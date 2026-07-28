# Bài 2
chuoi = input("Nhập danh sách sản phẩm: ")
tim = input("Nhập sản phẩm cần kiểm tra: ")
# Chuẩn hóa danh sách sản phẩm
ds = []
for sp in chuoi.split(","):
    sp = sp.strip()          # Xóa khoảng trắng thừa
    sp = sp.title()          # Viết hoa chữ cái đầu mỗi từ
    ds.append(sp)
# Chuẩn hóa sản phẩm cần tìm
tim = tim.strip().title()
# In danh sách
print("Danh sách sản phẩm:")
print(ds)
# Tổng số sản phẩm
print("\nTổng số sản phẩm đã mua:", len(ds))
# Sản phẩm ở vị trí giữa (nếu số phần tử lẻ)
if len(ds) % 2 == 1:
    print("\nSản phẩm ở vị trí giữa:", ds[len(ds) // 2])
# Tìm sản phẩm xuất hiện nhiều nhất
max_dem = 0
for sp in set(ds):
    if ds.count(sp) > max_dem:
        max_dem = ds.count(sp)
nhieu_nhat = []
for sp in set(ds):
    if ds.count(sp) == max_dem:
        nhieu_nhat.append(sp)
nhieu_nhat.sort()
print("\nCác sản phẩm được mua nhiều nhất:")
for sp in nhieu_nhat:
    print(f"{sp}: {max_dem} lần")
# Kiểm tra sản phẩm cần tìm
if tim in ds:
    print(f"\n{tim} đã được mua {ds.count(tim)} lần.")
else:
    print(f"\n{tim} chưa được mua.")
# Thêm "Bánh Nabati" vào đầu danh sách
ds.insert(0, "Bánh Nabati")
# Xóa lần xuất hiện đầu tiên của "Sữa" nếu có
if "Sữa" in ds:
    ds.remove("Sữa")
# In danh sách sau khi cập nhật
print("\nDanh sách sau khi cập nhật:")
print(ds)