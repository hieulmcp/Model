Decision_tree = '''
    1. Giới thiệu
        - Decision tree được sử dụng cho cả classification và regression
        - Là thuật toán theo mô hình cây sử dụng xác định kết quả hành động. Mỗi nhánh cây đại diện cho một quyết định, sự xuất hiện hay phản ứng có thể xảy ra
    2. Ứng dụng
        - Decision tree được sử dụng để phát triển các mô hình dự đoán và phân loại trong nhiều lĩnh vực khác nhau:
            * Business management
            * Customer Relationship Management
            * Fraudulent Statement Detection
            * Engineering
            * Energy Consumption
            * Fault diagnosis
            * Healthcare Management
            Ví dụ: Đánh giá cơ hội mỡ rộng thương hiệu của một doanh nghiệp sử dụng dữ liệu bán hàng lịch sử
    3. Ý tưởng
        - Tìm tính năng (feature) mô tả có chứa thông tin nhất về target feature và sau đó chia tập dữ liệu dọc theo các giá trị của các feature => Sao cho tập con thuần khiến nhất
        - Quá trình tìm kiếm các tính năng có thông tin nhất được thực hiện cho đến khi chúng ta có hoàn điều kiện dừng khi cuối cùng kết thúc ở nút lá (leaf node)
        => Các nút có chứa các thông tin dự đoán mà chúng ta thực hiện cho các thực thể mới được trình bày cho trained model
        => Chia dữ liệu vào các vùng thuần nhất
        - Khi chia theo thứ tự: Root node (nút gốc) => Các nút nội tại (interior/internal node) => leaf node được nói với nhau bằng các nhánh (branch)
    4. Xây dựng cây quyết định
        Bước 1: Bắt đầu với các mẫu dữ liệu tại root node nút gốc 
        Bước 2: Các mẫu được phân vùng dữa trên input để tạo ra các tập con thuần khiết nhất (purest subset)
        Bước 3: Lặp lại quá trình phân vùng dữ liệu cho các tập con thuần khiết hơn
        a. Làm sao để xác định phân chia tốt nhất ?
            - Lam sao chia các tập con đồng nhất/ thuần khiến nhất có thể thì càng tốt
        b. Đo lường mức độ không đồng nhất
            - Để so sánh các cách khác nhau khi cắt dữ liệu trong một node
                * Chỉ số Gini-Gini index: 
                    + Càng cao => càng ít thuần khiết
                    + Càng thấp => càng thuần khiết
                    + Cách chia gini
                        * Tính gini cho từng thuộc tính, theo class kết quả
                        * Thuộc tính nào trong nhóm các thuộc tính có gini bé nhất => Chọn thuộc tính đó để chia nhánh cho cây
                            => Gini tại 1 điểm  = 1 - xác xuất bình phương
                * Chỉ số Entropy
                    + Càng cao càng không thuần khiến
                    + Càng thấp càng thuấn khiến
                *  Information Gain
                    + Càng lớn càng tốt
                    + Càng bé thì không chọn
                    => Cái nào lớn thì tốt hơn
                    => Tính gain cho từng thuộc tính, theo class kết quả
                    => Thuộc tính nào trong nhóm các thuộc tính có Gain lớn nhát => Chọn thuộc tính đó để chia nhánh cho cây
        c. Variable nào sẽ được chia nhỏ ?
            - Chia nhỏ trên tất cả các biến kiểm tra
        d. Khi nào dừng chia nhỏ node
            - Khi tất cả các mẫu có class label
            - Số lượng các sample trong node đạt đến mức tối thiểu
            - Thay đổi trong đo lường độ không đồng nhất nhỉ hơn ngưỡng
            - Đạt được sâu cây tối đa
        e. Decision tree trong classification
            - Cây kết quả thương đơn giản dễ hiểu
            - Tính toán không tốn kém
            - Dùng ranh giới ra quyết định là rectilinear
        f. Khuyến điểm
            - Nếu tính năng liên tục được sử dụng thì cây có thể trở nên rất lớn và ít diễn giải => Bining rank dữ liệu trong LDS5 => Chia khoảng dữ liệu
            - Nhưng thay đổi nhỏ trong dữ liệu có thể dẫn đến cây hoàn toàn khác (Có thể dùng random forest để khắc phục)
                * 10 cấp thì có 2^10 = 1024 nút lá thì nếu mẫu có 2000 mẫu thì không đủ để chia nút lá
            - Nếu số lượng tính năng tương đối lớn mà số lượng mẫu lại nhỏ có thể dẫn đến không phù hợp với dữ liệu
            - Vẽ cây như thế nào ? => Cách xây dựng cây để hiểu
            - Cây sẽ đi từ theo thuộc tính ví dụ thuộc tính số lượng 3 thì chỉ cho 3 nhánh thui theo cách chia của 3 thuộc tính đó cây sẽ chia


'''