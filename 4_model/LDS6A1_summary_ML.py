Summary_machine_learning = '''
    1. Giới thiệu
        - ML là khoa học dữ liệu từ việc học hỏi dữ liệu
        - Là 1 nhánh nhỏ trong AI
        a. Mục đích
            - Liên quan chặt chẽ đến thông kê tính toán
            - Cùng tập trung vào việc dự đoán, ra quyết định thông qua việc sử dụng máy tính
            - Có quan hệ chặt chẽ với tối ưu toán học, cung cấp các phương thức, lý thuyết và các miền ứng dụng cho lĩnh vực tương ứng
            - Đôi khi cho vào nhóm data mining (khai thác dữ liệu), tập trung vào việc phân tích khám phá còn gọi là unsupervised learning
        b. Machine learning
            - Học từ dữ liệu
            - Học từ chính nó
            - Khám phá các mẫu ảnh (hidden pattern) và xu hướng
            - Đưa ra các quyệt định theo định hướng dữ liệu (data-driven decision)
        c. Tại sao lại sử dụng machine learning ?
            - Các vấn đề giải pháp tồn tại yêu cầu thực hiện thủ công rất nhiều hoặc danh sách các quy tắc
            => Một thuật toán ML có thể đơn gian hóa code và hoạt động tốt hơn
            - Tim giải pháp tốt cho bài toán
            - Khi môi trường biến động: một hệ thống ML có thể thích nghi với dữ liệu mới
            - Có thể nhận thông tin chi tiết về các vấn đề phức tạp và lượng dữ liệu lớn
    2. Phân loại
        2.1. Supervised learning: target is available => Task driven gồm Regression/ Classification
            * Mục tiêu classification: dự đoán loại category từ các biến dữ liệu được cung cấp
            * Mục tiêu Regression: Dự đoán giá trị số
        2.2. Unsupervisd learning: target is not available => Task driven gồm Clustering/ Association
            * Mục tiêu cluster Analysis: Sắp sếp các item tương tự nhau vào các nhóm
            * Mục tiêu Association analysis: tìm các quy luật để nắm bắt mối liên kết giữa các item
        2.3. Reinforcement learning: Sử dụng thuật toán, máy được huấn luyện để đưa ra các quyết định cụ thể
            * Mục tiêu Reinforcement learning: máy được tiếp xúc với môi trường nơi có liên tục tự thử và sai.
            Học kinh nghiệm trong quá khứ và cố gắng nắm bắt kiến thức tốt nhất có thể đưa ra quyết định nghiệp vụ chính xác
    3. Thách thức của machine learning
        3.1. Không đủ dữ liệu đào tạo (training data)
            * Cần nhiều dữ liệu để ML hoạt động chính xác
            * Cần đến hàng triệu mẫu để thực hiện thuật toán ML
        3.2. Dữ liệu đào tạo không đại diện
            * Đại diện 1 số thuộc tính khái quát được bài toán: tập dữ liệu sẽ không tốt nếu nó thiếu đi một vài đại diện
            * Cần phải có 1 tập dữ liệu huấn luyện đại diên cho các trường hợp ta muốn khái quát hóa
            * Dữ liệu chất lượng quá kém: chứa nhiều lỗi, ngoại lệ và nhiều (errors, outlier, noise), hệ thống sẽ gặp khó khăn
            => Vì vậy cần phải xử lý và nỗ lực dành thời gian để làm sạch dữ liệu
        3.3. Thuộc tính không liên quan
            * Hệ thông chúng ta chỉ có khả năng học nếu dữ liệu đào tạo có đủ thuộc tính liên quan và có ít thuộc tính không liên quan.
            Đây là 1 phần thành công trong dự án ML để huấn luyện => Được gọi là feature engineering
                trong đó:
                    - Lựa chọn thuộc tính (Feature selection): lựa chọn các thuộc tính hữu ích nhất để huấn luyện dựa trên những thuộc tính hiện có
                    - Trích xuất thuộc tính (Feature extraction): Kết hợp các thuộc tính hiện có để tạo ra 1 tính năng mới  hữu ích hơn
                    => Giảm kích thước của dữ liệu, dimensionality reduction algorithms hoặc tạo thêm thuộc tính mới bằng thu thập dữ liệu mới
        3.4. Overfitting dữ liệu huấn luyện
            * Overfitting (Over-learning): Khi mô hình thể hiện sự chính xác trên tập huấn luyện (training data) nhưng lại kém chính xác trên
            tập dữ liệu kiểm tra (test data) => Qua khớp với tập dữ liệu huấn luyện
            * Nguyên nhân: 
                - Tập dữ liệu có nhiễu (noise)
                - Mô hình qua phức tạp quá nhiều tham số so với dữ liệu dữ liệu quan sát được thể hiện
                => Chỉnh nhiễu đã gây tác động xấu đến quá trình dự đoán của mô hình dữ liệu kiểm tra
            * Nhận biết
                - Khi mô hình có độ lệch chuẩn nhỏ (low bias) nhưng phương sai lớn (high variance)
            * Cách giải quyết
                - Đơn gian hóa mô hình bằng cách chọn một hình có ít tham số hơn, bằng cách giảm các thuộc tính trong dữ liệu đào tạo
                - Thu thập thêm dữ liệu đào tạo
                - Giảm nhiễu trong dữ liệu đào tạo: sữa lỗi dữ liệu error và loại bỏ các ngoại lệ outliers
        3.5. Underfitiing dữ liệu huấn luyện
            * Underfitting (under-learning): khi một mô hình thực thi không tốt trên cả tập dữ liệu huấn luyện và tập dữ liệu kiểm tra.
            => Cũng có thể hình dung khi mô hình không khớp với tập dữ liệu huấn luyện
            * Nguyên nhân: xảy ra khi mô hinh đang xây dựng đơn giản so với tập dữ liệu
            * nhận biết: khi mô hình có kết quả độ lệch chuẩn lớn nhưng phương sai nhỏ (high bias nhưng low variance)
            * Cách giải quyết:
                - Chọn 1 mô hình mạnh mẽ hơn, nhiều tham số hơn
                - Lựa chon thuộc tính tốt hơn cho thuật toán (feature engineering)
        => Model lý tưởng là model không quá đơn gian nhưng cũng không quá phức tạp và không dễ bị ảnh hưởng bởi dữ liệu nhiễu

        3.6 Độ lệch (Bias)
            - Độ lệch là 1 số đặc trưng cho giá trị trung bình của các số liệu so với giá trị đúng. 
            => Độ lệch là lỗi từ việc giả định sai của thuật toán.
            => Mô hình khi có độ lệch sẽ gây ra những sai số khi khái quát hóa => giữa giá trị thực tế và dự báo
            - Bias lơn sẽ dẫn đến tới underfitting
        3.7. Phương sai (Variable)
            - Phương sai là số đặc trưng cho độ phân tán của các số liệu so với số trung bình của nó
            - Phương sai là mức độ nhạy cảm với sự biến động nhỏ trong tập dữ liệu được huấn luyện
            - Chạy nhiều lần trên 1 tập dữ liệu để giảm phương sai
            - Phương sai lớn sẽ gây ra overfitting
        3.8. Cân bằng giữa bias-Variance
            - Lựa chọn mô hình chính là việc cần bằng giữa bias-variance
            - Mô hình bias thấp sẽ có variance cao và sẽ cần huấn luyện nhiều hơn; trong khi mô hình có bias cao sẽ có variance thấp
        3.9. https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html
            Có thể xem ở đây để chon thuật toán phụ hợp khi số lượng mẫu bị thiếu    


'''