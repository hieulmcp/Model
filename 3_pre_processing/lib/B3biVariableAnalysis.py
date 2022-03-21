import pandas as pd 
from pandas.core.frame import DataFrame
import seaborn as sns
from scipy.stats import chi2_contingency
import statsmodels.api as sm
from statsmodels.formula.api import ols
import warnings
warnings.filterwarnings('ignore')

Note = '''
    3. Phân tích 2 biến (BI-variable analysis
        3.0. Phân tích 2 biền làm gì ?
            - Tìm sự liên kết (association) và không liên kết (Disassociation)
                * Hai biến input có độc lập với nhau không
                * Hai biến input và output có phụ thuộc lãnh nhau không => Có sự liên kết với nhau không ? => Nếu phú thuộc thì quá tốt với model
                * Thực tế các biến input khó có thể độc lập với nhau => Cần xem mức độ tương quan giữa các biến
                * Các biến input phụ thuộc nhau các ít càng tốt
                * Biến input luôn phải phụ thuộc với biến output thì mới có ý nghĩa
        3.1. Biến liên tục với biến liên tục (Continuous vs Continuous)
            - Dùng biểu đồ phân tán
                * Đó là cách phù hợp để xem mối quan hệ 2 biến
                * Cho thấy mỗi quan hệ là tuyến tính hoặc phi tuyến tính
            - Dùng Correction
                * Tương quan khác nhau giữa -1 đến 1
                * Bé hơn 0.3 tương quan rời rác
                * Từ 0.3 đến 0.6 tương quan
                * Lớn hơn 0.6 tương quan mạnh mẽ
        3.2. Hai biến phân loại (Categorical vs Categorical)
            Step 1: Dùng two-way table
                - Bắt đầu phân tích mỗi quan hệ bằng cách tạo 2 chiều Count
                - Các dòng category theo các dòng khác nhau
            Step 2: Stacked column chart - Trực quan hóa 2 cột chồng lên nhau
            Bước 3: Dùng Chi-square
                - Kiểm định 2 biến độc lập hay phụ thuộc
                    * Thức đo giá trị thống kê: Statistic >= Critical value: Dữ liệu độc lập, ngược lại là dữ liệu phụ thuộc
                    * 2. Theo giá trị p-value: p-value <= alpha: 2 biến độc lập, ngược lại 2 biến phụ thuộc hoặc alpha = 1-prod trong đó thường prod: 0.95
        3.3. Biến liên tục vs biến phân loại (Categorical vs Continuous) => Một trường hợp phức tạp
            - Trực quan hóa dữ liệu bằng boxlot
                * Với số lượng thuộc tính ít, không hiển thị ý nghĩa thống kê
            - Dùng ANOVA - để xem mức độ tương quan: aov_table[aov_table['PR(>F)'] < alpha] => Có tương quan với nhau 
        3.4. Mục đích phân tích để làm gì ?
            Thứ 1: Phát hiện missing value và outlier
            Thứ 2: Chọn các thuộc tính categorical, continious phù hợp với bài toán
            Thứ 3: Xem có thể thực các bước tiếp theo      
'''

## A. PHÂN TÍCH 2 BIẾN CONTINIOUS VS CONTINIOUS
### 3.1. Ma trận hệ số tương quan: dùng để xem xét mức độ tương quan của 2 biết liên tục => Quan sát nhìn qua
def corrContinious(df, lst_output, lst_lientuc):
    try:
        return df[lst_output + lst_lientuc].corr()
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 3.2. Biểu đồ tương quan: Thể hiện tương quan giữa các biên nhưng rất khó nhìn hạn chế dùng
def pairplotChart(df, lst_output, lst_lientuc):
    try:
        return sns.pairplot(df[lst_output + lst_lientuc], corner = True)
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

###3.3. Biến inputs liên tục với biến output liên tục: Dùng để xem mực độ tương quan của biến output và output
##### Khi nào biến output là biến continious
##### Biến output và input phải có mức độ tương quan với nhau
def tuongquanOutputvsBienlientuc(df, lst_lientuc, lstOutput, manh=0.6, tuongquan=0.3):
    try:
        j = lstOutput
        pair1 = []
        pair2 = []
        pair3 = []

        for i in lst_lientuc:
            corr = abs((df[[i,j]].corr().loc[[i],[j]]).values[0][0])
            if corr >= manh:
                pair1.append(['Mạnh',j,i,  round(corr,2)])
            elif corr >= tuongquan:
                pair2.append(['Tương quan',j,i,  round(corr,2)])
            else: 
                pair3.append(['Yếu',j,i,  round(corr,2)])
        kq1 = pd.DataFrame(pair1, columns=['Tuong_quan','Variable_output', 'Variable_input',  "corr"])
        kq2 = pd.DataFrame(pair2, columns=['Tuong_quan','Variable_output', 'Variable_input',  "corr"])
        kq3 = pd.DataFrame(pair3, columns=['Tuong_quan','Variable_output', 'Variable_input',  "corr"])
        result = kq1.append(kq2)
        result = result.append(kq3)
        return result
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

###3.4. Tương quan giữa các biến inputs liên tục: Xem mức độ tương quan của các thuộc tính input liên tục với nhau
##### Biến input càng tương quan thì cần xem xét nên chọn biến nào đề phù hợp với bài toán
def tuongquan2bienInputLientuc(df, lst_lientuc, choose="Mạnh"):
    try:
        pair1 = []
        pair2 = []
        pair3 = []
        pair4 = []

        for i in lst_lientuc:
            for j in lst_lientuc[lst_lientuc.index(i)+1:]:
                corr = abs((df[[i,j]].corr().loc[[i],[j]]).values[0][0])
                if corr >= 0.9:
                    pair1.append(['Mạnh',j,i, round(corr,2)])         
                elif corr >= 0.6:
                    pair2.append(['Vừa',j,i, round(corr,2)])          
                    
                elif corr >= 0.3:
                    pair3.append(['Tương quan',j,i, round(corr,2)])
                else: 
                    pair4.append(['Yếu',j,i, round(corr,2)])
        if choose =="Mạnh":
            kq1 = pd.DataFrame(pair1, columns=['Tuong_quan','Variable_input1', 'Variable_input2',  "corr"])
            return kq1
        elif choose == "Vừa":
            kq2 = pd.DataFrame(pair2, columns=['Tuong_quan','Variable_input1', 'Variable_input2',  "corr"])
            return kq2
        elif choose =="Tương quan":
            kq3 = pd.DataFrame(pair3, columns=['Tuong_quan','Variable_input1', 'Variable_input2',  "corr"])
            return kq3
        elif choose == "Yếu":
            kq4 = pd.DataFrame(pair4, columns=['Tuong_quan','Variable_input1', 'Variable_input2',  "corr"])
            return kq4
        elif choose == "Tất cả":
            kq1 = pd.DataFrame(pair1, columns=['Tuong_quan','Variable_input1', 'Variable_input2',  "corr"])
            kq2 = pd.DataFrame(pair2, columns=['Tuong_quan','Variable_input1', 'Variable_input2',  "corr"])
            kq3 = pd.DataFrame(pair3, columns=['Tuong_quan','Variable_input1', 'Variable_input2',  "corr"])
            kq4 = pd.DataFrame(pair4, columns=['Tuong_quan','Variable_input1', 'Variable_input2',  "corr"])
            result = kq1.append(kq2)
            result = result.append(kq3)
            result = result.append(kq4)
            return result
        else:
            print("Please check and call to me")
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

## B. PHÂN TÍCH BIẾN LIÊN TỤC VÀ BIẾN PHÂN LOẠI (Continious & Categorical)
### 3.5. Giữa biến output liên tục và biến inputs phân loại: thể hiện mức độ tương quan giữa các biến continious vs categorical có phụ thuộc nhau
##### Trường hợp là input vs input => Tương quan càng mạnh thì cần loại bỏ
##### Trường hợp là input vs output => Tương quan càng mạnh thì lấy biến input
##### Nên việc chọn các thuộc tính trong bài toán cực kỳ quan trọng
##### Có 3 kết quả để choose trong [Kết quả, Hiển thị ANOVA, Tương quan]
def tuongquanOutputContiniousAndCategorical(df, lst_phanloai, variableInput, choose ="Kết quả"):
    try:
        ## Tạo chuỗi
        prob = 0.95
        alpha = 1.0 - prob
        string = []
        for i in lst_phanloai:
            t = 'C(' + i + ')'
            string.append(t)
        string = '+'.join(string)
        ## ANOVA và chọn biến inputs phân loại có ảnh hưởng lớn đến biến output
        model = ols(variableInput+' ~ '+ string, data=df).fit()
        aov_table = sm.stats.anova_lm(model, typ=2)
        aov_table1 = aov_table[aov_table['PR(>F)'] < alpha]
        lst_phanloai_chosen = aov_table1.index.str.extract('(C\()(\w+)')[1].to_list()
        if choose == "All":
            results = [print('- Kết luận: Các thuộc tính phân loại có ảnh hướng đáng kể dến thuộc tính output (price):',
            lst_phanloai_chosen), print('Các thuộc tính có ảnh hướng đáng kể dến thuộc tính price:', '\n', aov_table1),
            print('Kiểm định ANONA giữa thuộc tính price và các thuộc tính phân loại:','\n', aov_table) ]
            return results
        elif choose == "Hiển thị ANOVA":
            return aov_table
        elif choose == "Tương quan":
            return aov_table1
        elif choose == "Kết quả":
            results = DataFrame(lst_phanloai_chosen, columns=["Ảnh hưởng đến biến continious "+variableInput])
            return results
        else:
            print("Please check again")
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")
    
### 3.6. Giữa các biến inputs phân loại và biến inputs liên tục
#### Xem mức độ tương quan của các biên phân loại vs liên tục theo 2 cách choose: [matrix, melt]
#### Matrix: thể hiện 2 biến dòng và côtj
#### melt: thể hiện theo hàng cột
def tuongquanInputVariableContiniousVsInputCategorical(df, lst_lientuc, lst_phanloai, choose="matrix"):
    try:
        ## Tạo chuỗi
        prob = 0.95
        alpha = 1.0 - prob
        names = {}
        for j in lst_lientuc:
            string = []
            name = "aovTable_"+j
            for i in lst_phanloai:
                t = 'C(' + i + ')'
                string.append(t)
            string = j + ' ~ ' + '+'.join(string)
            string

            model = ols(string, data=df).fit()
            aov_table = sm.stats.anova_lm(model, typ=2)
            aov_table1 = aov_table[aov_table['PR(>F)'] < alpha]
            name = {j: i, j: round(aov_table1['PR(>F)'],2)}
            names.update(name)
        if choose == "melt":
            result_melt = pd.DataFrame.from_dict(names).melt()
            return result_melt
        elif choose == "matrix":
            result = pd.DataFrame.from_dict(names)
            return result
        else:
            print("Check para choose = [melt or matrix]")
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

## C. PHÂN TÍCH 2 BIẾN PHÂN LOẠI
### 3.7 Biến phân loại và Biến phân loại (Categorical & Categorical)
##### Kiểm tra mức độ tương quan của 2 biến categorical: Phụ thuộc hay độc lập
##### Chọn được các trường hợp: choose [Phụ thuộc, Độc lập, Tất cả]
def tuongquan2VariableCategorical(df, lst_phanloai, choose ="Tất cả"):
    try:
        prob = 0.95
        alpha = 1.0 - prob

        pair1 = []
        pair2 = []

        for i in lst_phanloai:
            for j in lst_phanloai[lst_phanloai.index(i)+1:]:
                crosstab = pd.crosstab(df[i], df[j])
                stat, p, dof, expected = chi2_contingency(crosstab)
                #critical = chi2.ppf(prob, dof)
                if p <= alpha:
                    pair1.append(["Phụ thuộc nhau (reject H0)",i,j])
                else:
                    pair2.append(["Độc lập nhau (fail to reject H0)",i,j])
            
        if choose =="Phụ thuộc":
            kq1 = pd.DataFrame(pair1, columns=['Tuong_quan','Variable_input1', 'Variable_input2'])
            return kq1
        elif choose == "Độc lập":
            kq2 = pd.DataFrame(pair2, columns=['Tuong_quan','Variable_input1', 'Variable_input2'])
            return kq2
        elif choose == "Tất cả":
            kq1 = pd.DataFrame(pair1, columns=['Tuong_quan','Variable_input1', 'Variable_input2'])
            kq2 = pd.DataFrame(pair2, columns=['Tuong_quan','Variable_input1', 'Variable_input2'])
            result = kq1.append(kq2)
            return result.drop_duplicates()
        else:
            print("Please choose = [Phụ thuộc or Độc lập or Tất cả]")
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")