Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Bài tập về nhà buổi 1
... ## Bài 1: Python là ngôn ngữ thông dịch hay biên dịch?
... Python là **ngôn ngữ thông dịch**.
... ### Tại sao?
... - **Cơ chế:** Khi bạn chạy một chương trình Python, mã nguồn không được chuyển đổi trực tiếp thành mã máy như các ngôn ngữ biên dịch (ví dụ: C/C++). Thay vào đó, mã nguồn Python được chuyển đổi sang một dạng mã trung gian gọi là **Bytecode**.
... - **Thực thi:** Bytecode sẽ được **Python Virtual Machine (PVM)** đọc và thực thi.
... - **Đặc điểm:** Nhờ cơ chế này, Python không cần biên dịch toàn bộ chương trình trước khi chạy, giúp việc phát triển, kiểm thử và sửa lỗi diễn ra nhanh chóng.
... > **Lưu ý:** Python thường được gọi là ngôn ngữ thông dịch, mặc dù trên thực tế CPython vẫn biên dịch mã nguồn thành Bytecode trước khi thực thi.
... 
... ---
... 
... # Bài 2: Tổng hợp kiến thức Python
... ## 1. Các kiểu dữ liệu trong Python
... | Kiểu dữ liệu | Tên | Ví dụ |
... |--------------|-----|--------|
... | Số nguyên | `int` | `10`, `-5` |
... | Số thực | `float` | `3.14`, `2.0` |
... | Chuỗi | `str` | `"Xin chào"` |
... | Boolean | `bool` | `True`, `False` |
... | Danh sách | `list` | `[1, 2, 3]` |
... 
... ---
... 
... ## 2. Các toán tử trong Python
... ### Toán tử số học
... - `+` : Cộng
... - `-` : Trừ
... - `*` : Nhân
... - `/` : Chia
... - `//` : Chia lấy phần nguyên
... - `%` : Chia lấy dư
... - `**` : Lũy thừa
### Toán tử so sánh
- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`
### Toán tử logic
- `and`
- `or`
- `not`
### Toán tử gán
- `=`
- `+=`
- `-=`
- `*=`
- `/=`
---
## 3. Mệnh đề điều kiện và vòng lặp
### Mệnh đề điều kiện
- `if`: Kiểm tra điều kiện.
- `elif`: Kiểm tra điều kiện tiếp theo nếu điều kiện trước sai.
- `else`: Thực hiện khi tất cả điều kiện đều sai.
### Vòng lặp
- `for`: Dùng để lặp qua một chuỗi dữ liệu (`list`, `tuple`, `string`, `range`,...).
- `while`: Lặp lại khi điều kiện còn đúng.
---
## 4. Kiểu dữ liệu Boolean (`True`, `False`)
Kiểu dữ liệu **Boolean** (`bool`) chỉ có hai giá trị:
- `True`
- `False`
Boolean thường là kết quả của phép so sánh hoặc được sử dụng trong các câu lệnh điều kiện.
Ví dụ:
```python
print(5 > 3)# True
print(10 == 2)# False
age = 20
if age >= 18:
    print("Đủ tuổi")
else:
    print("Chưa đủ tuổi")
