data_pipeline = '''
    1. Sử dụng data pipeline
        Bước 1: Data processing
        Bước 2: Data Transform
        Bước...
        Bước n: model predict (estimator)
    2. Định nghĩa 1 mô hình rất nhiều bước trong 1 mô hình để có những đối tượng estimator => Để cho mô hình chạy
        - Get_dummy và onehotcoder khác nhau cái gì ?
            * Nằm ở 2 thư việc khác nhau
            * Muốn dưa đối tưởng vào pipeline => Chỉ dùng onehotcoder chứ không dùng được get_dummy chỉ có phương thức nên nó không có transform cho nên không đưa vào được pipeline
        => Chỉ có nhưng đối tượng có fit và transform thì mới đưa vào được pipeline
        - pipeline mục đích chủ yếu là gì ? => Để khởi tạo đối tượng cho chúng ta
    3. Có nghĩa là chúng ta phải làm class chứa những cái khởi tạo vào sau đó pipeline sẽ thực hiện những bước tiếp theo
        - Đối vs enduser => Quan tâm kết quả cuối cùng
        
'''