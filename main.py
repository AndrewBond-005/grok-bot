import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from commands import setup_stats_handlers
from telegram.request import HTTPXRequest
from responses import *
from reply import *
from dublicate import *
from trigger import *
from printandsave import *
from react import *

load_dotenv()
TOKEN = os.getenv('TOKEN')
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text

    await react_to_message(update,context)
    if not message_text:
        return
    message_lower = message_text.lower()
    if await reply(update,context):             # ответ reply
        return
    print_and_save(message_text)                # сохранить сообщение
    await dublicate(update)       # прошлое сообщение dublicate
    if await yesno(message_lower, update):      # ответить на да/нет responses
        return
    await trig(message_lower,update)            # триггер


def main():
    request = HTTPXRequest(
        read_timeout=30,
        write_timeout=30,
        connect_timeout=30
    )
    application = Application.builder().token(TOKEN).request(request).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    setup_stats_handlers(application)
    print("Бот запущен...")
    application.run_polling()


if __name__ == "__main__":
    main()
