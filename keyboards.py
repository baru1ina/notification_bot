from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Добавить дело')
b2 = KeyboardButton('Текущие дела')
b3 = KeyboardButton('Выполненные дела')
b4 = KeyboardButton('Главное меню')
kb_start.add(b1).insert(b2).add(b3).insert(b4)



