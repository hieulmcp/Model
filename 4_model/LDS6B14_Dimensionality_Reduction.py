Dimensionnality_Reducition = '''
    1. Giới thiệu
        - Nhiều vấn đề về Machine learning liên quan hàng nghìn hoặc thậm chí hàng triệu tính năng/ thuộc tính cho mỗi cá thể huấn luyện
        => Điều này không chỉ làm việc đào tạo cực kỳ chậm mà còn có thể làm cho việc thực hiện trở nên khó hơn nhiều để tìm ra 1 giải pháp tốt
        - Giảm số lượng các tính năng đáng kể => Chuyển 1 vấn đề phức tạp thành 1 vấn đề có thể xử lý được
        => Giảm chiều dữ liệu đề làm được nhiều chuyện hơn
        - Nếu không gian quá nhiều chiều thì cần phải cân nhắc giảm chiều dữ liệu
        - Chọn nhứng thuộc tính quan trọng liên quan đến target của chúng ta
        - Ngoài ra việc tăng tốc đào tạo, việc giảm kích thước cũng vô cùng hữu ích cho việc trực quan hóa dữ liệu
    2. Ghi chú
        - Giám kích thước sẽ làm mất 1 số thông tin => Vì vậy mặc dù nó sẽ tăng tốc đào tạo, nó cũng có thể làm cho hệ thống của ta hoạt động kém hơn 1 chút
        - Vi vậy cho nên chúng ta cần đào tạo hệ thống với dữ liệu gốc trước khi cân nhắc việc sử dụng giảm kích thước nếu đào tạo quá chậm
        - Trong 1 số trường hợp việc giảm kích thước đào tạo có thể lọc ra một số nhiễu và chi tiết không cần thiết và do đó dẫn đến hiệu suất cao hơn 
        => Nhưng đa phân là không nó chỉ tăng tốc độ đào tạo
    3. Phân loại: có 2 loại giảm chiều hay nói tới
        - Projection (phép chiếu)
            * Giảm số chiều dữ liệu
            * Không phải luôn là một cách tiếp caabh tốt để dimensionlity reduction
        - Manifold
            * Tìm ra cơ sở low-D để mô tả dữ liệu high-D
            * Khám phá chiều nội tại (intrinsic dimensionality)
            * Lý do áp dụng Mainfold
                + Nén dữ liệu
                + Giảm chiều/ giảm nhiễu
                + Trực quan hóa/ Số liệu khoảng cách hợp lý
                + Nhưng: Manifold càng công ("curvier"), dữ liệu càng phải dày đặc
    4. Ứng dụng
        - Khám phá các mối tương quan/ Chủ đề ẩn (vd: Các từ thương đi cùng nhau)
        - Loại bỏ các tính năng dư thừa và nhiễu vì không phải tách cả các tính năng đều hữu ích
        - Giải thích và trực quan hóa
        - Lưu trữ và xử lý dữ liệu dễ dàng
    5. Một số thuật toán
         5.1. Linear
            * PCA - Principal component Ananlysis (Non-Parametric)
            * LDA - Linear Discriminant Analysis (Parametric(có tham số))
        5.2. Non linear
            * LLE - Local Linear Embedding
            * tSNE - T-distributed Stochastic Neighbor Embedding
    6. PCA và LDA
        6.1. PCA
            - Không quan tâm đến target
            - Nếu giảm chiều thì khi chiếu xuống thì các điểm sẽ trung lẫn nhau
            - Lúc đó phép chiếu này không quan tâm đến target
            => Trên 1 mặt phăng những mà chồng lên nhau giữa điểm xanh và đỏ
        6.2. LDA
            - Tìm ra 1 chiều maximising tìm tập dữ liệu x và y tìm 1 chiều khoog gian sao cho giữa các cụm và các điểm bên trong lớn nhất có thể có
            - Tách bạch 2 điểm xanh đỏ trên mặt phẳng nhưng khác nhau


'''

PCA = '''
    1. Giới thiệu PCA
        - PCS (principal component analysis): phân tích thành phần chính, là 1 thuật toán dimensionnality reduction phổ biến hiện nay
        - Thuộc nhóm: Unsupervised learning
        - PCA thực hiện việc tìm các hướng của phương sai tối đa maximum variable trong dữ liệu high-dimensional và chuyển vào một không gian
        con có chiều nhỏ hơn và giữ lại hầu hết các thông tin
        => Chỉ lấy trục x không lấy trục y nữa có nghĩa về cùng 1 mặt phảng nó thu hép thuộc tính lại không trải dài trên 2 trục x và y
        => Nó xát với x thì không cần quan tâm chiều con lại
    2. Mục tiêu
        - Mục tiêu chính của phân tích PCA là xác định các mẫu trong dữ liệu
        - PCA giúp phát hiện mối tương quan giữa các biến. Nếu có mối tương quan chặt chẽ giữa các biến tồn tại, nỗ lực giảm kích thước mới có ý nghĩa
        - Vector riêng và giá trị riêng
            * Vector riêng: đó là tọa độ
            * Giá trị riêng nó là 1 giá alpha => Thể hiện độ lớn của giá trị này
            => Nếu giá trị quá nhỏ thì sẽ lấy trọng số gần nó
    3. Nhược điểm
        - PCA không thể chỉnh hằng số
        - Các hướng có phương sai lớn nhất được giả định là quan trọng nhất
        - Chỉ xem xét các biến đổi trực giao của các biến gốc
        - PCA chỉ dựa trên vector trung bình và ma trận hiệp phương sai. Một số phân phối đặc trưng bởi điều này, nhưng 1 số khác thì không
        - Nếu có các biến tương quan, PCA có thể giảm kích thước
        - Nếu không PCA không giảm được kích thước
        => Nên dùng PCA khi nào và khi nào dùng thì tốt
    4. Ứng dụng
        - Trực quan hóa dữ liệu
        - Nếu ML quá chậm mà kích thước đầu vào quá cao thì việc sử dụng PCA để tăng tốc là một lựa chọn hợp lý
        - Nếu bộ dữ liệu và dung lượng ổ đĩa bị giới hạn, PCA cho phép tiết kiệm không gian để đổi lấy một chút thông tin của dữ liệu
        => Đây có thể là một sự cân bằng hợp lý
        - Nén dữ liệu => Sau đó xử lý hình ảnh rồi mới train dữ liệu
        - 2 vector nào quan trọng nhất năm bên trên nó quan trọng hơn
        - PCA cho phép người dùng để lấy bao nhiều chiều để được bao nhiêu %
'''

LDA = '''

'''

