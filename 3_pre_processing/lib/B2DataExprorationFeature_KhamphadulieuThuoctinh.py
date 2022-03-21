import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import warnings
import pandas_profiling as pp # tổng quan ban đầu về dữ liệu => Cài trên này
warnings.filterwarnings('ignore')
from nltk.stem.wordnet import WordNetLemmatizer
from scipy.stats import kurtosis, skew 

Note = '''
    2. Các bước thực hiện Data exploration
        2.1. Xác định thuộc tính/ biến (Variable indentification)
                - Nhiệm vụ: Loại dữ liệu; mỗi quan hệ giữa các thuộc tính; thuộc tính nào hữu ích; loại bỏ các thuộc tính không cần thiết
                - Xác định các thuộc tính: Xác định thuộc tính hữu ích kinh tế; tiếp thị; phân tích hiệu suất chính (KPIs) và xác định biến đâu ra cần xác định
                - Các bước thục hiện khi phân tích thuộc tính/Biến
                    Step1: Xác định các biến đầu vào (input) và output
                        * Cách dễ nhất để xác định biến input là xác định biến output
                    Step2: Kiểu dữ liệu của thuộc tính
                        * Kiểu dữ liệu mặc định thế nào
                        * Hiểu về thuộc tính dữ liệu và bản chất của dữ liệu
                        * Ưu và nhược điểm của mỗi thuộc tính
                    Step3: Xác định loại thuộc tính phân loại hay liên tục
                        * Thuộc tính phân loại kiểu số hay kiểu chuỗi
                        * Cần dựa vào ý nghĩa của thuộc tính
                - Kiểu dữ liệu thường có 4 loại
                    * Numerical Data: Kiểu rồi rạc hoặc liên tục có logic/ xem mức độ range = max - min
                    * Categorical Data: Loại theo thứ tự theo tự nhiên hoặc loại không theo thứ tự/ text: spam hoặc ham
                    * Time seris Data: Biến động theo thời gian và liên tục
                    * Text: Dạng văn bản NLP
        2.2. Phân tích đơn biến (Univariable analysis)
            2.2.1. Biến liên tục (Continuous variables)
                Thứ 1: Tìm hiểu xu hướng trung tâm và sự lây lan của biến
                Thứ 2: Được đo bằng các thước đo
                    - Central tendency - Xu hướng trung tâm và lây lan của biến
                        * Mean: giá trị trung bình
                        * Median: trung vị của dữ liệu
                        * Mode: giá trị xuất hiện nhiều
                        * Min: Giá trí thấp nhất
                        * Max: Giá trị cao nhất
                    - Measure of dispersion - Độ phân tán của dữ liệu
                        * Range = Max - Min: khoảng cách
                        * Quartile liên quan đến tứ phân vị: 25%, 50%, 75%
                        * IQR: Khoảng cách dữ liệu năm trong vùng median 25% và median 75% hay Q1 và Q3 cho biết các giá trị outlier hợp lý và không hợp lý
                        * Variable (đo khoảng cách dữ mỗi số): mức độ phân tán của dữ liệu
                        * Standard Deviation: độ lệch chuẩn, trung tâm lệch chuẩn, lệch trái, lệch phải...
                        * Skewness: Phân phối chuẩn hay không ? => nếu trả về 0 phân phổi chuẩn, lớn >0 lệch phải; < 0 lệch trái.
                        * Kurtosis: =0 thì phân phổi chuẩn >0 nhọn hơn phân phối chuẩn; <0 thì nó bẹt hơn phân phối chuẩn
                    - Visualiation methods
                        * Histogram: Giá trị phối theo cột
                        * Box plot: thuộc tính có giá trị outlier  hay không
                        * Distributionplot: Phân phối trung tâm bị lệch phải hay lệch trái so với trung tâm
                Thứ 3: Mục đích
                    - Làm nỗi lên giá trị thiếu hoặc missing value hoặc ngoại lệ/outlier
            2.2.2. Biến phân loại (Categorical variables)
                Thứ 1: Sử dụng tần số để hiểu phân phối cùng loại/ tỉ lệ % theo giá trị hàng mục hoặc theo đếm dữ liệu
                Thứ 2: Được đo bằng các thước đo
                    - Đếm bằng value_count theo từng category => Xem được mức độ cần bằng của dữ liệu theo tần suất  
                Thứ 3: Trực quan hóa dữ liệu
                    - Bar chart để trực quan hóa xem mức độ dữ liệu
            2.2.3. Mục đích của việc phân tích đơn biến
                - Sử dụng để làm nổi bật các giá trị bị thiếu và ngoại lệ
                 
'''

## A. Phân tích thuộc tính
### 2.0. Tổng quan về thông tin ban đầu: thì cần coi lại những thuộc tính cần thiết
def startInformation(df, choose, list_, head =10, tail = 10):
    try:
        # Xem info
        if choose == "info":
            info = df[list_].info()
            return info
        # Xem dữ liệu trống
        elif choose == "nan":
            nan = df[list_].isna().sum()
            return nan
        # Xem 10 dữ liệu đầu
        elif choose == "head":
            head = df[list_].head(head)
            return head
        # Xem 10 dữ liệu đầu
        elif choose == "tail":
            head = df[list_].tail(tail)
            return head
        elif choose == "shape":
            shapes_ = df.shape
            return shapes_
        elif choose == "null":
            # Xem giá trị null
            null_ = df[list_].isnull().sum()
            return null_
        elif choose == "profile":
            # Nhìm tổng quan về báo cáo
            profile = pp.ProfileReport(df)
            return profile
        elif choose == "dtypes":
            dtypes_ = df[list_].dtypes
            return dtypes_
        else:
            print("Please see file")
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")
 
### 2.1. Các thuộc tính input kiểu số /kiểu chuỗi: Xem lại kiểu dữ liệu của bài toán
def defineDtypeFeatures(df, lst_input, choose = "object"):
    try:
        if choose == "object":
            print('Thuộc tính kiểu chuỗi:', df[lst_input].select_dtypes(include=['object']).columns)
            lists_ = df[lst_input].select_dtypes(include=['object']).columns
            result = pd.DataFrame(lists_, columns=['Thuộc tính kiểu chuỗi'])
            return result
        elif choose == "numbers":
            #2.3. Các thuộc tính input kiểu số 
            print('Thuộc tính kiểu số:', df[lst_input].select_dtypes(include=['int','float']).columns)
            lists_ = df[lst_input].select_dtypes(include=['int32','float64','int','float']).columns
            result = pd.DataFrame(lists_, columns=['Thuộc tính kiểu số'])
            return result
        else:
            print("Please choose = [object or numbers]")
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 2.2.  Xác định thuộc tính input là phân loại (Categorical field): Dùng để đưa các thuộc tính phân loại vào thuộc tính => Lấy dữ liệu là lst_phanloai
##### Mục đích xem lại các dữ liệu là thuộc tính thuộc categorical
def defineDtypeCategorical(df, lst_input, numbers = 20):
    try:
        categoricals = []
        continuous = []
        lst_phanloai = []

        for i in lst_input:    
            if df[i].dtypes =='object':
                lst_phanloai.append(i)
                i = '\'' + i + '\''
                categoricals.append(i)
            elif len(df[i].unique()) <= numbers and df[i].dtypes =='int':
                lst_phanloai.append(i)
                i = '\'' + i + '\''
                continuous.append(i)   
            else: pass    
        print('- Thuộc tính có thể phân loại kiểu chuỗi: ',', '.join(categoricals))
        print('- Thuộc tính có thể phân loại kiểu số: ',', '.join(continuous))
        return lst_phanloai
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### .3. Xác định thuộc tính input là liên tục (Continious field): dùng để lựa chọn lại các thuộc tính lst_lientuc
##### Mục đích xem lại các dữ liệu là thuộc tính thuộc liên tục
def defineDtypeContinuous(lst_input, lst_phanloai):
    try:
        lst_lientuc = list(set(lst_input) - set(lst_phanloai))
        t3 = []
        for i in lst_lientuc:
            i = '\'' + i + '\''
            t3.append(i)   
        print('- Thuộc tính liên tục:',', '.join(t3))
        return lst_lientuc
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

## B. PHÂN TÍCH BIẾN LIÊN TỤC (Continious field)
### 2.4. Các chỉ số mô tả thuộc tính output và input liên tục
##### Mục đích thực hiện xem các dữ liệu 'nameFeature', 'min', 'max', 'mean', 'median',
##### 'mode', 'std', 'var', 'kurtosis', 'text_kurtosis', 'skew', 'text_skew' => Xem thế nào và thực hiện tiếm các bước tiếp theo của biến continious
def summaryVariableContinuousAndCategorical(df, lst_lientuc, lst_output, columns = ['nameFeature', 'min', 'max', 'mean', 'median', \
        'mode', 'std', 'var', 'kurtosis', 'text_kurtosis', 'skew', 'text_skew']):
    try:    
        lst_ = lst_lientuc+lst_output
        results_ = []
        kurtosis_ = 0
        skew_ = 0
        for i in lst_:
            #print("\nGiá trị thống kê của", (lst_lientuc+lst_output)[i],":\n",stats.describe(df[(lst_lientuc+lst_output)[i]]))
            nameFeature = i
            min = round(df[i].min(),1)
            max = round(df[i].max(),1)
            mean = round(df[i].mean(),1)
            median = round(df[i].median(),1)
            mode = round(df[i].mode()[0],1)
            std = round(df[i].std(),1)
            var = round(df[i].var(),1)
            kurtosis_ = round(kurtosis(df[i]),1)
            if kurtosis_ > 0:
                text_kurtosis = "Lệch phải"
            elif kurtosis_ < 0:
                text_kurtosis = "Lệch trái"
            elif kurtosis_ == 0:
                text_kurtosis = "Đối xứng"
            skew_ = round(skew(df[i]),1)
            if skew_ > 0:
                text_skew = "Nhọn"
            elif skew_ < 0:
                text_skew = "Bẹt"
            elif skew_ == 0:
                text_skew = "~Chuẩn"
            result = (nameFeature, min, max, mean, median, mode, std, var, kurtosis_, text_kurtosis, skew_, text_skew)
            results_.append(list(result))
            kq = pd.DataFrame(results_, columns=columns)
        return kq
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 2.5. Biểu đồ phân phối => Mục đích: Xem mức độ thuộc tính xem mực độ phân bổ dữ liệu trong thuộc tính
def displotChart(df,lst_lientuc, lst_output, witdth=15, height=10, a=3, b=5):
    try:
        plt.figure(figsize=(witdth,height))
        n=0
        for i in (lst_lientuc+lst_output):
            n=n+1
            plt.subplot(a,b,n)
            sns.distplot(df[i])
        plt.tight_layout()
        plt.show()
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 2.6. Biểu đồ phân phối chồng lên nhau: Xem mức độ các biên có sát nhau không gần nhau không
def subplotsChart(df, lst_lientuc, lst_output, witdth=15, height=10):
    try:
        f, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(witdth,height))
        for i in (lst_lientuc+lst_output):
            sns.distplot(df[i], ax= ax1, hist=False)
        plt.show()
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

## TÌM HIỂU VỀ OUTLIER
### 2.7. Biểu đồ boxplot dùng xem outlier => Xem mức độ dữ liệu phân bổ dữ liệu outlier hợp lý và không hợp lý
def boxplotChart(df, lst_lientuc, lst_output, a=3, b=5):
    try:
        plt.figure(figsize=(15,8))
        n=0
        for i in (lst_lientuc+lst_output):
            n=n+1
            plt.subplot(a,b,n)
            sns.boxplot(df[i])
        plt.tight_layout()
        plt.show()
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 2.8. Xem xét outlier (thuộc tính 'compression_ratio'): Hiển thị những giá trị outlier của thuộc tính
##### filterOutlier: thuộc tính cần tìm hiểu về outlier
##### listsDisplay: Hiện thị các thuộc tính kèm theo
def filterOutlier(df, filterOutlier, listsDisplay):
    try:
        IQR= scipy.stats.iqr(df[filterOutlier])
        Q3 = np.quantile(df[filterOutlier].dropna(), 0.75)
        Q1 = np.quantile(df[filterOutlier].dropna(), 0.25)
        result1 = df.loc[df[filterOutlier] > Q3 + 1.5 * IQR,listsDisplay]
        result2 = df.loc[df[filterOutlier] < Q1 - 1.5 * IQR,listsDisplay]
        result = pd.concat([result1, result2])
        return result
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

## C. PHÂN TÍCH BIẾN PHÂN LOẠI (Categorical field)
### 2.9. Các chỉ số mô tả thuộc tính: xem lại mức tần số mức độ dữ liệu
def summaryCategorical(df, lst_phanloai, columns = ['feature','Số phân tử']):
    try:
        lsts_ = []
        for i in lst_phanloai:
            nameFeature = i
            values = len(df[i].unique())
            value_counts = df[i].value_counts()
            print('-', '\033[4m'+'Mô tả biến ', i+'\033[0m', ':',len(df[i].unique()),'giá trị')
            print(value_counts)
            lst_ = (nameFeature, values)
            lsts_.append(list(lst_))
            kq = pd.DataFrame(lsts_, columns=columns)
        return kq
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 2.10. Value_count theo từng thuộc tính: xem mức độ các biên, count các phần tử
def categorical_value_counts(df, lst_phanloai):
    try:
        value_counts_ = df[lst_phanloai].value_counts()
        kq = pd.DataFrame(value_counts_)
        return kq
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")   

### 2.11. Xem barchare xem mức độ dữ liệu
def barchart(df, lst_phanloai, width=15, height=10, rotation=45, a =4, b=3):
    try:
        # Biểu đồ barchart
        plt.figure(figsize=(width,height))
        n=0
        for i in lst_phanloai:
            n=n+1
            plt.subplot(a,b,n)
            df[i].value_counts().plot.bar()
            plt.title(i)
            plt.xticks(rotation=rotation)

        plt.tight_layout()
        plt.show()
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 2.12. Xem lại thuộc tính phân loại: Xem lại các mức độ tần số xuất hiện dữ liệu
def categorical_value_counts_count(df, lst_phanloai_chosen):
    try:
        dicts = {}
        for i in lst_phanloai_chosen:
            dict_  = {i: list(df[i].sort_values().unique())}
            dicts.update(dict_)
        #result = pd.DataFrame.from_dict(dicts)
        return dicts
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")
