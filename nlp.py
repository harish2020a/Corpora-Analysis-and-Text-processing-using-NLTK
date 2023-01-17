
#Harish B
#20BCE1417
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from collections import defaultdict
from nltk.corpus import brown
from urllib import request
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

text = brown.words()
finaltext = ' '.join([str(elem) for elem in text])

brown.words(categories='government')
print(finaltext)


print("Explore Brown Corpus and find the size, tokens, categories")
print(brown.categories())

print("Find the size of word tokens")
print(len(word_tokenize(finaltext)))

print("Find the size of the category “government” ") 
print(len(brown.words(categories='government')))

temp = defaultdict(int)
for sub in finaltext:
    for wrd in sub.split():
        temp[wrd] += 1
res = max(temp, key=temp.get)
print("Word with maximum frequency : " + str(res))

print("Count the number of sentences") 
number_of_sentences = sent_tokenize(finaltext)
print(len(number_of_sentences))


url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
type(raw)   
len(raw)
raw[:75]


print(text[31])


print(text[-12:-7])
print( text[12:70])

lorem = """The Fulton County Grand Jury said Friday an investigation of Atlanta's recent primary election produced `` no evidence '' that any irregula
rities took place ."""
 


print("\nConverted String:")
print(lorem.upper())
 


print("\nConverted String:")
print(lorem.lower())
 


print("\nConverted String:")
print(lorem.title())
 

print("\nOriginal String")
print(lorem)


path = nltk.data.find('C:\Users\Nitharshan Vijay\Downloads\dummytext.txt')
f = open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))





lower_case = finaltext.lower()
tokens = nltk.word_tokenize(lower_case)
tags = nltk.pos_tag(tokens)
counts = Counter( tag for word,  tag in tags)
print("COUNTING POS TAGS: number of tags=")
print(counts)

print("Tagging Sentences: ")
sen = nltk.sent_tokenize(finaltext)
for sent in sen:
     print(nltk.pos_tag(nltk.word_tokenize(sent)))



sentences = nltk.sent_tokenize(finaltext)

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    print(words)
    print()





for sentence in sentences:
    print(sentence)
    print()


text = [token.lower() for token in text]
print(text)



  
stop_words = set(stopwords.words('english'))
  
word_tokens = word_tokenize(finaltext)


filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
  
print(word_tokens)
print(filtered_sentence)




ps = PorterStemmer()
words = ["consultant", "consulting", "consults", "consulting", "consultative"]
  
for w in words:
    print(w, " : ", ps.stem(w)) 



lemmatizer = WordNetLemmatizer()
  
print("rocks :", lemmatizer.lemmatize("trees"))
print("corpora :", lemmatizer.lemmatize("children"))
  

print("better :", lemmatizer.lemmatize("better", pos ="a"))





stop_words = set(stopwords.words('english'))
tokenized = sent_tokenize(text)
for i in tokenized:
     
    
    
    wordsList = nltk.word_tokenize(i)
 
    
    wordsList = [w for w in wordsList if not w in stop_words]
 
    
    
    tagged = nltk.pos_tag(wordsList)
 
    print(tagged)

