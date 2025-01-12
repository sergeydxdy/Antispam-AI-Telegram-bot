from ai_models.ai_model import Model
from aiogram.types import Message
from aiogram import F, Router

model = Model()
ai_router = Router()

@ai_router.message(F.chat.type != 'private')
async def start_reg_channel(message: Message):
    print(message.text)
    if model.predict_spam(message.text):
        await message.delete()
