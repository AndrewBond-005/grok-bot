import random

MESS = [
    "сказал один мудрец",
    "сказал один глупец",
    "спизданул один хуесос",
    "спизданул один пидарас",
]
LOG_FILE = "messages.txt"


async def dublicate(update, prob):
    if random.random() < prob:
        try:
            # Читаем все строки из файла
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            if lines:
                # Выбираем случайную строку и убираем перенос строки
                random_line = random.choice(lines).strip()

                if random_line:  # проверяем, что строка не пустая
                    mess = random.choice(MESS)
                    await update.message.reply_text(f"\'{random_line}\'-{mess}")

        except FileNotFoundError:
            # Если файла нет - просто ничего не делаем
            pass
        except Exception as e:
            print(f"Ошибка в dublicate: {e}")