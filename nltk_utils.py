import nltk
import numpy as np
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()


def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenze_sentence,all_words):
    """
    sentence=['hello','how','are','you']
    words=['hi','hello','I','you','bye']
    bag=[  0   ,   1   ,   0   ,   1  ,  0   ]

    """
    tokenze_sentence=[stem(w) for w in tokenze_sentence]
    bag = np.zeros((len(all_words),), dtype=np.float32)

    for idx,w,in enumerate(all_words):
        if w in tokenze_sentence:
            bag[idx]=1.0

    return bag




# sentence=['hello','how','are','you']
# words=['hi','hello','I','you','bye']
# bag=bag_of_words(sentence,words)
# print(bag)




# a="How long does it take ?"
# print(a)
# a=tokenize(a)
# print(a)

# words=["organization","organize","organizes"]
# stemmed=[stem(w) for w in words ]
# print(stemmed)