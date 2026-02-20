from telegram import Update, ReactionTypeEmoji
from telegram.ext import ContextTypes
import random

REACTIONS = ["👍", "👎", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌"]


async def react_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and random.random() < 0.25:  # 50% вероятность
        # Выбираем случайную реакцию
        reaction = random.choice(REACTIONS)

        # Устанавливаем реакцию на полученное сообщение
        await context.bot.set_message_reaction(
            chat_id=update.message.chat_id,
            message_id=update.message.message_id,
            reaction=[ReactionTypeEmoji(emoji=reaction)]
        )