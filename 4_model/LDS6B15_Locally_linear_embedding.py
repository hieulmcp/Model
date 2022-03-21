LLE = '''
    1. Giới thiệu
        - LLE (locally linear Embedding): nhúng tuyến tính cục bộ, là 1 thuật toán giảm chiều dữ liệu phi tuyến tính trong loại Manifold Learning
        - Thuộc nhóm: Unsupervised Learning
        - LLE là 1 kỹ thuật manifold learning hoạt động bằng cách đo lường cách thực mỗi cá thể huấn luyện liên quan tuyến tính với láng giềng gần nhất của nó
        => Sau đó tìm kiếm đại diện low-dimensional của bộ huấn luyện nơi các mối quan hệ cục bộ được bảo toàn tốt nhất
        - Điều này giúp nó đặc biệt tốt khi tháo xoắn (unrolling) dữ liệu khi dữ liệu không có quá nhiều nhiễu
    2. Ứng dụng
        - Trong nhiều lĩnh vực nghiên cứu, các tập dữ liệu lớn cần được giản hóa và dễ dàng hơn để hình dung
            * Hình ảnh khuôn mặt hoặc bài phát biểu (âm thanh) là phức tạp và cần phải được xử lý trước khi 
            các mẫu cơ bản bên trong các dữ liệu này có thể được nhình thấy => Cần phải giảm kích thước
    3. Thuật toán
        Bước 1: LLE tìm những KNN hàng xóm gần nhất của các điểm
        Bước 2: Tính xấp xỉ mỗi vector dữ liệu như một tổ hợp tuyến tính  trọng số của các hàng xóm gần nhất của nó
        Bước 3: Tính toán các trọng số tái tạo tốt nhất các vector từ các làng giềng của nó, sau đó tạo ra các low-dimensional vector 
        được tái tạo tốt bởi các trọng số
        Bước 4: LLE bảo tồn khoảng cách cục bộ giữa các điểm dữ liệu và sẽ phát hiện cấu trúc phi tuyến tính trong dữ liệu
        Bước 5: Sau đó ta có nhiều điểm nối dọc đường theo đường công manifold
        Bước 6: Việc ghép từng điểm không liên quan đến quá trình chuyển đổi (dịch, xoay...) để trọng số tuyến tính của các điểm là bất biến
        => Ta sử dụng các trọng số để tái tạo các điểm diwx liệu trong low dimensional
        => Khoảng cách cục bộ giữa các điểm được bảo toofnn theo cách này
    4. Nhược điểm
        - LLE nhạy cảm với nhiễu hoặc các ngoại lệ
        - Các bộ dữ liệu có mật độ khác nhau và không phải lúc nào cũng có thể có manifold phẳng. Trong những trường hợp này, LLE có kết quả kém
        - LLE là 1 phương pháp unsupervied learning và giả định rằng các điểm dữ liệu nằm trên hoặc nằm gần một manifold phẳng, có thể không giải 
        quyết một số tình huống khác như vấn đề multi-class classification (phân loại nhiều lớp)
        
'''