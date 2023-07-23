import requests
import json
from flask import Flask
import threading
import time

app = Flask(__name__)


def generate_response(message, user_name):
    api_endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    headers = {
        'Authorization': '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',
        'Content-Type': 'application/json'
    }

    # Modify the prompt to include a rhyming requirement
    prompt = f"Write a rhyming response for{message}\n @{user_name}，try to sound philosophical"


    data = {
        'prompt': prompt,
        'max_tokens': 150  # Adjust according to your needs
    }

    response = requests.post(api_endpoint, headers=headers, json=data)
    response_data = response.json()

    return response_data['choices'][0]['text'].strip()


def send_response_to_weibo(response, user_name):
    api_endpoint = 'https://api.weibo.com/2/statuses/update.json'
    headers = {
        'Authorization': 'OAuth2 YOUR_WEIBO_API_KEY',
        'Content-Type': 'application/json'
    }
    data = {
        'status': f"@{user_name} {response}"
    }

    requests.post(api_endpoint, headers=headers, json=data)


def check_mentions():
    last_id = 0  # Start from the first mention
    api_endpoint = 'https://api.weibo.com/2/statuses/mentions.json'
    headers = {
        'Authorization': '******'
    }
    params = {
        'since_id': last_id
    }

    while True:
        response = requests.get(api_endpoint, headers=headers, params=params)
        mentions = response.json()['statuses']

        for mention in reversed(mentions):
            message = mention['text']
            id = mention['id']
            user_name = mention['user']['screen_name']

            response = generate_response(message, user_name)
            send_response_to_weibo(response, user_name)

            last_id = max(last_id, id)

        time.sleep(60)  # Wait for 1 minute before checking for new mentions again


# Start the background thread for checking mentions
threading.Thread(target=check_mentions).start()

if __name__ == '__main__':
    app.run(port=5000)
