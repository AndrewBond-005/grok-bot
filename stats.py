import json
import os
from pathlib import Path

if os.path.exists('/data/'):  # Railway
    STATS_FILE = '/data/yesno_stats.json'
elif os.path.exists('/tmp/'):  # Render и другие
    STATS_FILE = '/tmp/yesno_stats.json'
else:  # Локально
    STATS_FILE = Path(__file__).parent / "yesno_stats.json"

def load_stats():
    """Загружает статистику из файла"""
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_stats(stats):
    """Сохраняет статистику в файл"""
    with open(STATS_FILE, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)


def update_user_stats(username):
    """Увеличивает счётчик пользователя на 1"""
    stats = load_stats()

    if username not in stats:
        stats[username] = {'count': 0}

    stats[username]['count'] += 1
    save_stats(stats)
    return stats[username]['count']


def get_stats_text():
    """Возвращает текст статистики"""
    stats = load_stats()
    if not stats:
        return "Статистика пока пуста"

    # Сортируем по убыванию
    sorted_users = sorted(stats.items(), key=lambda x: x[1]['count'], reverse=True)

    lines = ["Стата подъёбов да/нет:\n"]
    for username, data in sorted_users:
        lines.append(f"{username}: {data['count']}")

    return "\n".join(lines)