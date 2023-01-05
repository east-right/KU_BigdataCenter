# ================================================= [ Setting ] =======================================================
import threading
import json

from ChatBotProject.config.DatabaseConfig import *
from ChatBotProject.utils.Database import Databse
from ChatBotProject.utils.BotServer import BotServer
from ChatBotProject.utils.Preprocess import Preprocess
from ChatBotProject.models.intent.IntentModel import IntentModel
from ChatBotProject.models.ner.NerModel import NerModel
from ChatBotProject.utils.FindAnswer import FindAnswer

# ============================================== [ load Models ] =====================================================
p = Preprocess(word2_index_dic = "./train_tools/dict/chatbot_dict.bin", userdic = "./utils/user_dic.tsv")
intent = IntentModel(model_name = "./models/intent/intent_model.h5", preprocess = p)
ner = NerModel(model_name = "./models/ner/ner_model.h5", preprocess = p)

def to_client(conn, addr, params) :
    db = params['db']
    try :
        db.connect()
        read = conn.recv(2048) # 데이터 수신
        print("===============================")
        print("Connection form : %s" % str(addr))

        if read is None or not read :
            print("Client don't connection your server")
            exit(0)

        ## todo + [ json to data ] =========
        recv_json_data = json.loads(read.decode())
        print("read Data : ", recv_json_data)
        query = recv_json_data["Query"]

        ## todo + [ prediction Intent ] =====
        intent_predict = intent.predict_class(query)
        intent_name = intent.labels[intent_predict]

        ## todo + [ NER tag classification ] ======
        ner_predicts = ner.predict(query)
        ner_tags = ner.predict_tags(query)

        ## todo + [ serch answer ] =================
        try :
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(ner_predicts, answer_text)

        except :
            answer = "죄송합니다 ㅠㅠ 무슨말인지 모르겠어요. 조금 더 공부할게요. "
            answer_image = None

        send_josn_data_str = {'Query' : query,
                              'Anwer' : answer,
                              'AnswerImageUrl' : answer_image,
                              'Intent' : intent_name,
                              "NER" : str(ner_predicts)}

        message = json.dumps(send_josn_data_str)
        conn.send(message.encode())

    except Exception as ex :
        print(ex)

    finally :
        if db is not None :
            db.close()
        conn.close()

## + todo [ 질문 / 답변 학습 DB 연결 객체 형성 ]
if __name__ == "__main__" :
    db = Databse(host = DB_HOST, user = DB_USER, password = DB_PASSWORD, db_name = DB_NAME)
    print("DB connection")

    port = 5050
    listen = 100
    bot = BotServer(port, listen)
    bot.create_sock()
    print("bot start")

    while True :
        conn, addr = bot.ready_for_client()
        params = {'db' : db }

        client = threading.Thread(target = to_client, args = (conn, addr, params))
        client.start() # start thread