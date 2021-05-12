import pyttsx3
import PyPDF2  #pacakge for to read the pdf file
book = open('python cheat sheet.pdf','rb')  #rb = rb : Opens the file as read-only in binary format and starts reading from the beginning of the file.
pdfReader = PyPDF2.PdfFileReader(book)   #for to read the files
pages = pdfReader.numPages   #for to print page numbers
print(pages)
speaker = pyttsx3.init()  #intilazating the pyttsx3 package
for num in range (10,pages):
    page = pdfReader.getPage(9)   #for to read the particular page if u want to read 10 then enter 9 page number
    text =page.extractText()
    speaker.say(text)
    speaker.runAndWait()



#total page numbers in pdf file is 14

#uploading in  Github