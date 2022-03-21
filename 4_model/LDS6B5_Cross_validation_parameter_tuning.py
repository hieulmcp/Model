Cross_validilation = '''
    1. Vi sao cross-validation hữu ích ?
        - Giúp đánh giá chất lượng mô hình
        - Giúp chọn mô hình sẽ hoạt động tốt nhất trên dữ liệu unseen data
        - Giúp tránh overfitting and underfitting
    2. Overfitting và underfitting
        - Underfitting: không nắm bắt đủ các mẫu trong dữ liệu => Mô hình thực hiện kém cả training set lãnh testset
        - Overfitting: đề cập đến a nhiễu và b các mẫu không khái quát tốt cho unseen data. Mô hình thực hiện rất tốt cho training test những kém ở test set
        - Dữ liệu chỉ năm trên tập trainset và chia dữ liệu ra các phần bằng nhau rồi chạy => Ví dụ: chia 10 lần thì 1 test 9 bộ lại train
        - K-fold: 
'''

Tuning_parameter = '''
    1. Vi sao cần có tunning parameter
        - Với các model đang sử dụng thì điều không thể thiếu là parameter và tất nhiên là tùy thuộc vào mỗi bài toán cụ thể, số dữ liệu training đang có, sẽ có parameter thịch hợp
        - Việc thự nghiệm parameter khác nhau là rất cần thiết
        - KNN có các parameter 
        - Việc thay đổi parameter sẽ ảnh hưởng đến chất lượng model => Công việc tìm được parameter ổn nhất => ĐƯợc gọi là điều chỉnh siêu tham số - Tunning HyperParameter
    2. Phương pháp sử dụng để chọn tunning parameter
        2.1. Grid search
            * Tập hợp các mô hình khác nhau với các tham số của chúng, nằm trên 1 lưới
            * Những gì làm là đào tạo từng mô hình và đánh giá nó bằng cách sử dụng xác thực chéo
            * Sau đó chọn mô hình thực hiện tốt nhất
            * Ưu điểm
                - Diệt nhầm con hơn bỏ sót, nên thường được ưu tiên lựa chọn
            * Nhược điểm
                - Đối với model cần lập nhiều parameter và nhiều giá trị thì việc tunning sẽ mất nhiều thời gian, hàng giờ => có thể bằng ngày
            => Mục đích lấy sao cho score tốt nhất
        2.2. Random search
            * Với random search đúng như tên gọi, từ những giá trị parameter ta thiết lập, Random search sẽ chọn ngẫu nhiên các cặp parameter để tiến hành độ chính xác của model
            * Ưu điểm
                - Random nên sẽ chạy không đủ các trường hợp như grid search nên sẽ nhanh hơn đáng kể
            * Nhược điểm
                - Có thể bỏ qua trường hợp hyper parameter tốt nhất
            
'''