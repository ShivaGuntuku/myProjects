import PyPDF2
pdfFileObj = open(r'C:\Users\gshiv\Downloads\The Key To Excellent English Speaking\The Key To Excellent Speaking.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText()) 
