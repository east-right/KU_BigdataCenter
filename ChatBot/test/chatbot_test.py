from ChatBotProject.config.DatabaseConfig import *
from ChatBotProject.utils.Database import Databse
from ChatBotProject.utils.Preprocess import Preprocess
from ChatBotProject.models.intent.IntentModel import IntentModel
from ChatBotProject.models.ner.NerModel import NerModel
from ChatBotProject.utils.FindAnswer import FindAnswer


p = Preprocess(word2_index_dic = "../train_tools/dict/chatbot_dict.bin", userdic = "../utils/user_dic.tsv")
db = Databse(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, db_name = DB_NAME)
db.connect()

## + todo [ intent classification ] ============
query = "모니터 구매 하려고 하는데요 "
intent = IntentModel(model_name = "../models/intent/intent_model.h5", preprocess = p)
predict = intent.predict_class(query)
intent_name = intent.labels[predict]

## + todo [ NER tagging Prediction ] ===========
ner = NerModel(model_name = "../models/ner/ner_model.h5", preprocess = p)
predicts = ner.predict(query)
ner_tags = ner.predict_tags(query)

print("질문 : ", query)
print("=" * 40)
print("의도 파악 : ", intent_name)
print("개채명 인식 : ", predicts)
print("답변 검색에 필요한 NER 태그 : ", ner_tags)
print("=" * 40)

## + todo [ serch answer ] =====================
try :
    f = FindAnswer(db)
    answer_text, answer_image = f.search(intent_name, ner_tags)
    answer = f.tag_to_word(predicts, answer_text)

except :
    answer = "죄송합니다. 무슨 말인지 모르겠어요."
print("답변 : ", answer)

db.close()