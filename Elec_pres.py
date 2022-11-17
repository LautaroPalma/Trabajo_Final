import PyPDF2
 
file = open('Mano_de_obra.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(file)
  
# printing number of pages in pdf file
print("Total number of pages in sample.pdf",pdfReader.numPages)
  
# creating a page object
pageObj = pdfReader.getPage(0)
# extracting text from page
print(pageObj.extractText())
  
# closing the pdf file object
file.close()