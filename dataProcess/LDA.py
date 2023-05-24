#!/usr/bin python3
from nltk.corpus import stopwords
import nltk

from nltk import word_tokenize, pos_tag
from gensim import corpora, models

# nltk.download('punkt')

# 1. Prepare text data
texts = ["red cooked meat is a traditional Chinese dish",
         "there are many ways to make red cooked meat",
         "red cooked meat is a dish that many people like"]

# 2. Tokenize text
texts = [word_tokenize(text) for text in texts]
print("2 . texts:", texts, "typeof:", type(texts[0]))

# texts: [['red', 'cooked', 'meat', 'is', 'a', 'traditional', 'Chinese', 'dish'],
#        ['there', 'are', 'many', 'ways', 'to', 'make', 'red', 'cooked', 'meat'],
#        ['red', 'cooked', 'meat', 'is', 'a', 'dish', 'that', 'many', 'people', 'like']]

# 3. Remove stopwords
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
print("nltk.data.path: ", nltk.data.path)
stopwords = set(stopwords.words('english'))
texts = [[word for word in text if word.lower() not in stopwords]
         for text in texts]
print("3 . texts:", texts)

# 3 . texts: [['red', 'cooked', 'meat', 'traditional', 'Chinese', 'dish'],
#            ['many', 'ways', 'make', 'red', 'cooked', 'meat'],
#            ['red', 'cooked', 'meat', 'dish', 'many', 'people', 'like']]

# 4. Create a word frequency matrix
dictionary = corpora.Dictionary(texts)

print("dictionary: ", dictionary)
corpus = [dictionary.doc2bow(text) for text in texts]
print("corpus: ", corpus)


# dictionary:  Dictionary<11 unique tokens: ['Chinese', 'cooked', 'dish', 'meat', 'red']...>

# corpus:  [
#           [(0, 1), (1, 1), (2, 1),(3, 1), (4, 1), (5, 1)],
#           [(1, 1), (3, 1), (4, 1), (6, 1), (7, 1), (8, 1)],
#           [(1, 1), (2, 1), (3, 1), (4, 1), (7, 1), (9, 1), (10, 1)]
#           ]

# 5. Train the LDA model

lda = models.LdaModel(corpus, num_topics=3, id2word=dictionary)
topics = lda.print_topics(num_words=5)
for topic in topics:
    print(topic)
    words = [word for word, tag in pos_tag(word_tokenize(topic[1])) if tag == "NN"]
    print("words", words)

'''
Important Illustration:

Once the model is trained, you can use the lda.print_topics() method to print the top words for each topic. The output of this method will be a list of tuples, where each tuple contains a topic number and a string of words that represents the topic. The topic number is an integer, and the string of words is a list of words separated by a + sign. The number before the word is weight of that word in topic.



'''

'''
# A document in the form of a list of words
document = ["Tesla is a company that specializes in electric vehicles.", 
            "Elon Musk is the CEO of Tesla.", 
            "Tesla's Model S is a popular electric car.", 
            "Tesla has a factory in Fremont, California."]

# Create a dictionary of words
dictionary = corpora.Dictionary(document)

# Convert the document into a bag-of-words representation
bow_representation = dictionary.doc2bow(document)
'''
