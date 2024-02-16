from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('6653096746:AAFKCqQEgQxOAqjMZwJZXaVegR-2VynLyfo')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://kyka71ks.beget.tech/')))
    await message.answer('Здарова бандит', reply_markup=markup)

executor.start_polling(dp)