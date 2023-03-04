import requests
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/mrm8488/xlm-roberta-base-finetuned-HC3-mix"
headers = {"Authorization": f"Bearer {'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'}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['text']
        output = query({
            "inputs": input_text,
        })
        human_score = next((item for item in output[0] if item["label"] == "Human"), None)
        chatgpt_score = next((item for item in output[0] if item["label"] == "ChatGPT"), None)
        h_score = human_score["score"]
        chat_score = chatgpt_score["score"]
        #print("h_score:", h_score, type(h_score))
        #print("chat_score:", chat_score, type(chat_score))
        #h_score_new = float(round(float(h_score), 2))
        #chat_score_new = float(round(float(chat_score), 2))
        return render_template('index.html', h_score=h_score, chat_score=chat_score)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
