from db import PostgreSQL
from aiogram import types
from aiogram import executor
from buttons import InlineButtons, Buttons
from config import dispatcher, bot, resize_image
from aiogram.types import Message, CallbackQuery

btns = Buttons()
ibtns = InlineButtons()

@dispatcher.message_handler(commands=['start'])
async def welcome(message: Message):
    welcome_sticker=open('/home/zhoomart/Pictures/welcome.gif', 'rb')
    await bot.send_animation(
        chat_id=message.from_user.id,
        animation=welcome_sticker
    )

    return await bot.send_message(
        chat_id=message.from_user.id,
        text=f'''
        *здравствуйте, {message.from_user.first_name}*
        компания Resto рада видеть вас в нашем телеграм боте!
        ''',
        parse_mode=types.ParseMode.MARKDOWN,
        reply_markup = btns.main_buttons()
    )

@dispatcher.message_handler(content_types=["text"])
async def main_response(message: Message):
    if message.text == 'заказывать еду на вынос 🍕':
       return await bot.send_message(
           chat_id = message.from_user.id,
           text = 'Здесь будет меню заказа...'
       )
    elif message.text == 'забронировать столик ⏰':
        return await bot.send_message(
            chat_id = message.from_user.id,
            text = 'Здесь будет бронь...'
        )
    elif message.text == 'узнать меню':
        return await bot.send_message(
           chat_id = message.from_user.id,
           text = 'Resto Меню:',
           reply_markup = ibtns.show_menu_buttons()
       )
    elif message.text == 'Отзывы':
        return await bot.send_message(
           chat_id = message.from_user.id,
           text='*Пожалуйста оставьте свой отзыв*',
           parse_mode=types.ParseMode.MARKDOWN,
           reply_markup=ibtns.feedbacks_buttons()
       )


@dispatcher.callback_query_handler()
async def show_menu(callback: CallbackQuery):
    psql = PostgreSQL()

    if callback.data == 'breakfast':
        for breakfast_object in psql.select(
                ('name', 'meal_type', 'image_path', 'price'), 
                'meal', 
                {"meal_type": 2}
            ):
            resized_image = resize_image(breakfast_object[2])

            await bot.send_photo(
                chat_id=callback.from_user.id,
                photo=open(resized_image, 'rb'),
                caption=f'_**Resto Завтраки:**_\nНазвание блюда: *{breakfast_object[0]}*\nЦена: *{breakfast_object[3]} сом*',
                parse_mode=types.ParseMode.MARKDOWN
            )
        else:
            psql.connection.close()

    elif callback.data == 'send_feedback':
        return await bot.send_message(
            chat_id=callback.from_user.id,
            text='*Пожалуйста оставьте отзыв:*',
            parse_mode=types.ParseMode.MARKDOWN
        )

@dispatcher.message_handler(content_types=["text"])
async def save_feedback(message: Message):
    print(message.text)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Ваш отзыв был успешно сохранён!"
    )


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher)