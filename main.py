import requests
from random import random
from ai_model import Model

API = '7202336450:AAHDhqjwNGOCLKJ21tJ0L1st3ZgDXldwCx8'
CHAT_ID = '-1002202582670'
BASE_URL = f'https://api.telegram.org/bot{API}/'

BANNED_WORDS = {'хуй'}

def check_banned_word(text):
    status = any(word in text for word in BANNED_WORDS)
    return status


class Bot:
    def __init__(self, api, chat_id, ai_model):
        self.api = api
        self.chat_id = chat_id
        self.base_url = f'https://api.telegram.org/bot{API}/'
        self.processed_messages = []
        self.last_update_id = None
        self.model = ai_model

    def _get_updates(self):
        url = self.base_url + 'getUpdates'
        params = {'timeout': 30}
        if self.last_update_id:
            params['offset'] = self.last_update_id + 1
        response = requests.get(url, params=params)
        return response.json()

    def _delete_message(self, message_id):
        url = self.base_url + 'deleteMessage'
        params = {'chat_id': self.chat_id, 'message_id': message_id}
        try:
            requests.post(url, params=params)
        except Exception as e:
            print('Error:', e)

    def _send_message(self, reply_to_message_id):
        url = self.base_url + 'sendMessage'
        text = 'Ваш комментарий был удалён'
        params = {'chat_id': self.chat_id, 'text': text, 'reply_to_message_id': reply_to_message_id}
        try:
            requests.post(url, params=params)
        except Exception as e:
            print('Error:', e)

    def process_messages(self):
        while True:
            updates = self._get_updates()
            for update in updates.get('result', []):
                self.last_update_id = update['update_id']
                message = update.get('message')
                if message and 'text' in message and message['message_id'] not in self.processed_messages:
                    if self.model.predict_spam(text=message['text']):
                        #self._send_message(reply_to_message_id=message['message_id'])
                        self._delete_message(message['message_id'])
                        self.processed_messages.append(message['message_id'])



if __name__ == "__main__":
    model = Model()
    bot = Bot(API, CHAT_ID, model)
    bot.process_messages()

