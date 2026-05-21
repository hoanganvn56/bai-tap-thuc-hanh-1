/* Câu 1: Tính tổng các chữ số của một số tự nhiên n Mô tả thuật toán bằng ngôn ngữ tự nhiên:

Bước 1 (Nhập): Yêu cầu người dùng nhập vào một số tự nhiên n từ bàn phím.

Bước 2 (Xử lý): 

Cách 1 (Dùng chuỗi): Chuyển số $n$ thành một chuỗi các ký tự. Duyệt qua từng ký tự (chữ số), chuyển nó ngược lại thành số nguyên rồi cộng dồn vào một biến tổng ban đầu bằng 0.

Cách 2 (Dùng toán học): Trong khi $n$ còn lớn hơn 0, lấy chữ số hàng đơn vị bằng phép chia lấy dư cho 10 (n \pmod(10)), cộng vào biến tổng, sau đó cắt bỏ chữ số hàng đơn vị bằng phép chia lấy nguyên cho 10 (n / 10).

Bước 3 (Xuất): In kết quả tổng các chữ số ra màn hình.*/
