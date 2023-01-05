import pickle
from ChatBotProject.utils.Preprocess import Preprocess

f = open("../train_tools/dict/chatbot_dict.bin", "rb")
word_inddex = pickle.load(f)
f.close()

sent = "내일 오전 10시에 탕수육 주문하고 싶어 ㅋㅋㅋ"
p = Preprocess(userdic = "../utils/user_dic.tsv")
pos = p.pos(sent)

keywords = p.get_keywords(pos, without_tag = True)
for word in keywords :
    try :
        print(word, word_inddex[word])

    except KeyError :
        print(word, word_inddex["OOV"])