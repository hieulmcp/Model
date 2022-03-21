Regression_analysis = '''

    1. Giới thiệu chung
        a. Regression analysis
            - Kỹ thuật mô hình tiên đoán (predictive modelling technique)
            - Điều tra mối quan hệ giữa dependent (target) và các independent variable (predictor)
        b. Kỹ thuật này sử dụng làm gì
            - Để dự báo (forecasting)
            - Mô hình hóa chuỗi thời gian (time series) và mối quan hệ giữa các biến
        c. Công cụ quan trọng để lập mô hình và phân tích
        => Công cụ quan trong tiên đoán dữ liệu và phân tích dữ liệu
    2. Đặc điểm và mục tiêu
        - Quy trình: Input variable => model => Output (number)
        - Mục tiêu: dự báo giá trị số (number) từ biến đầu vào input variable
        -Đặc điểm:
            + Dự đoán number từ input variable
            + Regression là supervised task
            + Target variable là giá trị số
        - Ví dụ: dự báo sản lương/ giá vàng/ giá nhà
    3. Xây dựng và áp dụng model
        - Training Phase
            * Điều chỉnh tham số model (model parameter)
            * Sử dụng dữ liệu huấn luyện (training data)
        - Testing Phase
            * Áp dụng mô hình (learned model)
            * Sử dụng dữ liệu mới (test data)
        - Đánh giá model
            * Dựa trên độ phủ của sroce của model của các Phase
            * Thời gian thực hiện
        => Mục tiêu để tránh overfitting và underfitting để xem model có phù hợp không ? => Model đó phù hợp không
    
'''
Danh_gia_mo_hinh_regression = '''
    1. Một số kỹ thuật đánh giá dùng 2 cách
        - Trực quan hóa dữ liệu: dùng distribution plot  để so sánh giữa actual value gần như khớp với nhau thì có thể dùng model
        => Ngoài ra dùng biểu đồ scatter plot 2 trùng nhau giữa actual value và predict value
        - Số liệu thống kê giữa y và y_pred có phù hợp với nhau không ?
            * Dùng thang đo thống kê: Mean Squared Error (MSE): (chêch lệch thực - dự đoán)^2/n phần tử 
            hoặc MAE (mean abssolute Error): |chêch lệch thực - dự đoán|/n phần tử
            => So sánh phương sai của 2 dự báo và thực tế để xem mức độ phương sai
            * Dùng R^2: Đo độ phù hợp của bài toán để xem mức độ phù hợp của phương sai
            1-(thực tế - dự đoán)^2/(thực tế - trung bình thực tế)^2 => MSE chia độ phân tán dữ liệu để ra đc mực độ phù hợp của model
        => Đánh giá chỉ đánh giá trên giá trị thực và giá trị dự báo
        => Phải viết ra những hàm đễ đánh giá theo thông kê và theo trực quan hóa dữ liệu
        => Phải đánh giá trên bộ dữ liệu train, bộ dữ liệu test và có thể làm ngẫu nhiên
        => Nếu sai biệt R^2 giữa train và test sai biệt tương đối với nhau, nếu sai biệt quá nhiều thì phải xem lại sự ổn định của mô hình
        => Khi cho test mô hình bằng nhau thì sẽ có tính ổn định hơn
    2. Cách xác định cần làm trong mỗi bộ dữ liệu
        - Training data: điều chỉnh các model parameter
        - Validation data: ngừng training tránh trường hợp overfiting và ước tính hiệu xuất
        - Test data: Đánh giá hiệu suất trên dữ liệu mới
    3. So sánh mô hình với mô hình baseline model
        - So sánh cơ sở dụ báo với phần chêch lệch nếu nó về bằng cơ sở

'''

Linear_regression = '''
    1. Giới thiệu
        - Thuật toán đơn giản nhất trong nhóm thuật toán supervised learning
        - Hệ thống quản lý đánh giá tính dụng
        - Ý tưởng theo Regression analysis
        - Mối quan hệ được mô hình hóa tuyến tính
        => Nếu giữa 2 đại lượng biến có tuyến tính với nhau thì mới có thể sử dụng linear regression
        => Con không có mối quan hệ thì nên bỏ ra
        - Dùng Correclation lớn hơn 0.6 trở đi thì có tương quan, 0.9 trở lên thì mới có tương quan mạnh
    2. Mục tiêu
        - Làm sao tìm ra đường thẳng với 2 biến và có 1 đường thẳng tuyến tính sao cho MSE, MAE nhỏ và R2 cao nhất
    3. Hạn chế
        - Nhạy cảm với nhiễu noise: outlier, missing value, error
        - Nên xem residplot sai biệt năm trên và dưới có phân bổ điều trên và dưới và ngẫu nhiêu nó quan hệ với nhau thể nào và có thể làm 
        mô hình tuyến tính hay không => Để biết đc R2 bé hay lớn
        - Không hợp với mô hình hóa các mối quan hệ tuyến tính
    4. Random_state: dùng để cố định cho không cho dữ liệu ngẫu nhiêu cho những lần tiếp theo
    5. Không nên dùng poly vì nó tăng thuộc tính và cũng như overfitting
    
        
'''
Lua_chon_thuoc_tinh = '''
    1. Dùng thư viện K-best để chọn thuộc tính nào phù hợp với bài toán
    2. Đánh giá được feature nào là quan trọng
    3. Lựa chọn biến ố trong quy đa biến
        - Khi thêm biến số vào mô hình, SSE luôn giảm, R2 luôn tăng
        - Không nên sử dụng quá nhiều biến số sẽ gây ra hiện tượng
            * Hiện tượng quá khớp (overfitting): Cao ở bộ train và thấp ở bộ test
            * Xảy ra sử dụng nhiều biến số mà bộ mẫu quá ít
        - Hai phương pháp để khác phục overfitting
            * Sử dụng R2 hiệu chỉnh: Giá trị R2 hiệu chỉnh cho số biến độc lập
            * Tách mẫu quan sát thành 2 phần: bộ mẫu xây dựng và bộ kiểm định
'''

Mot_so_luu_y = '''
    - Các giá trị ngoại lệ (outliers): Các quan sát có giá trị khác biệt lớn so với các quan sát khác
    - Hiện tượng đa cộng tuyến: các biến độc lập (input) có tương quan lớn với nhau có thể làm sai lệch mô hình
     
'''