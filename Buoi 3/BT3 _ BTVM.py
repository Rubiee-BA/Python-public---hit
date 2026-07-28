# Bài 3
a = input("Nhập sở thích của Người A: ")
b = input("Nhập sở thích của Người B: ")
set_a = set()
for so_thich in a.split(","):
    so_thich = so_thich.strip().title()
    if so_thich != "":
        set_a.add(so_thich)
set_b = set()
for so_thich in b.split(","):
    so_thich = so_thich.strip().title()
    if so_thich != "":
        set_b.add(so_thich)
# In sở thích của từng người
print("Các sở thích của Người A:")
print(set_a)
print("\nCác sở thích của Người B:")
print(set_b)
# Sở thích chung
giao = set_a & set_b
print("\nSở thích chung:")
if len(giao) > 0:
    print(giao)
else:
    print("Không có sở thích chung.")
# Sở thích chỉ Người A có
chi_a = set_a - set_b
print("\nSở thích chỉ Người A có:")
print(chi_a)
# Tất cả sở thích
tat_ca = set_a | set_b
print("\nTất cả sở thích:")
print(tat_ca)
# Tính độ tương đồng
if len(tat_ca) == 0:
    do_tuong_dong = 0
else:
    do_tuong_dong = len(giao) / len(tat_ca) * 100
print("\nĐộ tương đồng: {:.2f}%".format(do_tuong_dong))