LOG_FILE = "messages.txt"

def print_and_save(message_text):
    print(message_text)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{message_text}\n")