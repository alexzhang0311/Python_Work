import os
import comtypes.client
from datetime import datetime

wdFormatPDF = 17
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
input = 'C:/Users/p4423/Desktop/WORD' #创建一个文件夹装需要转PDF的word文档
output = 'C:/Users/p4423/Desktop/PDF' #创建一个装PDF文件夹的文档
log = 'C:/Users/p4423/Desktop/PDF/Trans_log.txt' #创建Log地址
def Replace(s):
    return s.replace('pdf','docx')

for dirpath,dirnames,filenames in os.walk(output):
    pdf_file = filenames

f_pdf_file = list(map(Replace,pdf_file))


for dirpath,dirnames,filenames in os.walk(input):
    for file in filenames:
        if file not in f_pdf_file:
            fullpath_input = dirpath+'/'+file
            fileout = file.replace('docx','pdf')
            fullpath_output = output+'/'+fileout
            try:
                word = comtypes.client.CreateObject('Word.Application')
                doc = word.Documents.Open(fullpath_input)
                doc.SaveAs(fullpath_output, FileFormat=wdFormatPDF)
                doc.Close()
                word.Quit()
                with open(log,'a') as f:
                    f.write('\n%s,%s ,Success Transfer to PDF'%(now,file))
            except:
                with open(log,'a') as f:
                    f.write('\n%s,%s ,FileName Format Not Correct'%(now,file))
        else:
            with open(log,'a') as f:
                f.write('\n%s,%s ,PDF File Already Existed'%(now,file))
