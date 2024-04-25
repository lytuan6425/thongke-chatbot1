import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open('thongke.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	text = ''
	for page in range(reader.numPages):
		text += reader.getPage(page).extractText()

# Tokenize the text
tokens = word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token not in stop_words]

# Join the filtered tokens back into a string
preprocessed_text = ' '.join(filtered_tokens)
