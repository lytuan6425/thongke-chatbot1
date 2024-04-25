import PyPDF2

with open('thongke.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	text = ''
	for page in range(reader.numPages):
		text += reader.getPage(page).extractText()
