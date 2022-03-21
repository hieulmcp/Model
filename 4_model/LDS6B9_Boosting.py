Boosting = '''
    1. Giới thiệu Boosting
        - Không liên quan gì đến thuật toán
        - Boosting hỗ trợ các mô hình ML để cải thiện độ chính xác của dự báo
        - Booting algorithm: thuật toán học tăng cường là một trong những thuật toán được sử dụng khá rộng rãi nhằm mục đích tăng cường thuật toán để cải thiện
        độ chính xác của mô hình
    2. Boosting là gì ?
        - Là thuật toán học quân thể bằng cách xây dựng nhiều thuật toán cùng 1 lúc (ví dụ như Decision Tree) và kết hợp lại chúng
        - Mục đích: Để có 1 cụm hoặc một nhóm các weak learner rồi kết hợp chúng lại để tạo ra một strong learner duy nhất
        - Weak learner phân loại với độ chính xác hầu như không cao
        - Strong leaner: phân loại với độ chính xác cao hơn
        => Là 1 kỹ thuật dựa trên model thuật toán nào đó để thực hiện và cải thiện model đó => Nó sẽ đi giải quyết đc cái sai của bước trước đó thế nào
        - 2 Vấn đề trong kỹ thuật boosting
            * Chọn tập dữ liệu nếu sai thì trọng số lơn hơn
            * Kết hợp các kết quả lại cái nào trọng số lơn hơn thì chọn nó => Kết quả alpha nào lớn hơn thì có trọng số đó để biết được nên chọn cái nào
            => Ý nghĩa boosting để tạo ra bộ dữ liệu mới cho bước sau đó, bộ liệu sai thì nâng lên
            => Vậy dự báo xong rồi mới học tăng cường để cái thiện thuật toán
    3. Cách hoạt động  ?
        Bước 1: Base learner lấy tất cả các phân phối và gán trọng số bằng nhau cho  mỗi quan sát
        Bước 2: Nếu có bất kỳ lỗi dự báo nào do base learning algorithm đầu tiên gây ra, thì ta sẽ chú ý cao hơn đến các quan sát có lỗi dự đoán
        => Sau đó ta áp dụng cho base learning algorithm tiếp theo
        Bước 3: Lặp lại bước 2 cho đến khi giới hạn của base learning algorithm đạt được hoặc đạt được đố chính xác cao hơn
        Bước 4: Cuối cùng => Kết hợp kết quả đầu ra từ weak learner và tạo thành một strong learner cải thiện sực mạnh dự đoán của mô hình
        => Boosting tập trung cao hơn vào các ví dụ bị phân lớp sai (mis-classified) hoặc có lỗi cao hơn bới các weak rule trước đó
    4. Phân loại: chia làm 2 loại Adaptive boosting (adaBoost) và Gradient Boosting (XGBoost)
        4.1. Adaboost
            - Adaboost là 1 kỹ thuật phân loại đồng bộ từ nhiều model phân loại
                => Kết quả đầu ra của nó là sự kết hợp kết quả đầu ra của các thuật toán phân loại
            - Thuật toán này tăng cường thích hợp => là 1 phương pháp chung để tạo ra một phân loại mạnh mẽ trong một tập hợp các phân loại yếu
            - AdaBoost là một kỹ thuật boosting phổ biến giúp ta kết hợp nhiều weak classifier thành strong classifier duy nhất
            - "Weak classifier" trình phân loại yếu: là 1 trình phân loại hoạt động kém những hoạt động tốt hơn so với việc dự đoán ngẫu nhiên
            - "Strong classifier" trình phân loại mạnh có độ chính xác cao hơn nhiều
                => Thường được sử dụng trong classifer SVM
            - Adaboost
                * Giúp chọn tập huấn luyện cho mỗi trình phân loại mới mà ta đào tạo dựa trên kết quả của trình phân loại trước đó
                * Xác định cần lựa chọn trọng số là bao nhiêu cho câu trả lời được đề xuất của mỗi phân loại khi kết hợp các kết quả
            4.1.1. Thuật toán adaboost
            - Bước 0: phân loại theo 2 lớp và chọn output: {-1, +1}
            - Bước 1: Fit model  classification đầu tiền H1(x)
                * Tính tổng lỗi, hệ số alpha (model performance)
                => Hệ số alpha nào lớn trên tổng thể thì phân ra cái nào đúng cái nào sai, số lượng sai thì tính được hệ số alpha của bước đầu
            - Bước 2: Lặp t=2 => m
                * Cập nhật được trọng số
                * Tạo tập dữ liệu mới dựa trên trọng số đã cập nhật
                * Fit mô hình classification 
                * Tính tổng lỗi hệ số alpha (model performance)
                => Cập nhật lại trọng số, đối với đúng thì trọng số thấp đi, và sai thì trọng số cao lên
                => lặp đi lặp lại cho đến khi m lần cho đến khi trọng số thấp đi nhất có thể
                => Tập trung vào dữ liệu sai, không quan tâm đến dữ liệu đúng nhiều và quan tâm đến alpha
            - Bước 3: 
                * Dự đoán cuối cùng là kết quả của các bước đã thực hiện nhân với alpha
                * Vì ban đầu được phân loại là  +1 hoặc -1, nên dấu của các dự đoán sau bước cuối là dự đoán cuối cùng bằng tổng các alpha cộng lại
        4.2. Gradien Boost
            - Thực hiện dự báo dựa trên nhiều lần chạy để khắc phục lỗi trước đó
            - Cứ cái thiện sao cho nó càng bám sát quá trình training => Để tránh overfitting => Learning rate: Để hội tụ tốt hơn hay không ?
    => Phải tìm hiểu thêm tunning parameter để chọn model phù hợp
        4.3. XGBoost
            - Định nghĩa: Phổ biến trong ML, thực hiện cho cả 2 công việc regression và classification
            - XGboost: một loại boosting cung cấp giải pháp tốt cho việc phối hợp với thuật toán cơ sở (mặc định là classification and regression trees CART)
            => Dựa trên ý tưởng của Fradien boost làm cốt lõi
            - Chạy trên mô hình phân tán => Kết hợp GPU nhiều máy với nhau
            - Tự động xử lý boosting missing data...
            - Tổ chức dưới dạng các cây
    => Quan trong Boosting là trong số => Classification cách kết hợp với model base để thực hiện sửa lỗi
    => Khi làm phải chủ ý đến tunning parameter để làm tốt thuật toán tốt hơn nhiều            
'''