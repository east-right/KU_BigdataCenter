# ================================================= [ Setting ] =======================================================
import tensorflow as tf
from tensorflow.keras import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
from ChatBotProject.utils.Preprocess import Preprocess
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from seqeval.metrics import f1_score, classification_report

def read_file(file_name) :
    sents = []
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for idx, l in enumerate(lines):
            if l[0] == ';' and lines[idx + 1][0] == '$':
                this_sent = []
            elif l[0] == '$' and lines[idx - 1][0] == ';':
                continue
            elif l[0] == '\n' :
                sents.append(this_sent)
            else:
                this_sent.append(tuple(l.split()))

    return sents

# ============================================ [ NER tagging modeling ] ==========================================
## + todo [ Preprocessing ] ===========================
p = Preprocess(word2_index_dic = '../../train_tools/dict/chatbot_dict.bin', userdic = '../../utils/user_dic.tsv')
corpus = read_file('ner_train.txt')

sentences, tags = [], []
for t in corpus :
    tagged_sentence = []
    sentence, bio_tag = [], []
    for w in t :
        tagged_sentence.append((w[1], w[3]))
        sentence.append(w[1])
        bio_tag.append(w[3])

    sentences.append(sentence)
    tags.append(bio_tag)

print("sample length : \n", len(sentences))
print("sample word sequence max length : ", max(len(l) for l in sentences))
print("sample word sequence mean length : ", (sum(map(len, sentences)) / len(sentences)))

tag_tokenizer = preprocessing.text.Tokenizer(lower = False)
tag_tokenizer.fit_on_texts(tags)
vocab_size = len(p.word_index) + 1
tag_size = len(tag_tokenizer.word_index) + 1
print("BIO tag dict length : ", tag_size)
print("word dict length : ", vocab_size)

x_train = [p.get_wordidx_sequence(sent) for sent in sentences]
y_train = tag_tokenizer.texts_to_sequences(tags)

index_to_ner = tag_tokenizer.index_word
index_to_ner[0] = "PAD"

max_len = 40
x_train = preprocessing.sequence.pad_sequences(x_train, padding = 'post', maxlen = max_len)
y_train = preprocessing.sequence.pad_sequences(y_train, padding = 'post', maxlen = max_len)

x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size = 0.2, random_state = 2109)
y_train = tf.keras.utils.to_categorical(y_train, num_classes = tag_size)
y_test = tf.keras.utils.to_categorical(y_test, num_classes = tag_size)

print("tarin sample sequence shape  : ", x_train.shape)
print("tarin label sample sequence shape : ", y_train.shape)
print("test sample saequence shaep : ", x_test.shape)
print("test label sample sequence shape : ", y_test.shape)

## + todo [ Bi-LSTM modeling ] ===========================
model = Sequential()
model.add(Embedding(input_dim = vocab_size, output_dim = 30, input_length = max_len, mask_zero = True))
model.add(Bidirectional(LSTM(200, return_sequences = True, dropout = 0.40, recurrent_dropout = 0.25)))
model.add(TimeDistributed(Dense(tag_size, activation = "softmax")))
model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])

es = EarlyStopping()
model.fit(x_train, y_train, batch_size = 64, epochs = 10, validation_split = 0.2)


print("model evaluate : ", model.evaluate(x_test, y_test)[1])
model.save("ner_model.h5")

## + todo [ sequence to NER tag ] ========================
def sequences_to_tag(sequences) :
    result = []
    for sequence in sequences :
        temp = []
        for pred in sequence :
            pred_index = np.argmax(pred)
            temp.append(index_to_ner[pred_index].replace("PAD", "0"))
            result.append(temp)

    return result

y_predicted = model.predict(x_test)
pread_tags = sequences_to_tag(y_predicted)
test_tags = sequences_to_tag(y_test)

print(classification_report(test_tags, pread_tags))
print("F1-socre : {:.1%}".format(f1_score(test_tags, pread_tags)))
