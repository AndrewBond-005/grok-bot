import random

REPLY_RESPONSES = [
    "соси",
    "бля ну какой же ты тупой",
    "засунь себе это в жопу",
    "ди нах",
    "заебал, отстань",
    "тупым слова не давали",
    "бля иди с дипсиком общайся",
    "тебе заняться нечем?",
    "с пидорами не разговариваю",
    "бля не заёбывай",
    "с хуесосами не разговариваю",
    "отстань, я занят",
]
async def reply(update,context):
    if update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id:
        reply_response = random.choice(REPLY_RESPONSES)
        await update.message.reply_text(reply_response)
        return True
    else:
        return False