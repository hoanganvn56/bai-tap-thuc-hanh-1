Câu 4: Tính chỉ số BMI và phân loại tình trạng cơ thể
Mô tả thuật toán bằng ngôn ngữ tự nhiên:

Bước 1 (Nhập): Nhập cân nặng (tính bằng kg) và chiều cao (tính bằng mét) từ bàn phím.

Bước 2 (Xử lý): * Tính chỉ số BMI theo công thức:
BMI = W/(HXh)
Sử dụng cấu trúc rẽ nhánh if - elif - else để phân loại:

Nếu BMI<18.5: Kết luận "Gầy".

Nếu 18.5≤BMI<25: Kết luận "Bình thường".

Nếu 25≤BMI<30: Kết luận "Hơi thừa cân".

Ngược lại (BMI≥30): Kết luận "Béo phì".

Bước 3 (Xuất): In ra chỉ số BMI và thông báo tình trạng cơ thể tương ứng.
