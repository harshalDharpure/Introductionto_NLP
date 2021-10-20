import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize,word_tokenize
text="Hello My name is xyz can you please refer a good Book"
print("tokenize_words ")

tokenize_sent=sent_tokenize(text)
for i in tokenize_sent:
    print(i)