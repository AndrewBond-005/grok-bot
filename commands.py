from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from stats import get_stats_text

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /grokyesno"""
    await update.message.reply_text(get_stats_text())

def setup_stats_handlers(application):
    application.add_handler(CommandHandler("grokyesno", stats_command))