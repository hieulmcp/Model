Classification = '''
    1. Mục tiêu: Dự đoán target là biến phân loại từ biến input đầu vào
    2. Phân loại
        - Binary Classification: target chỉ có 2 biến phân loại => True/False quan tâm đến true nhiều hơn
        - Multi-class Classification: Target có nhiều giá trị-value
    3. Đặc điểm chính
        - Tìm các tham số từ bộ mẫu
        - Từng bước tìm ra được hàm tối ưu nhất
    4. Xây dựng và áp dụng model
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

Danh_gia_mo_hinh_Classification = '''
    1. Một số kỹ thuật
        - Đánh giá được sự phụ hợp giữ y dự đoán và y thực tế
        - Sử dụng các thang đo trực quan
    2. Các thang đo mô hình classification - Binary classification
        a. Confusion maxtrix
            - Dữ liệu thực có 2 giá trị 0, 1
            - Dữ liệu dự đoán 2 giá trị 0, 1
        b. Accuracy score
            - model.score = (TN + TP)/(TN + FP + TP + FN)
            - Predict: mực độ dự báo trên biên phân loại  dự báo xem mức độ đúng bao nhiêu
            - Recall: Tính đầy đủ của thực tế so với dữ liệu
            => 2 Chỉ số predict, recall thì xem lại mức độ chính xác và tính đầy đủ giúp khắc phục sự thiếu sót của dữ liệu
            - Cân đối 2 thang đo Predict và recall có thêm thang đo F1 score
            - F1 score = 2 * precision * recall/(precision + recall)
            - TPR, FPR, FNR, TNR so sánh với thực tế
            - Sensitivity (recall) độ nhạy & Specificity độ đặc hiệu bằng 1-FPR so sánh với thực tế
    3. Quan tâm chỉ số nào khi đánh giá mô hình classification
        3.1. Đối với Binary Classification
            - Recall phải lớn, trong những bài toán y khoa thì rất quan trọng nếu những bài toán chấp nhận tăng recall lên để phù hợp hơn
            - Khi nào quan tâm vào precision: dự đoán spam mail => Độ precision quan trọng hơn
            => Quan trọng theo bài toán yêu cầu gì để nên tăng recall hay precision
            - Specificity (độ đặc hiệu) khi nào cần quan tâm: Nhưng cái nào kiểm tra đúng nhất có thể, nếu sai nó ảnh hưởng đến người nên phải kiểm kỹ
            => Tùy theo mỗi loại bài toán để nâng chỉ số lên cho phù hợp với bài toán   
        3.2. Đối với Multiple classification
            - Accuracy = Tổng dự đoán đúng/ Số mẫu
            - Precision, Recall, F1-sroce:
                * Average = 'Macro' lấy trung bình
                * Average = 'micro' lấy chi tiết để tính
            Với bài toán nào thì nên rất quan trọng:
                => Khi mà các lớp nó không cân bằng thì nó sẽ tính theo micro/ Nếu tập dữ liệu cân đối thì lấy trung bình theo macro
        3.3. Một số chỉ số khác
            - ROC-AUC
                * Hiện thị mối quan hệ TPR (Sensitivity - độ nhạy hay recall) và FPR (1-Specsitity - độ đặc hiệu) khi thay đổi giá trị threshold
                * Công cụ dùng đánh giá độ tốt giữa các mô hình trong bài Binary Classication
                * Với Multiple classification có thể dùng xác định class nào được dự báo tốt bới mô đồ
                * Khi nào thì tăng, giảm TPR và FPR
                * No skill la đường giới hạn 50% và 50%
                * Model-AUC=0.895: nó cao hơn đường No skill thì mô hình này thuật toán 
                * Khi mỗi mô hình đường model-AUC càng cao và tiệm cận 1 thì mô hình đó tốt => Đánh giá thuật toán 1, thuật toán 2 để xem mực độ thế nào
                => ROC-AUC dùng để đánh đổi đánh giá các mô hình xem thế nào
                => Nếu Multiple classification
                * Chỉ số ROC-AUC: phụ hợp các lợp dự báo cân bằng
                * Đường ROC (receive operator Charateristic Curve): Thể hiện sự đánh đổi độ nhạy và độ đặc hiệu khi giá trị ngưỡng thay đổi 
                    + Trục x: Sai số dương tính giả (1-Độ đặc hiệu) => Sai số dương tính giả (False Positive Error)
                    + Trục y: Độ nhạy
                => Khi độ nhạy tăng thì sai số dương tính giả tăng bà ngược lại
                
            - Precision Recall Curve-AUC
                * Còn nếu không phù cân bằng thi sẽ có chỉ số khác: Precision Recall Curve-AUC
                    - Hiển thị quan hệ Precision và Recall khi thay đổi giá trị Threshold
                    - Thường được sử dụng với unbalance data
                    => Cùng recall mà Precision cao hơn thì chọn cái đó
                * Hệ số AUC: Area Under the ROC Curve
                    + Là diện tích phần năm dưới đường ROC
                    + AUC thể hiện khả năng dự báo của mô hình: Thể hiện đúng hơn so với độ chính xác của mô hình trong trường hợp mẫu không cân bằng
            
        3.4. Visualize class data
            - Chỉ hiện thị trong không gian 2 hoặc 3 chiều => Khi x có nhiều chiều hơn thì phải giảm PCA
            - Thế hiện sự phân bố của dữ liệu các class (dùng màu sắc cho các lớp)
        3.5. Tại sao cần tính toán độ nhạy và độ đặc hiệu
            - Độ chính xác toàn thể không phải là thước đo tốt nhất trong trường hợp mẫu không cân xứng
            - Cho nên cần độ nhạy và độ đặc hiểu để bao phủ hết dữ liệu dự đoán
        
'''
Hieu_chinh_nguong_threshold_trong_classification = '''
    1. Chọn ngưỡng tối ưu cho bài toán
        - Cách thực hiện
            * Có thể chọn ROC hoặc Precision - Recall Cuve
                precision, recall, threshold = precision_recall_curve(y, y_prob)
            * Dựa trên kết quả trả về tính tập điểm scores theo các threshold
                scores = tpr - fpr
                score = 2*precision*recall / (precision+recall)
            * Tìm chỉ số có scores lớn nhất/ nhỏ nhất
                pos = np.armax(scores)
            * Trả về giá trị ngưỡng
                return threhold (pos), scores(pos)
    => Xem ngưỡng nào phù hợp với bài toán theo yêu cầu phù hợp
    2. Lựa chon ngưỡng phụ thuộc vào sai số nào quan trọng hơn trong mô hình
        - Âm tính giả ở biến 0 hay Dương tính giả ở biến 1
        - Ví dụ:
            * Gọi a là chi phí của KH vỡ nợ khi dự báo không vở nợ
            * Gọi b là chi phí của KH không vỡ nợ nhưng dự báo vỡ nợ
            * Tổng chi phí = a * Âm tính giả + b * Dương tính giả
            => Lựa chọn mức ngưỡng sao cho tổng chi phí là nhỏ nhất
'''

Logistic_Regression = '''
    1. Giới thiệu
        - Giữa trên xác xuất để làm > 50% thì thuộc TP, dưới 50% TN
    2. Thuật toán
        - Tìm trọng số sao cho output tổng xác xuất độ chính xác cao nhất
    3. Nhược điểm
        - Tập dữ liệu phải phân biện bởi mô hình tuyến tính phù hợp với các điểm dữ liệu với nhau
        - Không tuyến tính thì sẽ không hiệu quả => SVM() giải quyết bài toán này
    4. Sẽ gặp trong thực hiện qua bài toán chọn parameter
    5. Kiểm tra dữ liệu có mất cân đối không ? => nếu có thì phải dùng resample hoặc upresample
    6. Thường người ta sẽ điều chỉnh ngưỡng tốt nhất cho bài toán
    7. Là phép biến đổi nhằm đưa ra giá trị dự báo trong khoảng (0,1)

'''

