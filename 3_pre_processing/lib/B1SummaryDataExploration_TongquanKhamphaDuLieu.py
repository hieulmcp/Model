import pandas as pd 
import warnings
import pandas_profiling as pp # tổng quan ban đầu về dữ liệu => Cài trên này
warnings.filterwarnings('ignore')
import re
import string
import langid # Dùng để xem ngôn ngữ nước nào
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import time

Note = '''
    A. Data exploration - Khám phá dữ liệu
    1. Khám phá dữ liệu vì sao thực sự quan trọng ?
        - Một bước trong quá trình khám phá dữ liệu (Data clearning)
        - Khi làm việc với machine learning phải vật lộn để cải thiện độ chính xác của mô hình
        - Khám phá dữ liệu là bước cực kỳ quan trọng => Ảnh hưởng đến chất lượng input (biến đầu vào) => Dự báo được biến đầu ra
        - Chất lượng input đầu vào sẽ quyết định chất lượng biến đầu ra target (input)
        - Thời gian khám phá dữ liệu và làm sách dữ liệu chiếm phần lớn dự án đến gần 70% đến 80%       
'''
## A. LOAD DATA
### 1.1. Load data: dùng để load data các file đuôi csv, xlsx, json
def loadData(file_dir="", names=""):
    try:
        file_dir = file_dir.lower()
        if file_dir.endswith("csv"):
            df = pd.read_csv(file_dir, names=names)
            return df
        elif file_dir.endswith("xlsx"):
            df = pd.read_excel(file_dir, names=names)
            return df
        elif file_dir.endswith("json"):
            df = pd.read_json(file_dir, names=names)
            return df
        else:
            print("Please see file and path")
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

## B. TỔNG QUAN VỀ DỮ LIỆU
### 1.2. Tổng quan về thông tin ban đầu: info; nan; head; tail; shape; null; profile; dtypes... theo if elif else
def startInformation(df, choose, head =10, tail = 10):
    try:
        # Xem info
        if choose == "info":
            info = df.info()
            return info
        # Xem dữ liệu trống
        elif choose == "nan":
            nan = df.isna().sum()
            return nan
        # Xem 10 dữ liệu đầu
        elif choose == "head":
            head = df.head(head)
            return head
        # Xem 10 dữ liệu đầu
        elif choose == "tail":
            head = df.tail(tail)
            return head
        elif choose == "shape":
            shapes_ = df.shape
            return shapes_
        elif choose == "null":
            # Xem giá trị null
            null_ = df.isnull().sum()
            return null_
        elif choose == "profile":
            # Nhìm tổng quan về báo cáo
            profile = pp.ProfileReport(df)
            return profile
        elif choose == "dtypes":
            dtypes_ = df.dtypes
            return dtypes_
        else:
            print("Please see file")
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 1.3. % dữ liệu trùng: Xem tỉ lệ % dữ liệu trùng
def percentDuplicates(df):
    try:
        shapeBefore = df.shape
        countBefore = shapeBefore[0]
        data = df.drop_duplicates()
        shapeAfter = data.shape
        countAfter = shapeAfter[0]
        variableCount = countBefore - countAfter
        if variableCount == 0:
            result_ = 0
            return result_
        elif variableCount != 0:
            result_ = round(variableCount/countBefore,2)
            return  result_
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 1.4. Loại bỏ dữ liệu trùng
def deleteDuplicates(df):
    try:
        data = df.drop_duplicates()
        return  data
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 1.5. Xử lý dữ liệu (missing values)
def checkDtypesDataAndMissingvalues(df, chooses, index_=2, columns1 = ['Kiểm tra biến','giá trị', 'Số biến','Kiểu dữ liệu']):
    try:
        lists_ = []
        for i in df.columns:
            if len(df[i].unique()) > index_:
                if chooses == "print":
                    print('\033[4m'+'Kiểm tra biến', i +'\033[0m', ': ', len(df[i].unique())[:index_], 'giá trị,', 
                    df[i].sort_values().unique(), ', dtype:', df[i].dtypes)
                    #list_ = [i, len(df[i].unique()), df[i].sort_values().unique(), df[i].dtypes]
                    #lists_.append(list_)
                    #result_ = pd.DataFrame(list_)
                    #return lists_
                elif chooses == "table":
                    list_ = (i, len(df[i].unique()), df[i].sort_values().unique()[:index_], df[i].dtypes)
                    lists_.append(list_)
                    result_ = pd.DataFrame(lists_, columns=columns1)
                else:
                    print("Please check again !!!!")
            else:
                if chooses == "print":
                    print('\033[4m'+'Kiểm tra biến', i +'\033[0m', ': ', len(df[i].unique()), 'giá trị,', df[i].sort_values().unique(), ', dtype:', df[i].dtypes)
                    #list_ = [i, len(df[i].unique()), df[i].sort_values().unique(), df[i].dtypes]
                    #lists_.append(list_)
                    #result_ = pd.DataFrame(list_)
                    #return lists_
                elif chooses == "table":
                    list_ = (i, len(df[i].unique()), df[i].sort_values().unique(), df[i].dtypes)
                    lists_.append(list_)
                    result_ = pd.DataFrame(lists_, columns=columns1)
                else:
                    print("Please check again !!!!")
        return result_
            
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

## C. XỬ LÝ DỮ LIỆU TEXT TIẾNG ANH
### 1.6. Xử lý dữ liệu text
##### Check to see if a row only contains whitespace
##### Kiểm tra và nhìn thấy dữ liểu có chứa khoảng trắng
def check_blanks(data_str):
    try:
        is_blank = str(data_str.isspace())
        return is_blank
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 1.7. Check ngôn ngữ tiếng anh
##### Determine whether the language of the text content is english or not: Use langid module to classify
##### the language to make sure we are applying the correct cleanup actions for English langid
##### Kiểm tra ngôn ngữ English
def check_lang(data_str):
    try:
        predict_lang = langid.classify(data_str)
        if predict_lang[1] >= .9:
            language = predict_lang[0]
        else:
            language = 'NA'
        return language
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 1.8. Remove features
##### Remove những dữ liệu có chứa những ký tự đặc biệt và các ký tự không cần thiết
def removeFeatures(dataStr):
    try:
        # compile regex
        url_re = re.compile('https?://(www.)?\w+\.\w+(/\w+)*/?')
        punc_re = re.compile('[%s]' % re.escape(string.punctuation))
        num_re = re.compile('(\\d+)')
        mention_re = re.compile('@(\w+)')
        alpha_num_re = re.compile("[^A-Za-z0-9]") # Kiểu phủ định khác các chữ cái trên tron ^ là kiểu phủ đỉnh
        # convert to lowercase
        dataStr = dataStr.lower()
        # remove hyperlinks
        dataStr = url_re.sub(' ', dataStr)
        # remove @mentions
        dataStr = mention_re.sub(' ', dataStr)
        # remove puncuation
        dataStr = punc_re.sub(' ', dataStr)
        # remove numeric 'words'
        dataStr = num_re.sub(' ', dataStr)
        # remove non a-z 0-9 characters and words shorter than 3 characters
        list_pos = 0
        cleaned_str = ''
        for word in dataStr.split():
            if list_pos == 0:
                if alpha_num_re.match(word) and len(word) > 2:
                    cleaned_str = word
                else:
                    cleaned_str = ' '
            else:
                if alpha_num_re.match(word) and len(word) > 2:
                    cleaned_str = cleaned_str + ' ' + word
                else:
                    cleaned_str += ' '
            list_pos += 1
        return cleaned_str
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 1.9. removes stop words
##### removes stop words, phải lập những từ xuất hiền nhiều không có ý nghĩa
def remove_stops(data_str):
    try:
        # expects a string
        stops = set(stopwords.words("english"))
        list_pos = 0
        cleaned_str = ''
        text = data_str.split()
        for word in text:
            if word not in stops:
            # rebuild cleaned_str
                if list_pos == 0:
                    cleaned_str = word
                else:
                    cleaned_str = cleaned_str + ' ' + word
                list_pos += 1
        return cleaned_str
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 1.10. Tagging text - Gắn thẻ vẵn bản
def tag_and_remove(data_str):
    try:
        cleaned_str = ' '
        # noun tags
        nn_tags = ['NN', 'NNP', 'NNP', 'NNPS', 'NNS']
        # adjectives
        jj_tags = ['JJ', 'JJR', 'JJS']
        # verbs
        vb_tags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
        nltk_tags = nn_tags + jj_tags + vb_tags
        # break string into 'words'
        text = data_str.split()
        # tag the text and keep only those with the right tags
        tagged_text = pos_tag(text)
        for tagged_word in tagged_text:
            if tagged_word[1] in nltk_tags:
                cleaned_str += tagged_word[0] + ' '
        return cleaned_str
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

### 1.11. lemmatization
def lemmatize(data_str):
    try:
        # expects a string
        list_pos = 0
        cleaned_str = ''
        lmtzr = WordNetLemmatizer()
        text = data_str.split()
        tagged_words = pos_tag(text)
        for word in tagged_words:
            if 'v' in word[1].lower():
                lemma = lmtzr.lemmatize(word[0], pos='v')
            else:
                lemma = lmtzr.lemmatize(word[0], pos='n')
            if list_pos == 0:
                cleaned_str = lemma
            else:
                cleaned_str = cleaned_str + ' ' + lemma
            list_pos += 1
        return cleaned_str
    except Exception as failGeneral:
        print("Fail system, please call developer...", type(failGeneral).__name__)
        print("Mô tả:", failGeneral)
    finally:
        print("close")

## D. XỬ LÝ MISSING VALUE
### 1.11. Xử lý dữ liệu số với mean/ mode/ median => thay thế dữ liệu missing value bằng các giá trị mean/median/mode
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

### 1.12. Filter special character: Tỉm kiếm các ký tự đặc biệt trong kiểu dữ liệu object
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

### 1.14. Chuyển đổi kiểu dữ liệu cho thuộc tính: change astype for feature 
def changeToAstype(df, lst_int, lst_float):
    # Chuyển thành kiểu số int và float cho các biến kiểu số
    lst_int = lst_int
    lst_float = lst_float
    df[lst_int] = df[lst_int].astype(int)
    df[lst_float] = df[lst_float].astype(float)
    info = df.info()
    return info

### 1.15. Xử lý dữ liệu thiếu của các biến phân loại: add value for value failing
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

### 1.16. Xem mực độ chạy dữ liệu với thời gian ban đâu
def time_project():
    time_ = time.time()
    return time_


