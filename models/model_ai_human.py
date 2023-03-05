from flask import jsonify
import requests

from keys import keys;

def get_ai_vs_human_response(payload):
	API_URL = keys.API_URL
	headers = keys.headers

	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


def calculate_ai_vs_human_score(input_text):
	output = get_ai_vs_human_response({
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

	chat_score = float(f'{chat_score:.4f}')
	h_score = float(f'{h_score:.4f}')

	return { 'ai': chat_score, 'human': h_score }

