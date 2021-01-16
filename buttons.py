from aiogram import types

class Buttons:
    def main_buttons(self):
        markup = types.ReplyKeyboardMarkup(
            one_time_keyboard=True,
            row_width=2
        )

        order_food_to_deliver = types.KeyboardButton(
            text = 'заказывать еду на вынос 🍕'
        )
        book_table = types.KeyboardButton(
            text = 'забронировать столик ⏰ '
        )
        show_menu = types.KeyboardButton(
            text = 'узнать меню',
        )
        set_feedback = types.KeyboardButton(
            text = 'Отзывы',
        )
        markup.add(
            order_food_to_deliver,
            book_table,
            show_menu,
            set_feedback,
        )
        return markup


    def ask_phone_number(self):
        markup = types.ReplyKeyboardMarkup()

        ask_phone_number = types.KeyboardButton(
            text="Отправить Отзыв",
            request_contact=True
        )

        markup.add(ask_phone_number)

        return markup


class InlineButtons:
    def show_menu_buttons(self):
        markup = types.InlineKeyboardMarkup(
            row_width=1
        )

        primary_meal_btn = types.InlineKeyboardButton(
            text='Фирменные блюда',
            callback_data='primary_meal'
        )

        breakfast_btn = types.InlineKeyboardButton(
            text='Завтраки',
            callback_data='breakfast'
        )

        lunch_btn = types.InlineKeyboardButton(
            text='Обеды',
            callback_data='lunch',
        )

        dinner_btn = types.InlineKeyboardButton(
            text='Ужин',
            callback_data='dinner'
        )

        resto_btn = types.InlineKeyboardButton(
            text='Перейти на сайт',
            callback_data='resto',
            url='https://freehtml5.co/preview/?item=resto-free-responsive-bootstrap-4-template-for-restaurants'
        )
        markup.add(
            primary_meal_btn,
            breakfast_btn,
            lunch_btn,
            dinner_btn,
            resto_btn,
        )

        return markup


    def feedbacks_buttons(self):
        markup = types.InlineKeyboardMarkup(
            row_width=1
        )
        send_feedback_btn = types.InlineKeyboardButton(
            text='Оставить отзыв',
            callback_data='send_feedback'
        )

        read_feedbacks_btn = types.InlineKeyboardButton(
            text='Прочитать отзывы',
            callback_data='read_feedbacks'
        )

        markup.add(send_feedback_btn, read_feedbacks_btn)

        return markup