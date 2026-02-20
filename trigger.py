# Набор фраз для ответа
import random

RESPONSES = [
    "конешно",
    "очев",
    "ну да",
    "да",
    "ОЧЕВИДНО",
    "не",
    "не-а, неправда",
    "нет конечно",
    "ни в коем разе, не не не",
    "не знаю",
    "а ты сам как думаешь?",
    "хм, спорный вопрос",
    "лол, ты чё тупой?",
    "что за идиотские вопросы?",
]
# Слова-триггеры (можно добавлять свои)
TRIGGER_WORDS = ["грок", "грок это правда?", "грок, это правда?", "грок ответь"]
async def trig(message_lower, update):
    for trigger in TRIGGER_WORDS:
        if trigger.lower() in message_lower:
            response = random.choice(RESPONSES)
            await update.message.reply_text(response)
            break