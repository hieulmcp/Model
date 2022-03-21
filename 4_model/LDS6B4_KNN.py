KNN_K_NEAREAST_NEIGHBORS = '''
    1. Giới thiệu
        - KNN là 1 thuật toán thuộc nhóm supervised learning được sử dung trong bài toán classification và regression
            * Với classification, Output là class dữ trên KNN trong tập training data
            * Với regression, output là trung bình các giá trị của target variable dựa trên KNN trong training data
    2. Ứng dụng
        - Phân loại classification
        - Tìm các giá trị bị thiếu missing value
        - Nhận dạng mẫu pattern recognition
        - Xác định biểu hiện gen (gene expression)
        - Dự đoán protein 
        - Tìm cấu trúc 3D của protein
        - Đo lường tương tự của tài liệu => Tìm kiếm tài liệu tương tự về nghĩa từ
    3. Ý tưởng
        - Các điểm dữ liệu được phân loại và khi xác định loại của một điểm dữ liệu mới, K điểm gần nhất được sử dụng trong quá trình này
        - Dựa trên giá trị của K mà việc phân loại cho điểm dữ liệu có thể thay đổi
        - Từ các điểm gần nhất theo số phân tử k để tính giá trị cho biến dự đoán regression
        - Về classification thì cũng tương tính distance rôi sau đó classification nào gần hơn thì lấy biến phân loại đó
    4. Vấn đề
        - K bằng bao nhiêu ?
        - Cứ mỗi lần giá trị dự bào thì cần làm gì ?
            Bước 1: Tìm khoảng cách
            Bước 2: Tìm khoảng cách gần nhất
            * Đây là model lazy => Không có tổng quan được cứ mỗi lần như vậy thì đi tìm khoảng cách/ sắp sếp và đi tìm điểm gần nhất
            * Có 2 cách lấy theo trung bình hay trọng số
                + Nếu không lấy trọng số thì lấy trung bình
                + Lấy trọng số thì lấy theo bài toán tối ưu nó turning parameter nó, khoảng cách càng nhỏ thì trọng số càng cao
        - Ghi chú
            * Min-max normalization có thể được sử dụng để chuyển một giá trị v của một cột thuộc tính số A thành v' trong khoảng [0,1]
            v' = (v-mina)/(maxa-mina)
            * Phải scaling trc khi thực hiện model
            * k càng nhỏ thì sẽ tạo ra overfitting => sẽ rất nhạy cảm với nhiễu
            * Bảo tồn được vùng của chúng: chọn k cho dữ liệu số mẫu lớn: k = sqrt(mẫu)/2
    5. Nhược điểm
        - Gặp kho khăn trong việc tìm k thích hợp
        - Thay đổi k có thể thay đổi kết quả các lớp của dữ liệu
        - Độ chính xác của KNN có thể bị suy giảm nghiêm trọng với dữ liệu kích thước cao do có rất ít sự khác biệt giữa hàng xóm gần nhất 
        và xa nhất => Có nhiều feature mà chỉ đỏ và xanh gần nhau quá và lộn xộn thì tìm sẽ không dễ đúng/ mất cần bằng dữ liệu
        - KNN có thể bị phân phối lớp lệch
            * 1 lớp chiếm ưu thế trong tập huấn luyện, chiếm ưu thế hơn trong việc bỏ phiếu quyết định mẫu mới (số lượng lớn hơn = phổ biến hơn)

    Note: Scaler trước khi làm model => Công đoạn sửa dữ liệu => Scaler nếu có => Predict
        - Khi nói đến trung bình giá trị trung tâm của dữ liệu => xem tập dữ liệu sample => TB, std, sai biệt trong model
        - Phải chạy nhiều lần để xem mức độ ổn định của score => lấy ra được giá trị trung bình mới gọi là sự phù hợp của model
        - Phải xem lại mực độ phù hợp của mô hình xem thế nào => Với cần phản xây dựng mô hình phù hợp với bài toán đặt ra => Sẽ chọn score test cao nhất
        - Tối ưu tham số cho 1 mô hình
        - Cross vadiation => Dùng để chạy dữ liệu chia bộ dữ liêu ra để thực hiện xem tính ổn đỉnh của dữ liệu cũng như mô hình
        - Khi quan tâm đến model thì phải quan tâm đến trả giá như thế nào hiệu giữa training và test và thơi gian
        - Lướt qua mô hình đã biết, sau đó tăng hơn nữa bằng cách para turning theo dạng tổng => Truyền trong danh sách rồi đi kiểm tra 
        => Cách làm thử hết các mô hình để hiểu chỉnh mô hình sao phù hợp
        - n_neight = thường sẽ số lẽ vì nó liên quan đến vote sẽ là số lẽ để dễ quyết định
'''  