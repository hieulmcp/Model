
Naive_bayesian = '''
    - Gốc vấn đề phải cần có xác xuất luôn có 1 hàm phân phối để biết được xác xuất từ 0-1 => Phân phối dữ liệu đó có những thuộc xích ma... => Tính được xác xuất của dữ liệu bao nhiêu
    - Dùng giá trị phân phối chuẩn để xây dựng từng cột để xem mức độ xác xuất thế nào ?
    - Mọi thứ phụ thuộc vào phân phỗi chuẩn dữ liệu để xem mực độ xác xuất từng nhóm

    1. Giới thiệu
        - Dựa trên định lý bayes với các giả định độc lập giữa các yêu tố dự báo
        - Không có ước lượng tham số lặp phức tạp => Hữu ích với tập dữ liệu lớn
        - Phương pháp phân loại hữu ích giựa trên phân phổi chuẩn từ các thuộc tính đơn lẽ
        - Nó gần giống với linenear Regression => Xu hướng đào tạo nhanh hơn
        - Cái giá phải tra cho mô hình này là hiệu suất tổng quan hơi kém hơn so với các phân loại tuyến tính như Logistic Regression và LinearSVC
    2. Lý do các mô hình Naive Bayes rất hiệu quả là
        - Học bằng cách xem xét đặc trưng/ tính năng riêng rẻ và thu thập số liệu thống kê mỗi lớp đơn giản từ từng tính năng
        - Sử dụng công cụ phân phối của Naive bayes => GaussianNB, BernoulliNB và MultinomialNB
    3. Phân loại
        a. GaussianNB
            * Có thể được áp dụng cho bất kỳ dữ liệu liên tục nào
            * GaussianNB lưu trữ dữ liệu TB, độ lệch chuẩn (std deviation) cho từng tính cho mỗi lớp
            * GaussianNB chủ yếu được sử dụng trên dữ liệu High-dimensional data => Nếu nhiều chiều như dữ liệu ảnh...
            => Độ lệch dữ liệu nhất định nào đó 
        b. BernoulliNB
            * Áp dụng trên dữ liệu nhị phân (mỗi thành phần là một giá trị binary bằng 0 và 1)
            * Được áp dụng rộng rãi cho dữ liệu thưa thớt (sparse count data) => Ví dụ như văn bản
            * Số lần xuất hiện trong word giá trị xuất hiện 0, 1
        c. MultinomialNB
            * Áp dụng cho dữ liệu đếm 
            * Tính giá trị TB của từng tính năng (feature) cho mỗi lớp class
            * Được sử dụng rộng rãi cho dữ liệu đếm thưa thớt (sparse count data)
    4. Ứng dụng
        - Realtime prediction: dự đoán thời gian thực
        - Multiclass prediction: dự đoán đa lớp
        - Text classification/ Spam filtering/ Sentiment Analysis: phân loại văn bản, lọc thư rác, phân tích trạng thái
        truyên thông xã hội, đẻ xác định tính cảm khách hàng tích cực hay tiêu cực
        - Recommendation system: hệ thống đề xuất Naive Bayes Classifier và Collaborative Filtering cũng nhau xây dựng hệ thống đề xuất sử dụng kỹ thuật ML
        và khai thác dữ liệu lọc thông tin không xác định và dự đoán người dùng muốn một tài nguyên cụ thể hay không
    5. Khuyết điểm
        - Có thể có các tính năng tương quan => loại bỏ các tính năng liên quan vì khi các tính năng tương quan cao thì sẽ chọn 2 lần trong mô hình có thể
        dẫn đến việc vượt quá tầm quan trọng
        - Nếu một biến phân loại có một danh mục trong tập dữ liệu thử nghiệm mà không có trong tập quan sát thấy trong dữ liệu huấn luyện thì mô hình sẽ gán một xác suất bằng 0
        => Để giải quyết ta có thể dùng kỹ thuật làm mịn hay là ước tính Laplace
    6. Với người dùng:
        => Dùng pipeline chưa các thao tác xử lý để tạo ra model định nghĩa những bước cần làm cho bài toán
    7. Dùng thư pickle để lưu dữ liệu và đọc dữ liệu
        - Chuyển cho người dùng cần dùng pickle
'''
