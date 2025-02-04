# import logging
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
#
#
#
#
#
# def main():
#
#
#     logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#     logger = logging.getLogger(__name__)
#
#     async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#         keyboard = [
#             [InlineKeyboardButton("Пример работы бота", callback_data='example')],
#             [InlineKeyboardButton("Тарифы", callback_data='tariffs')]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         await update.message.reply_text('Привет! Я бот для автоматической выставки реакций на истории. Выберите опцию:',
#                                         reply_markup=reply_markup)
#
#     async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
#         query = update.callback_query
#         await query.answer()
#
#         if query.data == 'example':
#             keyboard = [[InlineKeyboardButton("Вернуться в главное меню", callback_data='menu')]]
#
#             reply_markup = InlineKeyboardMarkup(keyboard)
#             await query.edit_message_text(text="Скриншоты реакций на истории...", reply_markup=reply_markup)
#
#         elif query.data == 'tariffs':
#             keyboard = [[InlineKeyboardButton("Вернуться в главное меню", callback_data='menu')]]
#             reply_markup = InlineKeyboardMarkup(keyboard)
#             await query.edit_message_text(
#                 text="Тарифы:\n1 месяц - цена\n3 месяца - цена\n9 месяцев - цена\n1 год - цена",
#                 reply_markup=reply_markup)
#
#         elif query.data == 'menu':
#             await query.start()
#
#     application = ApplicationBuilder().token("7753733528:AAE4tUI3s3-M49k8Ajb9qEkY2W-7P6P-yOg").build()
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CallbackQueryHandler(button))
#     application.run_polling()
#
# if __name__ == '__main__':
#     main()
#

# import logging
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
#
#
# def main():
#     logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#     logger = logging.getLogger(__name__)
#
#     async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#         keyboard = [
#             [InlineKeyboardButton("Пример работы бота", callback_data='example')],
#             [InlineKeyboardButton("Тарифы", callback_data='tariffs')]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         await update.message.reply_text('Привет! Я бот для автоматической выставки реакций на истории. Выберите опцию:',
#                                         reply_markup=reply_markup)
#
#     async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
#         query = update.callback_query
#         await query.answer()
#
#         if query.data == 'example':
#             keyboard = [[InlineKeyboardButton("Вернуться в главное меню", callback_data='start_menu')]]
#             reply_markup = InlineKeyboardMarkup(keyboard)
#             await query.edit_message_text(text="Скриншоты реакций на истории...", reply_markup=reply_markup)
#
#         elif query.data == 'tariffs':
#             keyboard = [[InlineKeyboardButton("Вернуться в главное меню", callback_data='start_menu')]]
#             reply_markup = InlineKeyboardMarkup(keyboard)
#             await query.edit_message_text(
#                 text="Тарифы:\n1 месяц - цена\n3 месяца - цена\n9 месяцев - цена\n1 год - цена",
#                 reply_markup=reply_markup)
#
#         elif query.data == 'start_menu':
#             await start(query.message, context)
#
#     application = ApplicationBuilder().token("7753733528:AAE4tUI3s3-M49k8Ajb9qEkY2W-7P6P-yOg").build()
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CallbackQueryHandler(button))
#
#     application.run_polling()
#
#
# if __name__ == '__main__':
#     main()



import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Пример работы бота", callback_data='example')],
        [InlineKeyboardButton("Тарифы", callback_data='tariffs')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Я бот для автоматической выставки реакций на истории. Выберите опцию:',
                                      reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'example':
        keyboard = [[InlineKeyboardButton("Вернуться в главное меню", callback_data='start_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Скриншоты реакций на истории...", reply_markup=reply_markup)

    elif query.data == 'tariffs':
        keyboard = [[InlineKeyboardButton("Вернуться в главное меню", callback_data='start_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Тарифы:\n1 месяц - 55\n3 месяца - 111\n9 месяцев - 333\n1 год - 999",
            reply_markup=reply_markup)

    elif query.data == 'start_menu':
        await query.edit_message_text(text="Привет! Я бот для автоматической выставки реакций на истории. Выберите опцию:",
                                       reply_markup=InlineKeyboardMarkup([
                                           [InlineKeyboardButton("Пример работы бота", callback_data='example')],
                                           [InlineKeyboardButton("Тарифы", callback_data='tariffs')]
                                       ]))

if __name__ == '__main__':
    application = ApplicationBuilder().token("7753733528:AAE4tUI3s3-M49k8Ajb9qEkY2W-7P6P-yOg").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

