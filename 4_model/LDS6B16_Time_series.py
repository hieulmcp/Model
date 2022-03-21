Time_series = '''
    1. Giới thiệu
        - Dạng bài toán thông tin được thu thập 1 cách định kỳ và số lượng đi theo tháng đó
        - Chỉ cho 1 feature để suy ra target => Dự báo target thông qua độ trể dữ liệu quá khứ
        - Độ trê thời gian cần nhắc đến và nên sử dùng môn deep để xem lại thuật toán để biết hơn và phân tích dòng thời gian hay hơn
        - 2 Thuật toán liên quan đến thống kê ARIMA và thuật toán 
    2. Các thành phân trong bài toán time series
        - Trend
        - Seasonal
        - Residual
        -
        => Cách làm mô hình truyền thống
'''

ARIMA = '''
    1. Gồm 2 model: AR và MA
       - ARIMA(p, d, q)
       - AR (p)
       - MA (q)
    2. Các bước
        Bước 1: AR dùng kiếm ra hàm đường hồi quy tuyến tính trước => Ra phân lỗi err
        Bước 2: Dùng MA cho phần err trung bình của 2 cái trước đó lúc đó 
        Bước 3: Giá trị dự báo AR + MA => Ra dự báo
    3. Dữ liệu của Arima
        - Stationary: => Không có stationary thì phải chuyễn dữ liệu thành stationary => làm cho dữ liệu nó đều
        Arima: sẽ làm việc trên dữ liệu ARMA trước thì có nghĩa là làm việc trên stationary(mục đích giảm trend trong các tập dữ liệu)
        - d: giảm đi tính stationary
        - p: giá trị hồi quy tuyến tính
        - q: giá trị trùng bình khi tính err
        => Vậy p, d, q lấy bao nhiêu thì phù hợp ? => Cái nào cho độ do tốt nhất thì dùng cái đó
        - auto_arima: để do giá trị tốt nhất cho mô hình => tìm tunning parameter tốt nhất
        

'''