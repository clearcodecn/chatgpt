from chatgpt.main import Chatbot
from flask import Flask
from flask import request, jsonify


config = {
#    "proxy": "http://127.0.0.1:1081",
    'session_token':'', 
}
chatbot = Chatbot(config, conversation_id=None)

def getMessage(q = '') :
    print('q = ', q)
    resp = chatbot.get_chat_response(q, output='text')
    print('a = ', resp['message'])
    return resp['message'] 



app = Flask(__name__)

@app.route("/api", methods=['POST'])
def hello_world():
    q = request.json['q']
    msg = getMessage(q = q)
    if '抱歉' in msg :
        msg = ''
    return jsonify(code=200, status=0, message='ok', data={
        'a': msg, 
        'q': q, 
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0')
