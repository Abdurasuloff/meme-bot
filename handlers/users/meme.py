from aiogram import types
from loader import dp
from utils.memegen import memegen

@dp.message_handler(commands=['meme'])
async def send_meme(message: types.Message):
    meme = memegen()
    await message.answer(
       f"{meme['setup']} \n-{meme['punchline']}"
    )