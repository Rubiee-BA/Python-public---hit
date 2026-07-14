Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Bài tập về nhà buổi 1
... ## Bài 1: Python là ngôn ngữ thông dịch hay biên dịch?
... Python là **ngôn ngữ thông dịch **.
... **Tại sao?**
... * **Cơ chế:** Khi bạn chạy một chương trình Python, mã nguồn không được chuyển đổi trực tiếp thành mã máy như ngôn ngữ biên dịch (C/C++). Thay vào đó, mã nguồn Python được trình thông dịch chuyển đổi sang một dạng mã trung gian gọi là **Bytecode**.
... * **Thực thi:** Sau đó, Bytecode này sẽ được máy ảo Python đọc và thực thi từng dòng một.
... * **Đặc điểm:** Nhờ cơ chế này, bạn có thể chạy mã ngay lập tức mà không cần bước biên dịch tốn thời gian, giúp việc kiểm thử và phát triển phần mềm nhanh chóng hơn.
... 
... ---
... 
... ## Bài 2: Tổng hợp kiến thức Python
... ### 1. Các kiểu dữ liệu trong Python
... * **Số nguyên (Int):** 'int' (Ví dụ: '10', '-5')
... * **Số thực (Float):** 'float' (Ví dụ: '3.14', '2.0')
... * **Chuỗi (String):** 'str' (Ví dụ: '"Xin chào"')
... * **Boolean:** 'bool' (Giá trị: 'True', 'False')
... * **Danh sách (List):** 'list' (Ví dụ: '[1, 2, 3]')
... ### 2. Các toán tử trong Python
... * **Toán tử số học:** '+', '-', '*', '/', '//','%', '**' (lũy thừa).
... * **Toán tử so sánh:** '==', '!=', '>', '<', '>=', '<='.
... * **Toán tử logic:** 'and', 'or', 'not'.
... * **Toán tử gán:** '=', '+=', '-=', '*=', '/='.
... ### 3. Mệnh đề điều kiện và vòng lặp
... * **Mệnh đề điều kiện:**
...   * 'if': Kiểm tra điều kiện đầu tiên.
...   * 'else': Xử lý khi tất cả điều kiện trước đó sai.
... * **Vòng lặp:**
...   * 'for': Lặp qua một chuỗi (list, tuple, string...) hoặc một khoảng số.
...   * 'while': Lặp lại chừng nào điều kiện vẫn còn đúng.
... ### 4. Kiểu dữ liệu True, False (Boolean)
... * Đây là kiểu dữ liệu logic ('bool') dùng để biểu thị giá trị đúng ('True') hoặc sai ('False').
* Chúng thường là kết quả của các phép so sánh (ví dụ: `5 > 3` trả về 'True') hoặc các mệnh đề điều kiện.
