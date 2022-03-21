Association_Rule_Mining = '''
    1. Giới thiệu
        - Association rule learning khám phá mối quan hệ thu vị giữa các biến
        - Kỹ thuật để xác định mỗi quan hệ cơ bản giữa các item khác nhau
        - Là 1 thuật toán cổ điển => Recomment
        - Tìm ra những luật bài toán để đóng gói để tăng thêm những mặt hàng a thì mua mặt hàng b
    2. Đặc điểm của những thuật toán này
        - Trong thời gian ngắn các giao dịch liên quan đến một mô hình
        - Lợi nhuận nhiều hơn có thể được tạo ra nếu mối quan hệ giữa các mặt hàng được mua trong các giao dịch khác nhau được xác định
        - Quá trình xác định mối quan hệ giữa các sản phẩm được gọi là rule mining, khai phá quy luật kết hợp
        => Có thể gọi lại để thực hiện chính sách quảng cáo, những mặt hàng đi cùng với nhau, đặt đưa những vị trí nào để có thể kết hợp mặt hàng
        => Từ các giao dịch xuất hiện nhiều nhất và các giao dịch đi cùng nhau nhất
        - Sử BFS (Breadth first search) và Hash tree structure để đếm các bộ item ứng viên một cách hiệu quả
        - Trình bày dữ liệu theo định dạng ngang (horizontal data format)
    3. Ứng dụng 
        - Phân tích giỏ hàng của khách hàng mua hàng tại 1 cửa hàng
        - Tìm kiếm các quy tắc trong miền điều hướng người dùng web (vd: khách hàng đã truy cập trang web A và trang B cũng đã truy cập trang C)
        - Khai thác dữ liệu chay rừng
    4. Lý thuyết của thuật toán Apriori
        - Có 3 thành phần phải quan tâm: support/ Confidence/ lift
            * Support: Để cập đến mức độ phổ biến mặc định của một mục (A) và có thể tính toán bằng cách tìm số lượng giao dịch có chứa một mục cụ thể đó 
            (A)/ Tổng số giao dịch
                + Support (A) = (Transactions containing (A))/ (Total transactions) [Miền giá trị từ 0 đến 1]
                Có nhiều thuật toán đó là số lần xuất hiện trên giao dịch
                + Confidence: đề cập đến khả năng một mặt hàng B cũng được mua nếu mặt hàng A được mua. => Nó được tính toán bằng cách tìm số lượng giao dịch trong đó
                A và B được mua lại với nhau/ Chia cho tổng số giao dịch A được mua
                => confidence (A->B) = Transaction containing both (A and B))/(Transactions containing A) [Miền giá trị 0,1]
                + Lift: Đề cập đến sự gia tăng tỉ lệ bán B khi A được bán 
                => lift (A->B) = (Confidence(A->B))/(Support(B)) => Tỉ lệ quan trọng miền giá trị [1 đến vô cùng]
                => Nếu xác xuất bằng 1 thì sẽ không phải có sự liên kết
                + Chú ý:
                    lift =1: Không có sự liên kết giữa sản phẩm A và B
                    lift >1: Sản phẩm A và B có khả năng được mua cùng nhau hơn
                    lift <1: Sản phẩm A và B không được mua cùng nhau
        - Ngoài ra
            * Leverage: tính toán sự khác biệt giữa 2 tần số quan sát của A và B xuất hiện cùng nhau
                => tần số được kỳ vọng nếu A và B độc lập
                => Leverage = 0: Thể tính độc lập
                + Levarage(A->B) = Support(A->B) - Support(A)*Support(B) [Miền giá trị: -1 đến 1]
            * Conviction: về mặt toán học, nó có thể được biểu diễn nhữ sau
                + Convition (A->B) = (1-support (B))/(1-confidence(A->B)) [Miền giá trị 0 đến vô cùng]
                => Tương tự như lift xác xuất mua A mà không mua B
        - Nếu mẫu lớn thì => support = 0.3
        - Nếu mẫu nhỏ thì phải chọn cho phù hợp support
        - Lift phải được lọc để xác định
    => Xác định được min support và confidence sao cho phù hợp với bài toán và giảm tốc độ mỗi bước
    5. Nguyên tắc
        - Trích xuất tất cả các tập con có giá trị support cao hơn ngưỡng tối thiểu
        - Chọn tất cả các quy tắc từ các tập con với giá trị confidence cao hơn ngưỡng tối thiểu
        - Sắp sếp các quy tắc theo thứ tự giảm dần của lift
    6. Nhước điểm
        - Có thể cần phải tìm một số lượng các quy tắc nên việc tính toán tốn kém
        - Tình toán hỗ trợ thực hiện trên toàn bộ dữ liệu và được lặp đi lặp lại thông qua tất cả các giao dịch mỗi lần
        - Yêu cầu không gian bộ nhớ lớn khi thực hiện với số lượng lớn các item tạo itemset
        - Thuật toán nặng nề khi có quá nhiều feature

'''

ECLAT = '''
    1. Giới thiệu
        - 
    2. Ứng dụng
        - Phù hợp với loại dữ liệu nhỏ
        - Mua sắm trực tuyến: giúp tìm ra sản phẩm thường xuyên được khách hàng mua trong cửa hàng
        - Phân tích hành vi người tiêu dùng trong web blog
        - Các ứng dụng được thực hiện với Apriori cũng có thể áp dụng trên ECLAT tuy nhiên trên bộ dữ liệu nhỏ và trung bình
    3. Thuật toán
        - Đi thứ tự theo từng item duyệt từ trên xuống dưới cho đén khi hết thui thành 1 list => TidList/ Support
        - Từ cơ sở dữ liệu
            * Transaction database: là một bộ transaction
            * Mỗi Transaction là một bô các item
            * tidList là danh sách các id của các transaction
        - Từ đó mới tính sao cho chuyển dạng tidlist
        - Tạo ra các itemset và nối dữ liệu rồi sau đó sub rồi bỏ đi
    4. Nhược điểm
        - Các bộ TID (TID-set) có thể khá dài vì thế tốn nhiều thời gian thao tác và tính toán
        
'''