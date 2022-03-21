import pandas as pd 
import warnings
import pandas_profiling as pp # tổng quan ban đầu về dữ liệu => Cài trên này
warnings.filterwarnings('ignore')

Note = '''
    3. Các xử lý dữ liệu thiếu (Missing value)
        3.1. Tại sao phải xử lý dữ liệu thiếu ?
            - Tập training data set là tập không thể thiếu dữ liệu vì nó sẽ ảnh hưởng đến sức mạnh của model
        3.2. Một số nguyên nhân dữ liệu bị thiếu ?
            - Khai thác dữ liệu (data extraction): có thể ảnh hưởng đến quá trình truy xuất
            - Thu thập dữ liệu (Data colection): Thu thập trong quá trình sửa chửa giai đoạn này khó để sửa hơn
        3.3. Cách xử lý dữ liệu thiếu
            - Xóa (deletion): giảm kích thước mẫu, nên cần xem lại
            - Dùng Mean/mode, median
            - Dùng mô hình dự báo KNN hoặc 1 mô hình ML khác
            - Tự build 1 model để dự đoán dữ liệu
        3.4. Có 2 nhược điểm cho phương pháp dự báo
            - Các giá trị ước tích của mô hình thường xử lý tốt hơn các giá trị thực
            - Nếu không có mối quan hệ giữa các thuộc tính trong tập dữ liệu và 
            thuộc tính có các giá trị bị thiếu thì mô hình sẽ không chính xác khi ước tính các giá trị thiếu
            - Có thể sử dụng interpolate() để nội suy tuyến tính cho các giá trị bị thiếu
        3.5. Ưu điểm và nhược điểm của thuật toán KNN
            - Ưu điểm:
                * KNN có thể dự đoán cả hai thuộc tính định tính và định tính
                * Không cần tạo mô hình dự báo cho từng thuộc tính có dữ liệu thiếu
                * Có thể xử lý dễ dàng dữ liệu thiếu
                * Cấu trúc tương quan của dữ liệu được xem xét
            - Nhược điểm
                * KNN tốn thời gian trong việc phân tích dữ liệu lớn.
                Nó tìm kiếm dữ liệu thông qua tất cả dữ liệu để tìm các trường hợp tương tự nhất
                * Lựa chọn giá trị k là rất quan trọng

'''

## A. XỬ LÝ MISSING VALUE
### 3.1. Loại bỏ dữ liệu trùng
def deleteDuplicates(df):
    try:
        data = df.drop_duplicates()
        return  data
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")
### 3.2. Xử lý dữ liệu số với mean/ mode/ median => thay thế dữ liệu missing value bằng các giá trị mean/median/mode
def changeMisingValueContinuous(df, choose = "mean", lst_continuous=[]):
    try:
        # Xử lý dữ liệu thiếu của các biến liên tục bằng giá trị mean_i
        lst_missing = lst_continuous
        for i in lst_missing:
            if choose == "mean":
                # https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
                mean_i = df.loc[pd.to_numeric(df[i], errors='coerce').isnull()==False,i].astype(float).mean()
                df.loc[pd.to_numeric(df[i], errors='coerce').isnull(),i] = mean_i
                return df
            elif choose == "median":
                median_i = df.loc[pd.to_numeric(df[i], errors='coerce').isnull()==False,i].astype(float).median()
                df.loc[pd.to_numeric(df[i], errors='coerce').isnull(),i] = median_i
                return df
            elif choose == "mode":
                mode_i = df.loc[pd.to_numeric(df[i], errors='coerce').isnull()==False,i].astype(float).mode()
                df.loc[pd.to_numeric(df[i], errors='coerce').isnull(),i] = mode_i
                return df
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 3.3. Filter special character: Tỉm kiếm các ký tự đặc biệt trong kiểu dữ liệu object
def filterSpecialCharacter(df):
    try:
        lists_ = []
        data = "Bang"
        specialCharacter = ['^','<','>','{','}','""','/','|',';',':','.',',','~','!', \
            '?','@','#','$','%','=','&','*','(',')','\\','[','¿','§','«',\
            '»','ω','⊙','¤','°','℃','℉','€','¥','£','¢','¡','®','©','0','-','9','_','+',']','*','$']

        for chara in specialCharacter:
            ten = data.join(chara)
            for i in df.columns:
                ten = df.loc[df[i] == chara]
                lists_.append(ten)
        result = deleteDuplicates(df = pd.concat(lists_))
        return result
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 3.4. Chuyển đổi kiểu dữ liệu cho thuộc tính: change astype for feature 
def changeToAstype(df, lst_int, lst_float):
    # Chuyển thành kiểu số int và float cho các biến kiểu số
    lst_int = lst_int
    lst_float = lst_float
    df[lst_int] = df[lst_int].astype(int)
    df[lst_float] = df[lst_float].astype(float)
    info = df.info()
    return info

### 3.5. Xử lý dữ liệu thiếu của các biến phân loại: add value for value failing
def misingValueCategorical(df, list_category):
    try:
        # Xử lý dữ liệu thiếu của các biến phân loại
        specialCharacter = ['^','<','>','{','}','""','/','|',';',':','.',',','~','!', \
            '?','@','#','$','%','=','&','*','(',')','\\','[','¿','§','«',\
            '»','ω','⊙','¤','°','℃','℉','€','¥','£','¢','¡','®','©','0','-','9','_','+',']','*','$']
        for chara in specialCharacter:
            for i in list_category:
                #print(i)
                mode = df[i].mode().values[0]
                #print(mode)
                df.loc[df[i] == chara, i] = mode
                #print('\033[4m'+'Kiểm tra biến', df[i].value_counts())
        return df
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 3.6. Thay thế giá trị missing value bằng nội suy


### 3.7. Dùng thuật toán KNN để thay thế dữ liệu


