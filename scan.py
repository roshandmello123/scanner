import PyPDF2
a=PyPDF2.PdfFileReader('football.pdf')
print(a.documentInfo)
str=""
for i in range(1,11):
    str=str+a.getPage(i).extractText()
print(str)
f=open("text.txt",mode='w')
f.write(str)
