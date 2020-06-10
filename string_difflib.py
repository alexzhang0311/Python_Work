import difflib
import pandas as pd

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 1000)
pd.set_option("display.max_colwidth",1000)
pd.set_option('display.width',1000)


def string_similar(s1,s2):
    return difflib.SequenceMatcher(None,s1,s2).quick_ratio()


filepath = 'C:/Users/p4423/Desktop/noc_operation_email_data.xlsx'


raw_data = pd.read_excel(filepath, index_col=None)


process_data = raw_data[raw_data['Subject_ID'].notna()]

#process_data[['Subject_ID']] = process_data[['Subject_ID']].astype(int)

process_data.loc[:,['Subject_ID']] = process_data.loc[:,['Subject_ID']].astype(int)


base = 'Fraud call 852- from PCCWG on 20200527 [CMHKNOC-76867][INC1756737] - 4.msg'




for index,row in process_data.iterrows():
    print(row['Subject'])





# for Subject in process_data['Subject']:
#     if string_similar(base,Subject) >= 0.95:
#         percent = string_similar(base,Subject)
#         #process_data['置信度'] = percent
#         print(Subject,percent)

#print(raw_data)


#process_data.apply(string_similar(base, process_data[3]))


#print(process_data.apply(string_similar, (base, process_data[3])))


#print(process_data)

https://www.cnblogs.com/zhouziyuan/p/10137086.html
