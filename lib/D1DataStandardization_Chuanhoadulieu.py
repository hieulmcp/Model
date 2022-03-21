Note = '''
    1. Nhìn chung
        1.1. Lợi ích của việc chuẩn hóa dữ liệu
            - Sử dụng phân tích và sử dụng dữ liệu một cách nhất quán
        1.2. Có nên chuẩn hóa dữ liệu không ?
            - Biết được điểm mạnh và điểm yếu
            - Thu thập dữ liệu sao phù hợp
            - Dọn dẹp và phân tích dữ liệu phù hợp
        1.3. Khi nào cần chuẩn hóa dữ liệu ?
            - Khi xây dựng model
                * Mô hình không gian tuyến tính
                * Các tính năng dữ liệu có phương sai cao
                * Các tính năng dữ liệu liên tục có đơn vị đo lường khác nhau
                * Giả định tuyến tính khác nhau
            - Nhu cầu chuyển đổi dữ liệu có thể phụ thuộc vào mô hình hóa mà chúng ta dự định sử dụng
                * Phương sai của biến đâu ra không thay đổi khi chung ta thay đổi biến đầu vào
                * Đảm báo rằng mối quan hệ giữa các biến đầu vào và biến đầu ra xấp xỉ tuyến tính
    2. Log normalization
        2.1. Ý nghĩa
            - Mục đích: dùng log để thay đổi hình dạng phân phối của biến trên biểu đồ phân phối
            - Được sử dụng để làm độ lệch phải (right skewness) của các biến:
                * Chỉ áp dụng với số dương
                * Không áp dụng được với phân phối lệch trái
                * Nếu sử dụng log may mắn thì sẽ trả về phân phối chuẩn kết quả hiệu suất cao hơn
        2.2. Cách áp dụng hàm log
            - Chuyển đổi log tự nhiên
            - Log tự nhiên có cơ số e = 2.718
            - Năm bắt những thay đổi tương đối, cương độ thay đổi, cường độ thay đổi và dữ mọi thứ trong không gian dương
            - Chia dữ liệu trong phạm vi theo số log
            - Dùng cho skewed và wedi Distribution
        2.3. Nên sử dụng khi nào ?
            - Phân phối lệch phải và độ lệch dương => skew trả về dương
            - Nếu thành phân theo cấp số nhân => sử dụng log
            - Dữ liệu được phân loại theo tứ tự độ lớn
            - Phương sai lớn và phân phối lệch phải thì sử dụng log
            - Log áp dụng để giảm thiểu outlier
            - Áp dụng trên các thuộc tính riêng lẽ
    3. Feature scaling
        3.1. Feature scaling và ý nghĩa
            - Là 1 công việc chuẩn hóa dữ liệu
            - Áp dụng các tính năng và các biến dữ liệu
            - Chuẩn hóa dữ liệu trong 1 phạm vi cụ thể
            - Giúp tăng tốc tính toán trong một thuật toán
            - Áp dụng cho các biến thuộc tính đầu vào dữ liệu chỉ áp dụng thuộc tính kiểu số
            - Không scale các thuộc tính categorical
            - Chỉ scale thuộc tính kiểu dữ liệu continuous
            - Giúp thuộc tính giảm cường độ/ trọng số
        3.2. Đặc điểm
            - Feature scaling giúp cân bằng các tính năng hoặc thuộc tính là như nhau
            - Sự công băng giữa các thuộc tính giữa liệu
            -=> Khi làm dữ liệu thì sẽ làm dữ liệu gốc trước, sau đó mới scale dữ liệu để chọn model tốt nhất
        3.3. Các thuật toán thường chuẩn hóa dữ liệu/ Thuật toán không áp dụng
            - Áp dụng cho các thuật toán
                * PCA: Cố gắng giúp các tính năng có phương sai tốt nhất
                * Gradient Descent: Tốc độ tính toán tăng khi tính toán Theta trở nên nhanh hơn sau khi scaling
                * K-nearest neighbors: KNN sử dụng đo khoảng cách Euclidean, nếu chúng ta muốn tất cả các thuộc tính có đóng góp như nhau
                * K-means: Các cụm cũng được xem xét gần nhau theo khoảng cách như KNN
                * Khi thực hiện thuật toán ML => Nếu có khoảng cách thì chúng ta cần phải chuẩn hóa, con không thì chung ta không cần chuẩn hóa
            - Không áp dụng cho các thuật toán
                * Naive Bayer 
                * Linear Discriminant Analysis
                * Tree-Based models
                => Những thuật toán không ảnh hưởng bởi feature scaling
                => Các thuật toán không dựa trên khoảng cách thì không cần phải áp dụng feature scaling
        3.4. Phương pháp dùng Feature Scaling
            3.4.1. StandardScaler
                - Một kỹ thuật hữu ích để biến đổi các thuộc tính có phân phối Gaussian và các giá trị trung bình (mean) & 
                độ lệch chuẩn (std) khác nhau thành phân phối Gausian tiêu chuẩn với giá trị trung bình là 0 và 
                độ lệch chuẩn là 1 và tuân theo công thức sau cho mỗi tính năng/ thuộc tính
                - Công thức: (xi -mean(x))/stdev(x)
                - Được ưu tiên sử dụng khi các thuộc tính của chung ta có phân phôi chuẩn hoặc xấp xỉ chuẩn (~0)thì chung ta ưu tiền dùng StandardScaler 
                => chuyển thành phân phối Gaussian (chuẩn tắc) từ đó giá trị trung bình 0 và độ lệch chuẩn là 1
                - Nếu dữ liệu bên trong không được phân phối chuẩn thì đây không phải là cách chia tỷ lệ tốt nhất để sử dụng
                - Khi nào thì sử dụng
                    * - Khi các thuộc tính số mà chúng ta đưa vào đều là phân phối chuẩn hoặc xấp xỉ chuẩn 
                    => hiệu quả cao với standardScaler phải sử dụng khi thuộc tính phân phối chuẩn hoặc xấp xỉ chuẩn 
                    => Xem hiệu quả cao của model hay không.
            3.4.2. MinMaxScaler
                - MinMaxScaler có thể được xem là thuật toán chia tỉ lệ nổi tiếng nhất và tuân theo công thức sau cho mỗi tính năng/ thuộc tính
                - Công thức: (xi - min(x))/(max(x) - min(x)) => Dùng để thu hẹp dữ liệu lại min =1 và max = 1
                - Về cơ bản, nó thu hẹp phạm vì sao cho phạm vi mới nằm trong khoảng từ 0 đến 1 (hoặc -1 đến 1 nếu có các giá trị âm)
                - Phương pháp được để xuất sử dụng trong thuộc tính của chung ta có 1 hay vài thuộc tính không có phân phối chuẩn hoặc xấp xỉ không chuẩn
                - Đặc điểm
                    * Bộ chia tỉ lệ này hoạt động tốt hơn trong các trường hợp mà bộ chia tỷ lệ tiêu chuẩn (standard scaler) có thể không hoạt động tốt
                    * Nếu phân phối không phải là Gaussian hoặc độ lệch chuẩn là rất nhỏ, min-max scaler hoạt động tốt hơn
                    * Động lực để sử dụng tỉ lệ này bao gồm độ lệch chuẩn của các tính năng rất nhỏ và duy trì các entry có giá trị 0 trong dữ liệu thưa thớt
                - Khi nào nên dùng
                    * Không nên dùng: Có outlier không hợp lệ
                    * Không có outlier là điều kiên quyết => Ảnh hưởng tỉ lệ scale
                    * Không có phân phối chuẩn hoặc không phân phối xấp xỉ không chuẩn
                    * Nếu là outlier hợp lệ thì sau khi giải quyết xong outlier thì chung ta có quyền sử dụng MinMaxOutlier
                - Những hệ số tương quan là không thay đổi: Knew() => Phân phối chuẩn không thay đổi
                - Ưu tiền dùng khi nào
                    * Thuộc tính input không có phân phối chuẩn hoặc xấp xỉ không chuẩn
                    * Dữ liệu của chung ta không có outlier
                    => Khi có 2 yếu tố đó thì mới sử dụng MinMaxOutlier       
            3.4.3. Robust Scaler
                - MinMaxScaler dùng toàn bộ dữ liệu scaler tính toán ra giá trị/ tỉ lệ scaler
                - Robust Scaler dùng phần dữ liệu năm ở vị Q1 và Q3, nằm trong dữ liệu năm trong khoảng IQR để tính toán toàn bộ scaler
                - RobustScaler sử dụng một phương pháp tương tự như MinMaxScaler nhưng nó sử dụng Interquartike range thay cho min - max
                - Công thức: (xi-Q1(x))/(Q3(x)-Q1(x))
                - Đặc điểm
                    * Điều này có nghĩa là RobustScaler đang sử dụng ít dữ liệu hơn khi chia tỉ lệ để nó phù hợp hơn khi có cac ngoại lệ trong dữ liệu
                    * Sau khi áp dụng Robust scaling, các phân phối được dựa vào cùng một tỷ lệ và trùng lặp, 
                    nhưng các ngoại lệ vẫn nằm ngoài phần lớn của các bản phân phối mới
            3.4.4. Normalizer
                - Dùng cho cho dữ liệu rời rạc
                - Dùng cho 2 thuật toán: KNN và Neuron network
            3.4.5. Binarizer
                - Chuyển đổi dữ liệu bằng cách dùng binary threshold (Ngưỡng chọn).
                Tất cả các giá trị trên threshold được thay bằng 1 và các giá trị <= threshold được thay thế bằng 0
    4. Tóm tắt các phương pháp
        (1) StandardScaler: Khi thuộc tính đều có phân phối chuẩn và xấp xỉ phân phối chuẩn 
        (2) MinMaxScaler: Không có phân phối chuẩn và xấp xỉ phân phối chuẩn và trong dữ liệu không có outlier không hợp lệ
        (3) RobustScaler: Không có phân phối chuẩn và xấp xỉ phân phối chuẩn và trong dữ liệu có outlier
        (4) Có thể sử dụng log normalization để thay đổi phân phối chuẩn lệch phải để rồi sử dụng StandardScaler
    '''
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder, RobustScaler, StandardScaler, MinMaxScaler
import numpy as np
import warnings
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
warnings.filterwarnings('ignore')

## A. LOG NORMALIZATION
### 2.1. Chuẩn hoá Log normalization
##### lấy log cho các thuộc tính intputs liên tụ => Cách áp dụng phân phối chuẩn lệch phải thì cải thiện thuộc rất tốt và áp dụng cho 1 thuộc tính
def logNormalization(lst_lientuc_chosen, lst_lientuc_chosen2, df):
    try:
        for i in lst_lientuc_chosen:
            if i in lst_lientuc_chosen2: 
                pass
            else:
                name_log = i + '_log'
                lst_lientuc_chosen2.append(name_log)
                df[name_log] = np.log(df[i])
            
        result = df[lst_lientuc_chosen2]
        return result
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 2.2. Trực quan hóa thuộc tính trước log normalization
def visualizationBeforeLogNormalization(df, var_before_log):
    result = (
        plt.subplot(1,2,1),
        plt.hist(df[var_before_log]),
        plt.subplot(1,2,2),
        sns.displot(df[var_before_log]),
        plt.show()
        )
    return result

### 2.2. Trực quan hóa thuộc tính sau log normalization
def visualizationBeforeLogNormalization(df, var_after_log):
    result = (    
        plt.subplot(1,2,1),
        plt.hist(df[var_after_log]),
        plt.subplot(1,2,2),
        sns.displot(df[var_after_log]),
        plt.show())
    return result

### 2.3. Xem mối quan hệ 2 biến trước log
def visualizationBeforeLogNormalization_relationship(df, var_befor_log_x, var_before_log_y):
    result = (
        sns.lmplot(data=df, x = var_befor_log_x, y=var_before_log_y)
    )
    return result
    
### 2.4. Xem mối quan hệ 2 biến sau log
def visualizationAfterLogNormalization_relationship(df, var_after_log_x, var_after_log_y):
    result = (
        sns.lmplot(data=df, x = var_after_log_x, y=var_after_log_y)
    )
    return result

## B. Feature scalling
## 3.1 Trực quan hóa dữ liệu và xem dữ liệu
### 3.1.1. Trực quan hóa dữ liệu thuộc tính
def visualizationFeature_hist_subplot(df, var_featuer):
    result = (
        plt.subplot(1,2,1),
        plt.hist(df[var_featuer]),
        plt.subplot(1,2,2),
        sns.displot(df[var_featuer]),
        plt.show()
    )
    return result

### 3.1.2. Xem phân phối chuẩn lệch trái hay phải
def skew_Feature(df, var_featue):
    result = df[var_featue].skew()
    return result

### 3.1.2. Xem phân phối chuẩn nhọn hay bẹt
def kurtosis_Feature(df, var_featuer):
    result = df[var_featuer].kurtosis()
    return result

### 3.1.4. Trực quan hóa dữ liệu outlier
def visualizationFeature_boxplot(df, var_featuer):
    result = (plt.boxplot(df[var_featuer])
                ,plt.show())
    return result
### 3.1.5. feature scaler visualization
def visualizationRovustScaler(df, var_before_scaler1, var_before_scaler2, var_after_scaler1, var_after_scaler2):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6,5)),
    result = (
        ax1.set_title("Before Sacling"),
        sns.kdeplot(df[var_before_scaler1], ax=ax1),
        sns.kdeplot(df[var_before_scaler2], ax=ax1),

        ax2.set_title("After Robust Sacler"),
        sns.kdeplot(df[var_after_scaler1], ax=ax2),
        sns.kdeplot(df[var_after_scaler2], ax=ax2),
        plt.show()
    )
    return result

### 3.2. Robust scaler: Phân phổi không chuẩn hoặc không xấp xỉ chuẩn; và có outlier
### 3.2.1. Robust scaler
##### Trả về dữ liệu là 1 dataframe sau đó dùng concat để đưa vào df
def robust_Scaler(df, lst_lientuc_chosen):
    try:
        # Thêm tên khác cho các thuộc tinh scaler
        lst_name_column = []
        for i in lst_lientuc_chosen:
            lst_name_column.append(i+'_scaler')
        # Chuẩn hoá bằng RobustScaler trên dữ liệu đã Log normalization
        #--> Do các thuộc tính không có PP chuẩn và có outliers nên không sử dụng StandarScaler/MinMaxScaler
        scaler = RobustScaler()
        data = df[lst_lientuc_chosen]
        # X_train_scale = scaler.fit_transform(X_before_scale)
        scaler = scaler.fit(data)
        df_new = scaler.transform(data)
        df_new = pd.DataFrame(df_new, columns=lst_name_column)
        return df_new
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 3.3. Standard scaler: Nhớ chuẩn hóa dữ liệu trước khi làm
### 3.3.1. Standard scaler
### Trả về 1 dataframe
def min_Max_Scaler(df, lst_lientuc_chosen):
    try:
        # Thêm tên khác cho các thuộc tinh scaler
        lst_name_column = []
        for i in lst_lientuc_chosen:
            lst_name_column.append(i+'_scaler')

        # Chuẩn hoá bằng RobustScaler trên dữ liệu đã Log normalization
        #--> Do các thuộc tính không có PP chuẩn và có outliers nên không sử dụng StandarScaler/MinMaxScaler
        scaler = StandardScaler()
        data = df[lst_lientuc_chosen]
        data = data.astype('float64')
        # X_train_scale = scaler.fit_transform(X_before_scale)
        scaler = scaler.fit(data)
        df_new = scaler.transform(data)

        df_new = pd.DataFrame(df_new, columns=lst_name_column)
        return df_new
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 3.3. Standard scaler: Nhớ chuẩn hóa dữ liệu trước khi làm
### 3.3.1. Standard scaler
### Trả về 1 dataframe
def standard_Scaler(df, lst_lientuc_chosen):
    try:
        # Thêm tên khác cho các thuộc tinh scaler
        lst_name_column = []
        for i in lst_lientuc_chosen:
            lst_name_column.append(i+'_scaler')

        # Chuẩn hoá bằng RobustScaler trên dữ liệu đã Log normalization
        #--> Do các thuộc tính không có PP chuẩn và có outliers nên không sử dụng StandarScaler/MinMaxScaler
        scaler = MinMaxScaler()
        data = df[lst_lientuc_chosen]
        # data = data.astype('float64')
        # X_train_scale = scaler.fit_transform(X_before_scale)
        scaler = scaler.fit(data)
        df_new = scaler.transform(data)

        df_new = pd.DataFrame(df_new, columns=lst_name_column)
        return df_new
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

# 3.4. Concat nhiều database
# X_new = pd.concat([X_oh_encode, X[lst_lientuc_chosen], X_not_encode], axis=1)
def concatdf(new_data, df):
    X_new = pd.concat([new_data, df], axis=1)
    return X_new





    
