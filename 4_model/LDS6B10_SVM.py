Support_Vector_Machine = '''
    - Thuật toán khó nói nhất
    1. Giới thiệu
        - Là 1 mô hình machine learning rất mạnh mẽ và linh hoạt, có khả năng thực hiện phân loại tuyến tính và phi tuyến tính
        hồi quy và thậm chi phát hiện ngoại lệ
        - Là 1 một trong mô hình phổ biến nhất trong ML và bất kỳ ai cũng quan tâm đến ML nên biết
        => Đặc biệt thích hợp phân loại các bộ dữ liệu phức tạp nhưng nhỏ và vừa
        => Là 1 thuật toán strong learning
    2. Ứng dụng
        - SVM có thể được sử dụng để giải quyết các vấn đề khác nhau trong thế giới thực
            * Phân loại văn bản và siêu văn bản
            * Phân loại các ký tự viết tay
            * Nhận dạng chữ viết
            * Phát hiện xâm nhập
            * Phát hiện thông tin ẩn dấu trong hình ảnh kỹ thuật số
            * Phân loại hình ảnh. Kết quả thử nghiệm cho thấy SVM đạt độ chính xác cao hơn đáng kể so với các lược đồ sàng lọc truy vấn truyên thống sau khi chỉ thực hiện 3 đến 
            4 lượt phản hồi có liên quan
    3. Thuật toán
        3.1. Linear support vector machine
            - Ý tưởng cơ bản của SVM
            - Quan sát hình có 2 dạng phân tách
                * Phân tách theo giới tuyến tính
                => Tìm 1 đường mà phân tách thành 2 loại khác nhau: chia số lượng điểm 2 bên đúng nhất có thể có, có vô số cách chia
                => Thực hiện chia làm sao cho các điểm tách biệt làm sao càng tốt càng hay
                => Khi dự báo có thể các điểm năm trên đường thì nó có thể bị sai dự báo
                * Phân tách ranh giới theo SVM
                => Xây dựng con đường mà rộng nhất có thể có để làm sao tách bật chia đôi 2 nhóm
                => Sẽ làm hàng rào sắt ở giữa con con đường để khỏi vi phạm luận
                => Những điểm trên và outlier điễm nhiễu sẽ ko bị ảnh hưởng
            - Có thể nghĩ SVM classifier như cách làm đường phố rộng nhất có thể, đường giữa là tim đường và các đường đứt nét là lề đường
            (được biểu thị bằng các đường dứt nét song song) phân chia các lớp, nó được gọi là phân loại theo lề lớn
            => Giữa 2 nhóm có tách bật tuyến tính => Theo tỉ lệ kính
            - Soft-margin classification: chấp nhận nó khá nhạy cảm với các ngoại lệ => Tùy theo tunning của bài toán
            => Tìm làm sao có cái lề lớn nhất có thể có, chấp nhận các sai số về dữ liệu nhiễu
            - Thuật toán này liên quan đến khoảng cách như thế nào chỉ là 1 khoảng cách 1 điểm và hay 1 điểm khoảng cách
            => Đi tim 1 vector sao cho khoảng cách tới mặt phẳng là lớn nhất
        3.2. Nonlinear Support vector machine
            - Dựa trên khoảng cách 1 con số 1 để chia => Chuyển nhiều không gian nhiều chiều thi sẽ đường cong để chia dữ liệu
            - Chỉ là chuyển chiều không gian thui không có nâng bậc nhưng chỉ là không gian 2 chiều
            - Tính từ 1 điểm đến 1 điểm như thế nào ? => Dựa trên khoảng cách đến 1 mặt phẳng nào đó thì nó đồng điều nhau
    4. SVM Regression
        - Tìm ra 1 con đường à chứa nhiều điểm nhất có thể thay 1 đường thì nó là 1 con đường
        - Tìm ra 1 chiều không gian hay nhất có thể
    5. Nhược điểm
        - Chọn chức năng kernel tốt là không dễ hiểu
        - Thời gian đào tọa dài cho các tập hợp dữ liệu lớn
        - Khó có thể hiểu rõ và giải thích mô hình cuối cùng các biến trọng số
        - Vì mô hình cuối cùng không dễ nhận thấy, ta không thể thực hiện các phép hiệu chỉnh nhỏ cho mô hình
    6. Chú ý
        - Tham số C càng lơn thì con đường càng nhỏ sai sót càng ít => C càng lớn thì sai biệt càng nhiều
        - kernal: rbf ko quan tâm đến tuyến tính hay => Nếu poly thì sẽ làm degree mặc địch 3
'''