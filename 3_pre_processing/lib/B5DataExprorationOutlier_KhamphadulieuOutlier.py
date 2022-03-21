import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import warnings
import pandas_profiling as pp # tổng quan ban đầu về dữ liệu => Cài trên này
warnings.filterwarnings('ignore')

Note = '''
    4. Phát hiện và xử lý ngoại lệ với outlier hợp lệ và xử lý outlier không hợp lệ
        4.1. Outlier ngoại lệ là gì ?
            - Outlier là 1 mẫu xuất hiện và tách xa khỏi tổng thể
        4.2. Phân loại outlier
            - Ngoại lệ đơn biến: có thể xem xét khi xem xét 1 biến duy nhất
            - Outlier hợp lệ: những outlier đúng với nghiệp vụ kinh tế
            - Outlier không hợp lệ: cần xem lại các nghiệp vụ kinh tế và loại bỏ chúng ra khỏi tập dữ liệu
        4.3. Nguyên nhân gây ra ngoại lệ ?
            - Tự nhiên
            - Nhân tạo: Lỗi do nhập liệu/ Lỗi đo lường/ Lỗi thử nghiệm/ Ngoại lệ có chủ ý/ Lỗi xử lý dữ liệu/ Lỗi lấy mẫu  
        4.4. Tác động của outlier đến thế nào với dữ liệu ?
            - Tăng phương sai lỗi và giám sức mạnh của kiểm định thống kê
            - Làm giảm quy tắc nếu ngoại lệ không phân bổ tự nhiên
            - Chung có thể bias hoặc ảnh hưởng đên mức độ dữ liệu được quan tâm
            - Chúng tác động đến giả định cơ bản của regression và giả định mô hình thống kê khác 
        4.5. Các phát hiện outlier
            - Dùng boxlot, histogram, scatter plot
            - Quy tắc ngón tay
            - Phạm vi giá trị: Q1-1.5*IQR và Q1+1.5*IQR
            - Phạm vi phân vị từ 5 đến 95 nằm ngoài được coi là outlier
            - Phát hiện theo nghiệp vụ bai toán
        4.6. Cách loại bỏ outlier
            - Xóa bỏ: Mức độ ảnh đến bộ mẫu => Xóa khi outlier bất hợp lý/ Hợp lệ thi không xóa => Chỉ xóa những outlier có ngoại lệ nhỏ về số lượng
            - Điện giá trị thay thế bằng: mode/ median/ mean
            - Biến đổi chúng bằng các giá trị thông qua hàm với hệ số e =>Giảm giá trị về cùng cơ số, 
            phương thức log để tạo ra cột để độ lớn scale lại và tiệt tiêu độ lớn đó
            - Tách riêng bộ dữ liệu outlier và bộ không có outlier => kỷ thuật: Treat separately
            - Thuật toán chấp nhận outlier nhưng chỉ chấp nhận outlier hợp lệ cho nên cần xử lý triển để outlier không hợp lệ
            - Thuật toán Cây quyết định (Decision Tree) cho phép xử lý tốt các ngoại lệ do việc tạo biến
        4.7. Có thể nhìn thông qua để biết xem biết và phát hiện xử lý ngoại lệ
            - Mean/Median/Mode => Giá trị phải ngang ngang nhau => nếu không thì mean sẽ trội hơn so với thuộc tính median và mode
            - Rất quan trọng để điều tra bản chất của ngoại lệ trước khi quyệt định
'''

## A. TÌM HIỂU VỀ OUTLIER
### 4.1. Biểu đồ boxplot dùng xem outlier => Xem mức độ dữ liệu phân bổ dữ liệu outlier hợp lý và không hợp lý
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

### 4.2. Xem xét outlier (thuộc tính 'compression_ratio'): Hiển thị những giá trị outlier của thuộc tính
##### filterOutlier: thuộc tính cần tìm hiểu về outlier
##### listsDisplay: Hiện thị các thuộc tính kèm theo
##### Q1 - 1.5 * IQR to Q3 + 1.5 * IQR
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


### 4.3. % of outlier chiếm bao nhiêu - Number of lower outliers
##### filterOutlier: thuộc tính cần tìm hiểu về outlier
##### listsDisplay: Hiện thị các thuộc tính kèm theo
##### Q1 - 1.5 * IQR to Q3 + 1.5 * IQR
def percentageOfOuliers(df, filterOutlier):
    try:
        outlierUppers = []
        outlierLowers = []
        for i in filterOutlier:
            IQR= scipy.stats.iqr(df[i])
            Q3 = np.quantile(df[i].dropna(), 0.75)
            Q1 = np.quantile(df[i].dropna(), 0.25)
            outlierUpper = df.loc[df[i] > Q3 + 1.5 * IQR].shape[0]
            outlierLower = df.loc[df[i] < Q1 - 1.5 * IQR].shape[0]
            outlierUppers.append(outlierUpper)
            outlierLowers.append(outlierLower)
        outlierUpper_ = sum(outlierUppers)
        outlierLower_ = sum(outlierLowers)
        outliers_per = round((outlierUpper_+outlierLower_)/df.shape[0],3)
        return outliers_per
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")
