Random_Forest = '''
    1. Giới thiệu
        - Thuật toán này mục đích chỉnh sửa Decision tree => Overfitting 
        - Nhược điểm của cây quyết định - decision tree là chúng có khuynh hướng overfitting dữ liệu huấn luyện
        => Random forest là một cách giải quyết vấn đề này
        - Random forest bản chất là một tập hợp các cây quyết định, trong đó mỗi cây hơi khác so với các cây còn lại
    2. Ý tưởng
        - Mỗi cây có thể làm một công việc dự đoán tương đối tốt, nhưng có khả năng overfitting một phần dữ liệu.
        => Xây dựng nhiều cây thì các cây sẽ hoạt động tốt và vượt trội theo nhiều cách khác nhau, từ đó ta có thể giảm số lượng overfit bằng cách lấy trung bình kết quả của chúng
        - Điều này giúp giảm overfiting trong khi vẫn giữ được sức mạnh dự đoán của cây
        - Để thực hiện chiến lược này thì cần phải xây dựng cây quyết định trước => Công việc chấp nhận được để dự đoán target => Nên khác với cây khác
        => Đưa ngẫu nhiên mẫu vào cây để đảm bảo mỗi cây khác nhau
    3. Có 2 cách để các cây trong Random forest được chọn ngẫu nhiên
        - Bằng cách chọn các điểm giữ liệu được sử dụng để xây dựng một cây
        - Bằng cách chọn các tính năng trong mỗi split test
    4. So sánh với Decision tree
        - Random forest là một tập hợp của nhiều cây Decision tree
        - Decision tree có thẻ bị ảnh hưởng bởi overfitting, con Random forest ngăn overfitting bằng cách tạo ra cây trên các tập ngẫu nhiên
        => Random forest nếu overfitting thì phải tìm thuất toán khác decision tree
        - Decision tree tính toán nhanh hơn
        - Random forest khó giải thích, Trong decision tree có thể diễn giải dễ dàng và có  thể chuyển đội thành các quy tắc
    5. Ứng dụng
        - Phân loại phương tiện giao thông được phát hiện
        - Phân loại ảnh viễn thám (remote sensing)
        - Dự báo xu hướng cổ phiểu trên thị trường chứng khoán (stock trend forecasts)
        - Video classification
        - Image classification
    6. Các bước thực hiện
        - Chọn các mẫu ngẫu nhiên từ các tập dữ liệu cung cấp
        - Xây dựng cây quyết định cho các mẫu được chọn và nhận kết quả dự đoán từ mỗi cây quyết định
        - Thực hiện bỏ phiếu cho từng kết quá dự đoán
        - Cho kết quả dự đoán có nhiều phiếu nhất là dự đoán cuối cùng
    7. Làm thế nào để tìm thuộc tính quan trọng ?
        - Random forest cung cấp một chỉ số lựa chon chính năng tốt => Scikit learn cũng cấp thêm một biến model cho thây tầm quan trọng
        hoặc đóng góp tương đối của từng tính năng trong dự đoán
        - Nó tự đống tính toán điểm liên quan của từng tính năng trong quá trình đào tạo, sau đó nó cân đối mức độ liên quan xuống sao cho tổng của tất cả các điểm là 1.
        => Điểm số này sẽ giúp ta chọn các tính năng quan trọng nhất và bỏ đi các tính năng ít quan trọng cho việc xây dựng model
    8. Tìm các feature phù hợp với thuật toán Random forest
        - Để biết thông tin các tree trong random forest
            * Danh sách các tree, có thể truy xuất theo chỉ số
        - Nên xem các thuộc tính nào quan trọng và cần thiết để áo dụng trong mô hình, bỏ bớt các thuộc tính ít quan trọng (để không ảnh hưởng đến bài toán)
            * model.feature_importances_
    9. Đối với những thuật toán khác ngoài Random Forest => Thì dùng Select K-Best
        - Riêng với Random Forest dùng tính năng của feature_importances_ để chọn thuộc tính của bài toán
        - Lấy những feature > 0.5 => Thể hiện mức độ quan trọng
    10. Đối với bài toán Random forest không phải là dễ dự báo
        - Cần nên nhìn bài toán theo nhiều dạng khác nhau chuyển regression <=> classification chuyển dự báo khác nhau theo yêu cầu bài toán cho phù hợp
        - Có thể biến bài toán nếu thấp về Score và overfitting ở bài toán regression chuyển sang bài toán classification => theo khoảng giá hoặc giá trị phù hợp theo bins
        => Chia range có thể để tốt hơn cho bài toán
    11. Làm sao chuyển raw material để ra bài toán có các feature áp dụng đc
'''