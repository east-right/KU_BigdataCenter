from ChatBotProject.utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing

sent = "내일 오전 10시에 짬뽕 주문하고 싶어ㅋㅋ"
p = Preprocess(userdic = "../utils/user_dic.tsv")

pos = p.pos(sent)
ret = p.get_keywords(pos, without_tag = False)
# print(ret)

ret = p.get_keywords(pos, without_tag = True)
# print(ret)



