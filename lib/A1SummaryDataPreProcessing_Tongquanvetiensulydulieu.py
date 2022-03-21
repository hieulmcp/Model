Note = '''
    1. Quy trình về xử lý dữ liệu
        Step 1 Business understanding
            - Xác định được yêu cầu bài toán
            - Hiểu nghiệp vụ cần thiết tốt nhất tìm hiểu
            - Lấy ý kiến chuyên gia
        Step2 Data understanding
            - Dữ liệu đã phù hợp với nhu cầu chưa?
            - Thêm bớt dữ liệu thuộc tính thế nào ?
            - Ý nghĩa của các thuộc tính ra sao ?
        Step3 Data prepretion
            - Vận hành các thao tác để xử lý lỗi và chuẩn hóa dữ liệu
            - Xử lý missing value và outlier không hợp lệ
            - Thêm thông tin
        Step4 Modeling
            - Phối hợp dữ liệu đã chuẩn hóa và thuật toán machine learning để build model phù hợp
        Step5 Evaluation model
            - Kiểm chứng model đã đáp ứng được yêu cầu của bài toán chưa ?
            - Nếu đúng thì bước tiếp theo
            - Nếu sai thì quay lại xem xét lại tìm hiểu các bước trước
        Step 6 Deployment
            - Kết hợp dữ liệu để cho khách hàng có thêm lựa chọn khác
            - Xem dự án có thể mở rộng thêm sau này không
    2. Tại sao lại tiền xử lý dữ liệu ? Nó cực kỳ quan trọng trong làm data science
        - Tìm ra bất thường của dữ liệu để xứ lý cho phù hợp với dữ liệu bài toán
        - Các loại dữ liệu thường được xử lý
            * Dữ liệu thường không chính xác (inaccurate data)/ Dữ liệu bị thiếu (missing data) or thuộc tính thuộc dữ liệu tổng hợp không mang nhiều ý nghĩa
            * Dữ liệu bị nhiễu (noisy data) dữ liệu bị sai ngoai lệ (outlier)
            * Dữ liệu không nhất quán (Inconsistent data) dữ liệu bị trùng lặp, do người nhập liệu, vi phạm các ràng buộc về dữ liệu
            * Các phương pháp thu thập dữ liệu thường được kiểm soát lỏng lẻo, dẫn đến các giá trị ngoài phạm vi outlier
    3. Mức độ ảnh hưởng không xử lý dữ liệu
        - Kết quả dự báo sai lệch hoàn toàn => Không dùng được model hoặc không thể làm dự báo
    4. Quy trình về pre-processing
        4.1 Quy trình chung
            - Step1: Dữ liểu thô tiềm ẩn các lỗi bên trong
            - Step2: Apply pre-processing vận dụng các chức năng nhiệm vụ để xử lý các lỗi tiềm ẩn bên trong
            - Step3: Prepared-data dữ liệu đã được xử lý
            - Step 4: Xử lý lại vòng lặp nếu chưa xử lý được hết các lỗi tiềm ẩn bên trong
        4.2 Các bước thực hiện trong pre-processing
            Step 1-Import thư viện
                - Khi nào cần dùng thì import vào
            Step 2-Đọc dữ liệu và lựa chọn các thuộc tính cần thiết
               - Hàm đọc các loại file khác nhau cần làm 1 thư viện
               - Sau khi đọc xong thì phải là 1 dataframe
               - Thuộc tính đọc vào (input) nên lựa chọn phù hợp => Nên lựa chọn các thuộc tính không liên quan đến bài toán bỏ ra ngoài
            Step3-Kiểm tra dữ liệu thiếu (Missing value)
               - Không chỉ giá trị null và những giá trị về dữ liệu thiếu
               - Ảnh hưởng rất lớn về dự đoán bài toán theo yêu cầu
            Step4-Kiểm tra dữ liệu phân loại
                - Phải chuyển các biến phân loại qua số vì các thuật toán đều làm việc với dữ liệu số
                - Một số các chuyển đổi: Label endoder, Binary Encoder, one hot code endoder
            Step5-Chuẩn hóa dữ liệu (Data standardizing)
                - Tập dữ liệu đầu thường chỉ chứa các thuộc tính số và do đó có thể cần phải chia tỷ lệ (Feature scaling) cho các thuộc tính 
                trong dữ liệu trước khi thực hiện công việc tiếp theo như PCA, Kmeans...
                - Chia tỉ lệ theo phương pháp giới hạn nhập vi của các thuộc tính để chung có thể được so sánh dựa trên các căn cứ chung. 
                Một số cách để chia tỉ lệ là Standard Scaler, Min - max scaler...
            Step 6-Chuyển đổi dữ liệu
                - PCA tranformation giảm kích thước chiều không gian tính năng trong khi vẫn giữ lại các thông tin cần thiết
                - Chuyển đổi dữ liệu sao cho mức độ tương quan biến input và output phụ thuộc với nhau
            Step 7-Chia dữ liệu
                - Chia dữ liệu Training và testing
                - Xem mức độ cần bằng dữ liệu nếu biến output là biến categorical
'''