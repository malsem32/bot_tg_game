from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = ''
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


