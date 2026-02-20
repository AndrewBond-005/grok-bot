from stats import update_user_stats, get_stats_text

YES_RESPONSE = "пизда хахахахах"
NO_RESPONSE = "пидора ответ ахахахаха"


async def yesno(message_lower, update):
    words = message_lower.split()
    if words:
        last_word = words[-1]
        user = update.message.from_user
        username = user.username or user.first_name or f"id{user.id}"

        if last_word.endswith("да"):
            count = update_user_stats(username)
            await update.message.reply_text(YES_RESPONSE)

            if count % 10 == 0:
                await update.message.reply_text(f"🎉 {count} ответов!\n\n{get_stats_text()}")
            return True

        elif last_word.endswith("нет"):
            count = update_user_stats(username)
            await update.message.reply_text(NO_RESPONSE)

            if count % 10 == 0:
                await update.message.reply_text(f"🎉 {count} ответов!\n\n{get_stats_text()}")
            return True

    return False