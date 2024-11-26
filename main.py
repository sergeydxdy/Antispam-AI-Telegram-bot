import requests
from random import random

API = '7202336450:AAHDhqjwNGOCLKJ21tJ0L1st3ZgDXldwCx8'
CHAT_ID = '-1002202582670'
BASE_URL = f'https://api.telegram.org/bot{API}/'

BANNED_WORDS = {'хуй'}

def check_banned_word(text):
    status = any(word in text for word in BANNED_WORDS)
    return status


class SpamDetector:
    def __init__(self):
        pass

    def is_spam(self, text):
        return random() < 0.5


class Bot:
    def __init__(self, api, chat_id):
        self.api = api
        self.chat_id = chat_id
        self.base_url = f'https://api.telegram.org/bot{API}/'
        self.spam_detector = SpamDetector()
        self.processed_messages = []
        self.last_update_id = None

    def _get_updates(self):
        url = self.base_url + 'getUpdates'
        params = {'timeout': 1}
        if self.last_update_id:
            params['offset'] = self.last_update_id + 1
        response = requests.get(url, params=params)
        return response.json()

    def _delete_message(self, message_id):
        url = self.base_url + 'deleteMessage'
        params = {'chat_id': self.chat_id, 'message_id': message_id}
        requests.post(url, params=params)

    def _send_message(self, message_id):
        url = self.base_url + 'sendMessage'
        text = 'я тебя сейчас удалю нафиг'
        params = {'chat_id': self.chat_id, 'text': text, 'reply_to_message_id': message_id}
        requests.post(url, params=params)

    def process_messages(self):
        while True:
            updates = self._get_updates()
            for update in updates.get('result', []):
                self.last_update_id = update['update_id']
                message = update.get('message')
                if message and 'text' in message and message['message_id'] not in self.processed_messages:
                    text = message['text'].lower()
                    if check_banned_word(text):
                        self._send_message(message['message_id'])
                        self._delete_message(message['message_id'])
                        self.processed_messages.append(message['message_id'])



if __name__ == "__main__":
    bot = Bot(API, CHAT_ID)
    bot.process_messages()

