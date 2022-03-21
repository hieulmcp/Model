Handling_Imbalanced_Dataset = '''
    1. Đặt vấn đề
        - Bạn đang làm việc trên tập dữ liệu. Bạn tạo ra 1 mô hình phân loại (classification model) và nhận được độ chính xác 90% ngay lập tức. 
        Tốt quá, nhưng đến khi bạn hiểu sâu hơn một chút thì phát hiện ra rằng 90% dữ liệu thuộc về một lớp. Rồi xong ???!!!    
        => Đây là 1 ví dú về dữ liệu mất cân bằng và kết quả mà nó có thể gây ra
        - Giả sử bạn đang làm việc tại 1 công ty và bạn được yêu cầu tạo một mô hình, dựa trên các phép đo khác nhau theo ý của bạn, 
        mô hình sẽ dự đoán liệu sản phẩm có bị lỗi hay không. Bạn quyết định sử dụng trình phân loại yêu thích của mình huấn luyện cho nó trên dữ liệu và thật tuyệt: 
        bạn có độ chính xác 96.2 %
        - Sếp của bạn ngạc nhiên và quyết định sử dụng mô hình của bạn mà không cần kiểm tra thêm. Vài tuần sau anh ta 
        vào văn phòng của bạn và cho bạn một trận vì sự vô dụng của mô hình bạn đã làm. Sự thật là, mô hình của bạn tạo ra 
        không tim thấy bất kỳ sản phẩm bị lỗi nào kể từ khi nó được sử dụng trong sản xuất. Sau khi kiểm tra lại, 
        bạn phát hiện rằng chỉ có khoảng 3.8% sản phẩm do công ty của bạn sản xuất bị lỗi và mô hình của bạn luôn trả lời không bị lỗi, 
        dẫn đến độ chính xác 96.2%. Các kết quả mà bạn thu được là do bộ dữ liệu không cân bằng mà bạn đang làm việc. Ác mộng ????!!!
    2. Khi làm việc với dữ liệu cần chú ý
        - Phân loại là một trong những vấn đề machine learning phổ biến nhất. Cách tốt nhất để tiếp cận bất kỳ vấn đề phân loại là bắt đầu bằng việc phân tích và 
        khám phá bộ dữ liệu - Exploratory Data Analysis (EDA). Mục đích của công việc phân tích và khám phá dữ liệu là tạo ra càng nhiều insight và 
        thông tin về dữ liệu càng tốt. EDA cũng được sử dụng để tìm ra các vấn đề có thể tồn tại trong bộ dữ liệu
        - Một trong những vấn đề phổ biến được tìm thấy trong các bộ dữ liệu được sử dụng để phân loại là vấn đề về các lớp không cân bằng (imbalanced classes)
        - Nếu thuộc tính categorical có tính chất phân loại thì phải xem mức độ cân bằng dữ liệu không ? Nếu chêch lệch mất cân bằng thì phải xử lý nó.
    3. Mất cân bằng dữ liệu (Data imbalance) là gì ?    
        - Mất cân bằng dữ liệu thường phản ánh sự phân phối không đồng đều của các lớp trong một tập dữ liệu
        - Ví dụ: Trong 1 bộ dữ liệu phát hiện gian lận thẻ tín dụng, hầu hết các giao dịch thẻ tín dụng không phải là gian lận và rất ít là gian lận. 
        Đều này khiến chúng ta có tỷ lệ chênh lệch lớn (50:1, 1000:1...) giữa không gian lận: gian lận
    4. Cách để xem dữ liệu có mất cân bằng hay không ?
        - Như chúng ta có thể thấy, các giao dịch không gian lận vượt xa các giao dịch gian lận. 
        Nếu chung ta đào tạo 1 mô hình phân loại nhị phân mà không khăc phục vấn đề này, mô hình hoàn toàn sai lệch. 
        Nó cũng tác động đến mối tương quan giữa các tính năng trong dataset.
        - Trực quan hóa dữ liệu là một cách để xem có mất cân bằng dữ liệu không ?
        - Ví dụ: Bạn có thể có vấn đề phân loại 2 lớp (nhị phân ) với 1000 trường hợp (dòng).
        Tổng cộng có 800 trường hợp được gắn nhãn Class-1 và 200 trường hợp còn lại được gắn nhãn Class-2. 
        Đây là một bộ dữ liệu không cân bằng và tỷ lệ của các trường hợp Class-1 và Class-2 là 800:200 (hoặc 4:1)
    5. Mất cân bằng là một vấn đề phổ biến
        - Hầu hết các tập dữ liệu phân loại không có số lượng mẫu chính xác bằng nhau trong mỗi lớp, nhưng 1 sự chêch lệch nhỏ thường không quan trọng
        - Có những vấn đề mà sự mất cân bằng giữa các lớp rất phổ biến, hiễn nhiên
        - Khi có sự mất cân bằng lớp 4:1 như ví dụ trên => Có thể gây ra vấn đề
        - Có thể chấp nhận mất cân bằng những tỉ lệ nhỏ
    6. Nghịch lý chính xác (Accuracy Paradox)
        - Nghịch lý chính xác là tên gọi của trường hợp đo lường độ chính xác có kết quả chính xác tuyệt vời (ví dụ 90%), 
        nhưng độ chính xác này chỉ phản ánh cho một lớp, mà không phải là tất cả
        - Nó rất phổ biến, bởi vì độ chính xác phân loại thường là thước đo đầu tiên chung ta sử dụng khi đánh giá các mô hình phân loại
    7. Chiến thuật làm việc với dữ liệu mất cân bằng (Handling Imbalanced Dataset)
        Chiến lược 1: Thu thập thêm dữ liệu được khuyến khích sử dụng 
            - Đây là việc nên làm nhưng hầu như luôn bị bỏ qua
            - Hãy đặt cho mình câu hỏi: "Liệu có thể thu nhập thêm dữ liệu về vấn đề của mình không ?" => Dành thời gian suy nghĩ và trả lời câu hỏi này
            - Một tập dữ liệu lớn hơn có thể cho thấy một quan điểm khác biệt và có lẽ cần bằng hơn về các lớp
            - Chiến thuật cao nhất và mang lại hiệu quả cao nhất
            - Kinh phí và thời gian để thu thập dữ liệu rất tốn
        Chiến lược 2: Thay đổi performance Metric
            - Độ chính xác không phải là số liệu được dùng khi làm việc với bộ dữ liệu không cân bằng. Bới vì nó bị sai lệch
            - Có những số liệu đã được thiết kế để cho chúng ta biết cách chân thực hơn khi làm việc với các lớp không cân bằng
            - Có 2 phương pháp để thay đổi lượng chính xác của model
                a. Confusion Matrix:
                    * Phân tích các dự đoán bằng 1 bảng hiển thị các dự đoán chính xác (trên đường chéo) và các loại dự báo không chính xác 
                    ( các lớp dự đoán không chính xác đã được chỉ định)
                        + Precision: thước đo độ chính xác của phân loại
                        + Recall: Thước đo tính đầy đủ của phân loại
                        + F1 score (F-score): Trung bình của precision và recall
                        + Cách tốt và đơn giản thường được sử dụng khi xử lý vấn đề phân loại là confusion matrix. 
                        Số liệu này cung cấp một cái nhìn tổng quan thú vị về việc một mô hình đang hoạt động tốt hay không. 
                        Vì vậy nó là khời đầu tuyệt vời cho bất kỳ đánh giá mô hình phân loại
                        + Ý nghĩa công thức
                            1. Độ chính xác của mô hình về cơ bản là tổng số dự đoán đúng chia cho tổng số dư đoán
                            2. Độ chính xác (precision) của một lớp xác định mực độ tin cậy là kết quả khi mô hình trả lời một điểm thuộc về lớp đó
                            3. Recall của một lớp thể hiện mức độ tốt của mô hình có thể phát hiện lớp đó
                            4. F1-score của một lớp được tính bằng (2 x precision x recall)/(precision + recall),
                            nó là kết hợp precision và recall của một lớp trong một metric
                        + Đối với một lớp nhất định, các kết hợp recall và precision khác nhau có các ý nghĩa sau
                            1. High recall + High precision: lớp được xử lý hoàn hảo bởi mô hình
                            2. Low recall + High precision: mô hình có thể không phát hiện tốt lớp nhưng rất đáng tin cậy khi nó thực hiện
                            3. High recall + Low precision: Lớp được phát hiện tốt nhưng mô hình cũng bào gồm các điểm của các lớp khác trong đó
                            4. Low recall + Low precision: lớp được xử lý kém bới mô hình
                    b. ROC curves
                        + Giống như precision & recall, độ chính xác được chia thành độ nhạy (sensitivity) và 
                        độ đặc hiệu (specificity) và các mô hình có thể được chọn dựa trên ngưỡng cân bằng của các giá trị này
                        + Ý nghĩa của công thức
                            1. Hầu hết các phân loại tạo ra một điểm số, sau đó so với ngưỡng (theshold) để quyết định phân loại. 
                            Nếu 1 bộ phân loại tạo ra điểm số giữa 0.0 (chắc chắn nó là negative) và 
                            1.0 ( chắc chắn là positive với thông thường coi mọi thứ > 0.5 là positive)
                            2. Tuy nhiên bất kỳ ngưỡng nào cũng được áp dụng cho bộ dữ liệu (trong đó PP là positive population và NP là negative population) 
                            sẽ tạo ra true positive (TP), False positive (FP), true negative (TN) và false negative (FN). 
                            Chúng ta cần 1 phương pháp sẽ tính đến tất cả những con số này
            - Lấy mẫu lại bộ dữ liệu (Resampling Dataset)
                    a. Sau khi sử dụng Confusion matrix và ROC curver thấy không phù hợp thì chúng ta phải xem lại dữ liệu và 
                    có thể xem lại yêu cầu bài toán hoặc áp dụng 1 thuật toán khác
                    b. Chung ta có thể thay đổi tập dữ liệu mà ta sử dụng để xây dựng mô hình dự đoán để có dữ liệu cần bằng hơn
                    c. Thay đổi này gọi là lấy mẫu dữ liệu và có hai phương thức chính mà chúng ta có thể sử dụng
                        1. Thêm các bản sao của các thể hiện từ lớp đại diện dưới mức (under-represented class) được gọi là over-sampling 
                        (hoặc lấy mẫu hơn chính thức với sự thay thế)
                        2. Có thể xóa các thể hiện khỏi lớp được đại diện quá mức (over-represented class) được gọi là oversampling
                    d. Lấy dữ liệu giả lâp từ thư viên để làm giả lập cho cân bằng dữ liệu
                    e. Những cách tiếp cận này thường rất dễ thực thi và nhanh chóng thực thi => Đây cũng là giải pháp khởi đầu tốt
                    f. Trên thực tế, chung ta nên sử dụng cả 2 cách tiếp cận trên cho tất cả các bộ dữ liệu mất cân bằng, 
                    để xem liệu nó có giúp chung ta tăng cường các đo lường chính xác không
            - Một số nguyên tắc
                    a. Cân nhắc kiểm tra việc lấy mẫu under-sampling khi có nhiều dữ liệu (hàng chục hoặc hàng trăm nghìn trường hợp trở lên)
                    b. Cân nhắc kiểm tra việc lấy mẫu over-sampling khi không có nhiều dữ liệu (hàng nghìn trường hợp hoặc ít hơn)
                    c. Xem xét thử nghiệm các scheme lấy mẫu ngẫu nhiên (random) và không ngẫu nhiên ( non-random) (VD: Phân từng)
                    d. Xem xét thử nghiệm các tỷ lệ mẫu khác nhau (VD: ngoài tỷ lệ 1:1 trong bài toán phân loại nhị phân, hãy thử các tỉ lệ khác)
            - Thử các thuật toán ML khác nhau
                    a. Không nên sử dụng thuật toán yêu thích của mình cho mọi vấn đề. Ít nhất chung ta nên kiểm tra cùng lúc 
                    (Spot checking) nhiều loại thuật toán khác nhau cho một vấn đề nhất định
                    b. Gợi ý: Decision - cây quyết định thường hoạt động tốt trên các bộ dữ liệu mất cân bằng. 
                    Các quy tắc phân tách dựa vào biến lớp được sử dụng trong việc tạo cây, có thể ràng buộc các lớp được sử lý. 
                    Cũng có thể sử dụng Random Forest trong trường hợp này









'''