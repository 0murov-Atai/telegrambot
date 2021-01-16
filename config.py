from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from PIL import Image
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = Bot(BOT_TOKEN)
memory = MemoryStorage()
dispatcher = Dispatcher(bot=bot, storage=memory)


def resize_image(img_path):
    image = Image.open(img_path)
    new_image = image.resize((1024, 1024))
    new_image.save(img_path)
    return img_path
