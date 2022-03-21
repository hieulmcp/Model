cluster_analysis = '''
    1. Giới thiệu
        - Bài toán phân nhóm toán bộ dữ liệu X thành 1 nhóm nhỏ dựa trên sự liên quan giữa các dữ liệu trong mỗi nhóm
        - Mục tiêu: Tổ chức các item vào 1 nhóm
        => Phân cụm lại xem thế nào ? Kiểm chứng thao tác đó
    2. Ứng dụng
        - Phân nhóm khách hàng vào các nhóm
        - Phân loại các mẫu thời tiết khác nhau cho một vùng
        - Nhóm các bài viết tin tức vào 1 chủ đề
        - Khám phá các điểm nóng tội phạm
        => Trình bày phân ra bao nhiêu cụm, đặc thù của cụm
    3. Ý nghĩa
        - Chia dữ liệu vào các cluster
        - Các item tương tự được nhóm vào cùng 1 cluster
        - Có 2 sự khác biệt
            * Intra-cluster-khoảng cách giữa các điểm trong nhóm: tối thiểu
            * Inter-cluster-khoảng cách giữa nhóm này và nhóm kia: tối đa
        - Cách tính khoảng cách có 3 cách tính khoảng cách
            * Euclidean distance: khoảng cách giữa 2 điểm A và B so với điểm trung tâm của tập dữ liệu
            * Manhattan distance: khoảng cách cạnh huyển tọa độ 2 điểm 
            * Cosine similarity: khoảng cách giữa gốc tọa độ giữa 2 điểm
        - Chuẩn hóa các biến input => giá trị có thể được chia tỉ lệ => Phải scaler dữ liệu để về chung trọng số trc khi làm
    4. Ghi chú
        - Không có khái niệm cluster đúng
        - Cluster không có nhãn hay không có target
        => Giải thích và phân tích cần thiết để tạo các kết quả phân cụm có ý nghĩa
        => Giải thích được các nhóm đó phù hợp và những đặt tính gì để chia ra
    5. Sử dụng kết quả phân cụm
        - Phân đoạn dữ liệu: Phân tích từng phân đoạn có thể cung cấp insight
        - Các category để phân loại dữ liệu mới: Mẫu mới được gán cho cụm gần nó nhất
        - Dữ liệu được gán nhãn để phân loại: Các mẫu cụm được sử dụng như dữ liệu có gán nhãn
        - Là cơ sở cho việc phát hiện bất thường: Các cụm outline là bất thường
    6. Những thuật toán chính trong cluster analysis
        - K-Means clustering
        - Hierarchical clustering
        - GMM
    7. Bài toán phân cụm
        - Phân cụm khách hàng
        - Phân biện hình ảnh
        - GMM dùng để tìm ra những điểm khác biệt
    => Mỗi thuật toán sẽ cho các bộ khác nhau cho nên cần xem xét kỹ trước khi sử dung cho phù hợp bài toán
    
'''

Kmeans_clustering = '''
    1. Giới thiệu
        - Được sử dụng khi ta có dữ liệu không gán nhãn
    2. Ý tưởng
        - Tìm các nhóm trong dữ liệu với số lượng nhóm được đại diện bởi k
        - Thuật toán được lặp lại để gán mỗi điểm dữ liệu vào một trong các nhóm k dựa trên các tính năng được cung cấp
        - Các điểm dữ liệu được phân cụm dựa trên sự tương tự về tính năng
        - Kết quả của thuật toán k-means:
            * Các trung tâm centroid của các cụm k có thể được sử dụng gán nhãn dữ liệu mới
            * Các nhãn cho training data: mỗi điểm dữ liệu được gán cho 1 cụm duy nhất
    3. K-means Algorithm
        - Lựa chọn k centroid ban đầu (cluster center)
        - Lặp:
            * Gán từng mẫu vào centroid gần nhất
            * Tính toán trung bình của các cluster để xác định centroid mới
        - Cho đến khi: đạt được tiêu chí dừng
        Bước 1: Biết được bao nhiêu nhóm cần chia để tính centroid
        Bước 2: Giựa trên khoảng cách gần với centreid gần nhất để về nhóm đó
        Bước 3: Cập nhật lại trung tâm của nhóm để có trung tâm mới
        Bước 4: Lặp cho đến khi tìm các centroid khoảng cách không thay đổi với điểm dữ liệu
    4. Các vấn đề cần lưu ý
        - Chọn các centroid ban đầu
            * Vấn đề: Các cluster cuối thường nhạy cảm với các centroid ban đầu
            * Giải pháp: Chạy kmeans nhiều lần với các centroid ban đầu ngẫu nhiên khác nhau => chọn kết quả tốt nhất
        - Tính toán kết quả cluster
            * error: Khoảng cách giữa sample và centroid
            * squared error: error^2
            * Tính tổng các squared error giữa tất cả các sample và centroid
            => Tính tổng trên tất cả các cluster => WSSE-Within-Cluster Sum of Squared Error => Khoảng cách các điểm đến trung tâm của nó gọi là 1 độ đo error
        - Chọn giá trị k => sử dụng Elbow method để chọn k => cứ k nào tạo ra góc cụi chỏ thì chọn khi thay đổi k thì WSSE phải thay đổi nhỏ dần với error
        => Chon k nào mà giảm được error giảm cao nhất có thể
        - Elbow method: 
            * Tư tưởng của phương pháp K-means là định nghĩa là cụm sao cho tổng biến thiên bình phương khoảng cách trong cụm là nhỏ nhất, tham số này là WSS (within cluster sum of square)
            * Elbow method chọn số cụm k sao cho khi thêm vào một cụm khác thì không làm cho WSS thay đổi nhiều
            * Quy trình triển khai Elbow method như sau:
                + Triển khai thuật toán kmeans với các số cụm k thay đổi từ 2 đến 10
                + Với mỗi giá trị k, tính giá trị WSS
                + Vẽ Elbow curve theo các giá trị k
                + Dựa vào Elbow curve chọn số k thích hợp, là vị trị khúc cua hay củ chỏ
            * Điều kiện dừng
                + Việc lặp sẽ dừng khi không có sự thay đổi của các centroid
                + Số lượng mẫu thay đổi cluster dưới ngưỡng (threshold)
            * Diễn giải kết quả
                + Kiểm tra các cluster centroid: các cụm khác nhau như thế nào ? => So sánh các centroid để thấy sự khác biệt của các cluster
                + Từ các nhóm này cả thì phải xây dựng nó giải thích được mục đích của chúng diễn đạt nó
                + Dựa trên trung tâm nhóm dữ liệu để đưa ra quyết định, dựa trên các thuộc tính để đưa ra tính chất... => Để đưa ra giải thích tốt nhất
            * Kết luận
                + Thuật toán k-means để phân tích cluster
                + Đơn giản dễ hiểu và thực hiện có hiệu quả
                + Giá trị của k cần phải được xác định
                + Các cluster cuối cùng thường nhạy cảm với các centroid ban đầu
                => Đánh giá lại với thực tế xem thuật toán mình đngs không
            * Nhược điểm
                + Kho khăn khi dự đoán số lượng của các cluster (giá trị k)
                + Các phân vùng ban đầu khác nhau có thể dẫn đến các cụm cuối cùng khác nhau
                + Tứ tự của dữ liệu sẽ tác động đến kết quả cuối cùng
                + Nhạy cảm với việc thay đổi kích thước: thay đổi bộ dữ liệu chuẩn hóa sẽ thay đổi kết quả hoàn toàn
                + Hoạt động không tốt với các cụm (trong dữ liệu gốc) có kích thước và mật độ khác nhau
                => Dùng hết toán bộ model rồi sau xem lại model nào tốt thì lấy model đó
    7. Shihouette score là gì ?
        - (b-a)/max(a,b)
            + a: trung bình khoảng cách của các điểm trong 1 nhóm
            + b: trung bình khoảng cách giữa các nhóm
    8. Euclidean => tổng sai số của các điểm, tìm tổng sai số thấp nhất
        - Khoảng cách trung tâm điểm của các nhóm =>  Khoảng cách các điểm đển các điểm trung tâm
        
'''

Hierarchical_clustering = '''
    1. Dendrogram
        - Là một sơ đồ cây thường được sử dụng để minh họa cho sự sắp xếp của các cụm được tạo ra bới hierarchical clustering
        - Có bao nhiều mẫu thì chia bấy nhiêu mẫu => Có 2 cách chia từ trên xuống dưới hoặc từ dưới lên trên
        - Tìm 2 mẫu gần nhau nối với nhau thì nối nhau cho đến khi chỉ con lại 1 cụm
        - Nó giúp chung ta thấy được tại sao chúng ta chia cụm vì sao lại chia cụm như vậy
    2. Chỉ tiêu tính khoảng cách (Cluster distance measure)
        - Single linkage: min của 2 điểm 
        - Complete linkage: max của 2 điểm
        - Average linkage: Trung bình của 2 điểm
        - Ward's method:  Tìm điểm trung bình của những điểm 
        - Khoảng cách: manhattan; euclidean
        - Công việc chính ở đây tính proximity giữa 2 cluster
            * Có thể tính khoảng cách các điểm theo Euclidean, Manhattan, Cosine similarity distance
    3. Các bước thực hiện - Agglomerative Clustering Algorithm
        Bước 1: Tạo n cluster, mỗi cluster cho 1 data point
        Bước 2: Tính toán poximity Matrix
        Bước 3: Lặp lại
            - Gộp cluster gần nhau nhất
            - Cập nhật Proximity matrix
        Bước 4: Cho đến khi còn một cluster
        Bước 5: Khi một cụm được tạo thành, các dendrogram được sử dụng để chia thành nhiều cụm tùy vấn đề
        => Cách chon k sao cho phù hợp đó cách nhìn của người làm và giải thích được nó
'''

Gaussian_mixture_model = '''
    - Đối với những điểm không rảnh giới rật ròi nên xin thêm thuất toán này
    - Cluster => Kmeans => yes/no và không có điểm xác xuất
    1. Giới thiệu về GMM
        - Là mô hình xác xuất giả định là tất cả các điểm dữ liệu được tạo ra từ một hỗn hợp của một số hữu hạn của các phân phối
        Gaussian với các tham số không xác định
        - Các kiến thức liên quan
            * Phương pháp gaussian distribution hoặc normal distribution và vấn đề phân cụm
            * Cách tiếp cận tổng thể của GMM
            * Đào tạo model đòi hỏi phải sử dụng một thuật toán rất nỗi tiếng gọi là thuật toán tối đa hóa kỳ vọng EM (Expectation-Maximization)
    2. Phân phối chuẩn: hội tụ các thuộc tính về phân phối chuẩn => Hướng đến 1 phân phối chuẩn
        - 68% tính chất phân phối chuẩn để giải quyết phân outlier
        - Trung tâm của dữ liệu
        - Độ lệch chuẩn => Đo mức độ phân tán của dữ liệu và mực đó phân tán dữ liệu
        - min: Điểm trung tâm, xích ma là độ lêch chuẩn là 2 đại lượng chính của phân phối chuẩn
    3. GMM
        - Quan sát dữ liệu
            * Chắc chắn có thể nhóm các dữ liệu tạch bật thì kmeans sử dụng khá tốt => Kmean nó rất ròi
            * Khi tập dữ liệu chòng lấn lên nhau 
                => Dựa trên xác xuất để phân định xem điểm đó thuộc cụm nào (điểm trung tâm và xích ma là đô lệch chuẩn bao nhiêu)
    4. EM
        - Làm sao đi tìm xích mà và phân phổi chuẩn làm sao cứ 1 điểm trong này sẽ như thế nào
        - Khởi tạo bắt đầu theo min và xích mà bất kỳ => Nó cứ tìm min và xích ma liên tục
        - Xác xuất là % thuộc về lớp 1 và bao nhiêu % thuộc về lớp 2
        => Dựa trên hướng của sự phân tán dữ liệu
    5. Khuyến điểm 
        - Khi không có đủ dữ liệu cho mỗi hỗn hợp (mixture) việc ước lượng ma trận hiệp phương trở nên khó khăn
        - Khoảng cách đo lường hoàn toàn ngẫu nhiên
        - Không đảm bảo sự tối ưu hoặc hội tụ
    6. Giải thích sao cho phù hợp
        - Dựa trên min, variance, xích ma để giải thích trọng số của các group được chia

'''