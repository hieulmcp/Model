Feature_Engineering ='''
    A. Xử lý categorical và Continiuos
        1. Giới thiếu chung
            - Feature engineering: dùng domain business để tạo ra các tính năng giúp thuật toán máy học hoạt động
            - Cung cấp 1 số thư vện để chuyển đổi kiểu dữ liệu categorical từ dạng object sang kiểu dữ số
            - Giúp cho chung ta có thể truy vết nếu có vấn đề
            - Vậy vì sao phải chuyển qua kiểu category từ text sang dạng số ?
                * Tiết kiệm bộ nhớ
                * Các thuật toán Machine learning sẽ thao tác một cách nhanh hơn kiểu dữ liệu object
                * Bản chất thì chuyển qua kiểu dữ liệu category nhưng bản chất bên trong là kiểu object nên phải chuyển qua kiểu số để thuật toán ML thực hiện
        2. Đặc điểm
            - Feature engineering là việc tạo các tính năng đầu vào mới từ những tính năng hiện có của bộ dữ liệu
            - Đây là một trong những nhiệm vụ có giá trị nhất ma một nhà khoa học dữ liệu có thể làm để cải thiện hiệu suất mô hình
                * Chúng ta có thể làm cô lập và làm nổi bật thông tin chính, giúp thuật toán tập trung vào nhưng gì quan trọng
                * Chúng ta có thể vận dụng domain knowledge để có tính năng thích hợp
                * Chúng ta cũng có thể đem đến những người khác kiến thức mới và domain knowledge mới
        3. Domain knowledge
            - Chúng ta có thể thiết kế các thuộc tính thông tin (informative feature) 
            bằng cách dựa trên kiến thức chuyên môn của mình (hoặc những người khác) về lĩnh vực làm việc
            - Với những thông tin cụ thể mà ta có thể muốn cô lập, ta có thế có rất nhiêu tự do và sáng tạo
            - Domain knowledge rất rộng mở. Khi đó chũng ta có thể cạn kiệt về ý tưởng. Và có 1 số phương pháp phỏng đoán cụ thể giúp gợi mở nhiều hơn
        4. Tạo thuộc tính
            - Trong phần này chúng ta sẽ tìm hiểu các kỹ thuật liên quan đến thuộc tính tính năng (feature engineering) 
            và cách áp dụng nó vào dữ liệu trong thế giới thực
            - Chung ta sẽ tải, khám phá và trực quan hóa bộ dữ liệu, tìm hiểu về các loại dữ liệu cơ bản của chúng
            và lý do tại sao chúng có ảnh hưởng đến cách chúng ta thiết kế các thuộc tính của 
            a. Các kiểu dữ liệu khác nhau
                - Continuous: dữ liệu liên tục có thể là integer hoặc float
                - Categorical: dữ liệu phân loại, là tập hợp giá trị giới hạn: gender, country of birth
                - Ordinal: Giá trị xếp hạng, thường không có chi tiết về khoảng cách giữa chúng
                - Boolean: giá trị True/False
                - Datetime: giá trị thời gian
            b. Các thuộc tính thông dụng
                - df.columns: xem danh sách tên cột
                - df.dtypes: xem danh sách kiểu dữ liệu của cột
                - Chọn các cột có kiệu dữ liệu cụ thể: df2 = df.select_dtypes(include = ['int','float']) => df2.columns
        5. Chuyển đội dữ liệu
            - Integer encoder/ label encoder
                * Áp dụng trong kiểu phân loại và theo thứ tự
            - One hot encoder/ Dummy encoder
                * Đối với các biến phân loại không tồn tại mối quan hệ thứ tự, integer encoder là không đủ
                * Tuy thuộc vào dữ liệu chúng ta có, chung ta có thể gặp phải tình huống, sau khi Laber Encoder, 
                có thể nhầm lẫn mô hình vì nghĩ rằng một cột có dữ liệu với thứ tự hoặc thứ bậc nào đó.
                * One-hot encoder/ Dummy encoder có thể áp dụng thay cho biểu diễn số nguyên => kết quả giống nhau cách thức thực hiện khác nhau
            - One hot encoder      
                Bước 1: Xác định thuộc tính phân loại và không có thứ tự
                Bước 2: Import thêm thư viện vào
                Bước 3: Khởi tạo thư viện onehotencoder()
                Bước 4: Biển thuộc tính cần biến đổi theo mảng 2 chiều
                Bước 5: Truy ngược lại dữ liệu
            - Dummy encoder
                - Xử lý đơn giản hơn onehot encoder
                - Không lưu trữ dummy model encoder
                - Kết quả trả về là các cột mới trong dataFrame
                - Xử lý đơn giản đó là 1 phương thức của pandas không phải là model nên không thể truy ngược lại được
        6. Mục đích binning value
            - Đối với nhiều giá trị liên tục chúng ta có thể sẽ quan tâm ít hơn về giá trị chính xác của một cột kiểu số, thay vào đó chung ta quan tâm
            đến nhóm mà nó rơi vào => Điều này hữu ích khi vẽ các giá trị hoặc đơn giản hóa các mô hình ML Nó chủ yếu được sử dụng trên các biến liên tục 
            trong đó dộ chính xác không phải mối quan tâm lớn nhất. Tạo khoảng tuổi, chiều cao, tiền lương
            - Động lực chính của việc tao bin là làm cho mô hình mạnh mẽ hơn và ngăn ngừa overfitting, tuy nhiên, nó có chi phí hiệu suất cao hơn
            => Mỗi khi chúng ta dùng bin thì phải chấp nhận giảm bớt thông tin cho trường đó
            - Sự đánh đổi giữa hiệu suất và overfitting là điểm mẫu chốt của quá trình tạo bin
            => Nhìn chung chung ta có các cột số, ngoại trừ một số trường hợp quá rõ ràng, việc tạo bin có thể là dư thừa đối với một số loại thuật toán
            do ảnh hưởng của nó đến hiệu suất mô hình
            - Đối với các cột phân loại các nhãn có tần số thấp có thể ảnh hưởng tiêu cực đến độ mạnh của các mô hình thống kê.
            => Do đó việc gán danh mục chung cho các giá trị ít thường xuyên này sẽ giúp duy trì sức mạnh mẽ của mô hình
            - Các bin được tạo ra bằng cách sử dụng pd.cut(df['column_name'], bins) => Trong đó bins là integer chỉ định số lượng bin cách đều nhau hoặc đó 
            danh giới của bin
        7. Xử lý các danh mục không phổ biến (uncommon category)
            Một số tính năng có thể có nhiều loại khác nhau những phân phối rất không đồng đều về sự xuất hiện của chúng
    B. Xử lý dữ liệu văn bản (Text data)
        1. Các xử lý văn bản - text data
            - Dữ liệu văn bản phi cấu trúc có thể được sử dụng trực tiếp trong hầu hết các phân tích
                Bước 1: Chuẩn hóa dữ liệu và loại bỏ các ký tự nào có thể gây ra sự cố sau này trong việc phân tích của bản
                    - Loại bỏ những ký tự không mong muốn 
                        * Dùng regular expression:
                            + [a-zA-Z]: Tất cả các ký tự chữ
                            + [^a-zA-Z]: tất cả các ký tự không phải là ký tự chữ
                    - Chuẩn hóa chữ: dùng str.lower(): chuyển sang chữa thường
                Bước 2: Thuộc tính văn bản cấp cao (High level text feature)
                    - Khi văn bản đã được làm sạch và chuẩn hóa, chung ta có thể bắt đầu tạo các tính năng từ dữ liệu.
                    => Dùng các tính năng độ dài và số lượng tử
                        * Dùng str.len() biết chiều dài của chuỗi
                        * Dùng str.split() để cắt chuỗi thành các phần tử chữa trong list
                Bước 3: Word count Representation
                    - Khi thông tin cấp cao đã được ghi lại, chúng ta có thể bắt đầu tạo các thuộc tính dữ trên nội dung thực tế của từng văn bản
                    - Một cách để làm là tiếp cận nó theo cách tương tự như cách đã làm việc với các biến phân loại
                        * Đối với mỗi từ duy nhất trong tập dữ liệu tạo ra một cột
                        * Đối với entry, số lần từ này xuất hiện được đếm và giá trị đếm được nhập vào cột tương ứng
                    - Các cột count này có thể được sử dụng để huấn luyện các mô hình machine learning
                    - Kỹ thuật này được gọi là bag of words
        2. Dùng CountVectorizer
            - Các bước thực hiện trong thư viện
                Bước 1: Khởi tọa CountVectorizer
                Bước 2: fit
                Bước 3: Chuyển đổi văn bản
                Bước 4: Chuyển đổi kết quả các cột trong dataframe
                Note:
                    - CountVectorizer bổ sung tham số min_df và max_df
                    - Như vậy dùng CountVectorizer mặc định sẽ tạo ra một tính năng cho mỗi từ đơn lẻ trong kho văn bản
                    => Nó tạo ra nhiều thuộc tính, bao gồm các giá trị cũng cấp rất ít giá trị phân tích
                    - Cho nên min_df và max_df dùng để giảm dố lượng thuộc tính không cần thiết:
                        * min_df: Chỉ sử dụng những từ xuất hiền nhiều hơn tỷ lệ phần trăm tài liệu => Loại bỏ những từ ít hơn không khái quán được văn bản
                        * max_df: Chỉ sử dụng các từ xuất hiện ít hơn tỷ lệ phần % tài liệu này => Việc này làm giảm bớt những từ phổ biến xãy ra trong văn bản
                        mà không có thêm giá trị "and" hoặc "the"
                        VD: min_df > 20% và max_df < 80%
                Bước 5: Gộp dataFrame
                    df_new = pd.concat([df1, df2], axis=1, sort=False)
        3. Dùng TF-IDF
            - Tf-Idf (Term frequency-inverse document frequency)
                * Xử lý ngôn ngữ tự nhiên là một kĩ thuật quan trọng nhằm giúp máy tính hiểu được ngôn ngữ của con người,
                qua đó hướng dẫn máy tính thực hiện và giúp đỡ con người trong những công việc có liên quan đến ngôn ngữ như:
                dịch thuật, phân tích dữ liệu văn bản, nhân dạng tiếng nói, tìm kiếm thông tin, tóm tắt vắn bản...
                * Một trong những kĩ thuật để xử lý ngôn ngữ tự nhiên là TF-IDF (Tần xuất xuất hiện của từ nghịch đảo tần xuất suất của văn bản)
                * Mặc dù số lần xuất hiện của các từ có thể có ích khi xây dựng các mô hình, các từ xuất hiện nhiều lần có thể làm sai lệch kết quản
                một cách không mong muốn => TF-IDF có tác dụng làm giảm giá trị của các từ phổ biến, đồng thời tăng trọng số của các từ không xảy
                ra trong nhiều tài liêu
                * TF-IDF: là trọng số của một từ trong văn bản thu được qua thống kê, nó thể hiện mức độ quan trọng của từ trong một văn bản, 
                với bản thân văn bản đang xét nằm trong một tập hợp các văn bản
                * IF-IDF thường được sử dụng vì: trong ngôn ngữ luôn có những từ xảy ra thường xuyên với các từ khác
'''

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
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# sử dụng thư viện CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# A. FEATURE ENGINEERING
## 1.1. Get dummy: dùng để gán nhãn cho thuộc tính của thư viện pandas
def get_dummies(df, feature_get_dum, prefix):
    df_new = pd.get_dummies(data=df, columns=[feature_get_dum], prefix=prefix)
    return df_new

## 1.2. Label_Encoder: Áp dụng trong kiểu phân loại và theo thứ tự
def label_Encoder(df, name_before_label_encoder, name_after_label_encoder):
    encoder = LabelEncoder()
    df[name_after_label_encoder] = encoder.fit_transform(df[name_before_label_encoder])
    return df

## 1.3. MixMaxScaler: Có outlier và Không có phân phối chuẩn hoặc lệch chuẩn 
### Biến đổi bằng Dummy Encoder/OneHotEncoder
def onehotencoder(x, lst_phanloai_chosen):
    encoder = OneHotEncoder()
    lst_encode = lst_phanloai_chosen
    # lst_encode.remove('symboling')
    arr = encoder.fit_transform(x[lst_encode]).toarray()
    cols = []
    n = 0
    for i in encoder.categories_:
        for j in i[1:]: 
            t = 'oh_' + lst_encode[n] + '_' +j
            t = t.replace('-', '_')
            cols.append(t)
        n = n+1

    X_oh_encode = pd.DataFrame(arr, columns=cols)
    return X_oh_encode

## 1.4. Binning Value: Rất quan trong dùng để xem mức độ chia dữ liệu thế nào trong dữ liệu continious
def binning_value(df, name_before_binning_value, name_after_binning_value, bins ):
    df[name_after_binning_value] = pd.cut(df[name_before_binning_value], bins=bins) 
    return df


## B. XỬ LÝ DỮ LIỆU TEXT TIẾNG ANH
### 2.1. Xử lý dữ liệu text
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

### 2.2. Check ngôn ngữ tiếng anh
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

### 2.3. Remove features
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

### 2.4. removes stop words
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

### 2.5. Tagging text - Gắn thẻ vẵn bản
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

### 2.6. lemmatization
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

### 2.7. CountVectorizer: dùng để phân chia data text thành các chữa
def countVectorizer(df, var_feature_CountVectorizer,min_df=0.2, max_df=0.8):
    # khởi tạo
    cv = CountVectorizer(min_df=min_df, max_df=max_df)
    cv_transformed = cv.fit_transform(df[var_feature_CountVectorizer])
    cv_transformed = cv_transformed.toarray()
    # print(cv.get_feature_names())
    cv_df_new = pd.DataFrame(cv_transformed, columns=cv.get_feature_names()).add_prefix('cv_')
    return cv_df_new

### 2.8. TF-IDF
def tf_Idf(df, var_feature_CountVectorizer, max_features=200, stop_words='english'):
    tf_idf = TfidfVectorizer(max_features=max_features, stop_words=stop_words)
    tf_transformed = tf_idf.fit_transform(df[var_feature_CountVectorizer])
    tf_transformed = tf_transformed.toarray()
    tf_df = pd.DataFrame(tf_transformed, columns=tf_idf.get_feature_names()).add_prefix('tf_')
    return tf_df

### 2.9. TF_IDF với ngram_range
def tf_Idf_ngram_range(df, var_feature_CountVectorizer, max_features=200, stop_words='english',ngram_range=(2,2)  ):
    tf_idf = TfidfVectorizer(max_features=max_features, stop_words=stop_words, ngram_range=ngram_range)
    tf_transformed = tf_idf.fit_transform(df[var_feature_CountVectorizer])
    #print(tf_idf.get_feature_names())
    tf_transformed = tf_transformed.toarray()
    tf_df = pd.DataFrame(tf_transformed, columns=tf_idf.get_feature_names()).add_prefix('tf2_')
    return tf_df

# 2.9. Concat nhiều database
# X_new = pd.concat([X_oh_encode, X[lst_lientuc_chosen], X_not_encode], axis=1)
def concatdf(new_data, df):
    X_new = pd.concat([new_data, df], axis=1)
    return X_new

