# ================================================= [ Setting ] =======================================================
from ChatBotProject.utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

## todo + [ corpus data load ] =================================
def read_corpus_data(filename, encoding) :
    with open(filename, 'r', encoding = encoding) as f :
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1: ]
    return data

## todo + [ keyword parsing ] =================================
corpus_data = read_corpus_data('./corpus.txt', encoding = "utf-8")
p = Preprocess
dict = []

for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        dict.append(k[0])

tokenizer = preprocessing.text.Tokenizer(oov_token = 'OOV')
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

## todo + [ Make word index to use dict ] =================================
f = open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)

except Exception as e:
    print(e)

finally:
    f.close()