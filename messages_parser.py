import json

with open('result.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('messages.txt', 'w', encoding='utf-8') as out:
    for msg in data['messages']:
        if msg['type'] == 'message' and 'forwarded_from' not in msg:
            text = msg.get('text', '')
            if isinstance(text, list):
                text = ''.join([part['text'] if isinstance(part, dict) else part for part in text])
            if text and text.strip():
                out.write(text.strip() + '\n')

print('Готово!')