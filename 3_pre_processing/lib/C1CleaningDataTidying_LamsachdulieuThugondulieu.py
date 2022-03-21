Exploring_data = '''
    CLEANING DATA - LÀM SẠCH DỮ LIỆU
    1. Khám phá dữ liệu (Exploring data)
        Step1: Khám phá dữ liệu
            - Khám phá dữ liệu để làm gì ?
                * Chẩn đoán các vấn để như ngoại lệ, giá trị bị thiếu và trung lặp dữ liệu
            - Hiểu ý nghĩa của các thuộc tính và biến
            - Phát hiện các lỗi bên trong càng nhiều càng tốt, các lỗi tiềm ẩn bên trong 
            => Xây dựng 1 bộ dữ liệu phù hợp với yêu cầu bài toán
            - Các đánh giá nhanh nhất: thông qua các công cụ trực quan
            - Dữ liệu trùng lặp: trùng lặp trên 1 tập hợp các thuộc tính hữu hạn
        Step2: Chuẩn hóa dữ liệu
            - Làm sách dữ liệu xem dữ liệu bên trong có vấn đề gì không ?
            - Dữ liệu ban đầu luôn bị lỗi
            - Cần chuẩn hóa dữ liệu để tìm ra các vấn đề cần giải quyết
        Step3: Một số vấn đề thường gặp
            - Tên các cột không thống nhất
            - Dữ liệu bị thiếu: missing value, null, thiệu thuộc tính, thiếu thông tin, ký tự 
            => Thiếu 1 số thuộc tính cần thiết của bài toán
            - Ngoại lệ (outlier): 
                * Hợp lý không được xóa cần xem xét lại nghiệp vụ
                * Không hợp lệ: nếu xóa thì xem lại tỉ lệ bộ mẫu nếu tỉ lệ thấp thì xóa dữ liệu, 
                nếu cao thì cần xem xét lại tổng thệ của bộ mẫu
            - Dòng dữ liệu trùng lặp
                * Xem dữ liệu trùng lặp trên 1 bộ thuộc tính 
                => Nên xóa dữ liệu trung lặp
            - Dữ liệu không gọn gàng cần nhóm lại
            - Một cột chứa nhiều thông tin hoặc có những thông tin không mong muốn
        Step4: Quan trọng trong kham phá dữ liệu
            - Tần số đếm: đếm giá trị duy nhất trong dữ liệu => Dùng value_count() để đếm
            - Kiểu dữ liệu các cột đã đúng chưa
            - Vẽ biểu đồ boxlot xem xét tỉ lệ outlier nhiều hay ít
        Step5: Trực quan dữ liệu khám phá
            - Sử dụng biểu đồ phù hợp để phát hiện lỗi nhanh hơn
            - Tìm những điểm chung các pattern trong dữ liệu
            - Lập kế hoạch các bước để làm sạch dữ liệu
            - Dùng 1 số biểu đồ để khám phá dữ liệu
                * Bar plot: Biểu diễn số lượng rời rạc
                * Histogram: Biễu diễn min, max, xem tần số
                * Boxplot: biểu diễn min, max, 1Q, median, 3Q, outliers
                * Scatter plot: kiểm định ứng dụng vào model, phát hiện thêm outlier của 2 biến có hợp lý hay không ?
        Step6: Xác định error
            - Không phải các outlier cũng hợp lý và không hợp lý cần xem xét
            - Một số có thể là lỗi, có thể 1 số khác có giá trị là hợp lệ
    => Đã năm ở B1 đến B5
'''
Tidying_data = '''
    2. Thu gọn dữ liệu
        2.1. Mục tiêu
           - Đây không phải là phân tích các bộ dữ liệu mà là chuẩn bị chung theo cách chuẩn hóa dữ liệu phù hợp trước khi phân tích
        2.2. Một số loại dữ liệu lộn xộn cần phải giải quyết
            - Tiêu đề cột là giá trị, không phải tên biến
            - Nhiều biến được lưu trữ trong 1 cột
            - Các biến được lưu trữ trong một cột
            - Nhiều đơn vị mẫu được lưu trữ trong 1 bảng
            - Một mẫu quan sát duy nhất được lưu trữ trong nhiều bảng và file
        2.3. Dữ liệu như thế nào là dữ liệu gọn ?
            - Kết quả của quá trình thu gọn dữ liệu
            - Dễ dàng thao tác, mô hình hóa và trực quan
            - Mỗi tập dữ liệu gọn gàng được sắp sếp sao cho mỗi biến là một cột và mỗi quan sát là 1 hàng
        2.4. Đặc điểm đo lường
            - Một biến đo lường phải ở trong 1 một cột
            - Mỗi mẫu khác nhau của biến đó nên ở một hàng khác nhau
            - Cần mỗi biến là 1 cột khác nhau
            - Nếu có nhiều bảng, thì chúng có 1 cột trong bảng cho phép chung liên kết
        2.5. Pivoting data (un-melting data)
            - Trong melting data chung ta chuyển các cột thành các dòng
            - Trong pivoting data: chuyển các giá trị duy nhất thành các cột riêng biệt
            - Dùng để tạo các báo cáo
            - Vi phạm nguyên tắc của tity data: các dòng chứa các mẫu
            - Sử dụng pivot hoặc pivottable 
'''
combining_data = '''
    3. Kết hợp dữ liệu
        - Vấn đề
            * Dữ liệu không phải lúc nào cung lưu trong 1 tệp lớn 
        - Ưu điểm
            * Dễ dàng lưu trữ và chia sẽ
            * Có thể lưu trữ mỗi ngày
            * Có thể kết hợp với nhau để làm sạch dữ liệu hoặc ngược lại
        - Giải pháp
            * Phương pháp concat
                + Nối dữ liệu
                + Sử dụng để kết nối dataframe cùng cấu trúc dữ liệu
                + Nối nhiều tập tinh nhiều file
            * Phương pháp trộn dữ liệu merge()
                + Tương tự như phép join bằng bảng CSDL
                + Kết hợp các bộ khác nhau dựa trên các cột chung hay key
'''
cleaning_data = '''
    4. Làm sạch dữ liệu (Cleaning data)
        Step1: Kiểu dữ liệu (data type)
            - Theo yêu cầu phải chuyển dữ liệu từ kiểu này sang kiểu khác => Cột số có thể chứa chuổi hoặc ngược lại
            - Chuyển dữ liệu thành số pd.to_numeric(df['tên_cột']
            - Chuyển đổi kiểu dữ liệu cho cột: df['tên_cột'].astype(kiểu_dữ_liêu)
        Step2: Dữ liệu phân loại (Categorical data)
            - Chuyển categorical data chuyển dữ liệu thành 'category' dtype 
            - Có thể làm cho dataFrame giảm được kích thước trong memory
            - Có thể làm cho chúng được sử dụng dễ dàng bởi các thư viện python khác
        Step3: Thao tác trên chuỗi
            - Phần lớn việc làm sạch dữ liệu liên quan đến thao tác chuỗi
            - Hầu hết dữ liệu trên thế giới là văn bản không có cấu trúc
            - Có rất nhiều thư viện hỗ trợ built-in và thư viện bên ngoài
            - Các công cụ xử lý chuỗi
                * Sử dụng regular expression
                * Xử lý các dữ liệu không phù hợp
                * Xử lý dữ liệu trùng lặp
                * Xử lý dữ liệu thiếu (missing value)
        Mục đích:
            - Các function: df.apply()/ Regular expression: re.compile()/ User defined function

'''

import pandas as pd 
import numpy as np
import warnings
import pandas_profiling as pp # tổng quan ban đầu về dữ liệu => Cài trên này
warnings.filterwarnings('ignore')
import glob

## A. CLEANING DATA - LÀM SẠCH DỮ LIỆU
### 3.1. Chuyển cột chứa giá trị thay vi chứa biến nên dùng melt
##### Melt df into new dataFrame
##### Mục đích: Chuyển dữ liệu dạng báo cáo về dạng cột để thực hiện phân tích dữ liệu
def changeRowstoColumn(df, id_vars, var_name, value_name):
    try:
        df_melted = pd.melt(df, id_vars=id_vars, var_name=var_name, value_name=value_name)
        return df_melted
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 3.2. Short value => Mục địch short giá trị hoặc short theo biến
def sortFeature(df, by=[]):
    try:
        df_sort = df.sort_values(by=by)
        return df_sort
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 3.3. Merge in Datatidying
##### Dùng hàm merge để thực hiện kết nối 2 bảng
def mergeData(df1, df2, how = 'inner', on = []):
    try:
        result = pd.merge(df1, df2, how=how, on=on)
        return result
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 3.4. Dữ liệu trên nhiều file mục đích ghép nhiều file lại nhiều
def loadFileMul(dir_name_file="", names="", index_col=None, header =0):
    try:
        allFiles = glob.glob(dir_name_file)
        frame = pd.DataFrame()
        df_list = []
        for file_ in allFiles:
            if dir_name_file.endswith("csv"):
                df = pd.read_csv(dir_name_file, names=names, index_col=index_col, header=header)
            elif dir_name_file.endswith("xlsx"):
                df = pd.read_excel(dir_name_file, names=names, index_col=index_col, header=header)
            elif dir_name_file.endswith("json"):
                df = pd.read_json(dir_name_file, names=names, index_col=index_col, header=header)
            else:
                print("Please see file and path")
            df.columns = map(str.lower, df.columns)
            df_list.append(df)
        results = pd.concat(df_list)
        return results
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

# Tạo DataFrame chỉ gồm Biến output, Biến intputs được chọn (phân loại và liên tục)
def combiningData(df, lst_phanloai_chosen, lst_lientuc_chosen, lst_output):
    try:
        data0 = df[lst_phanloai_chosen+lst_lientuc_chosen+lst_output]
        results = data0.drop_duplicates().reset_index()
        return results
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")
