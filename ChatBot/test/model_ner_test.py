from ChatBotProject.utils.Preprocess import Preprocess
from ChatBotProject.models.ner.NerModel import NerModel

p = Preprocess(word2_index_dic = "../train_tools/dict/chatbot_dict.bin", userdic = "../utils/user_dic.tsv")
ner = NerModel(model_name = "../models/ner/ner_model.h5", preprocess = p)
query = "내일오전에 주문 하려고 하는데 .."

predicts = ner.predict(query)
print(predicts)