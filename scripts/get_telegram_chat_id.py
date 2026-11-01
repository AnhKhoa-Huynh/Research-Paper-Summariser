"""After creating your bot, send /start; run with env TELEGRAM_BOT_TOKEN set.
Never print or share the bot token itself.
"""
import os
import requests

token=os.environ.get('TELEGRAM_BOT_TOKEN','').strip()
if not token:
    raise SystemExit('Set TELEGRAM_BOT_TOKEN first; do not paste it into code.')
r=requests.get(f'https://api.telegram.org/bot{token}/getUpdates',timeout=25)
r.raise_for_status()
updates=r.json().get('result',[])
chat_ids=sorted({str(u.get('message',{}).get('chat',{}).get('id')) for u in updates
                 if u.get('message',{}).get('chat',{}).get('id') is not None})
print('Found chat IDs:',', '.join(chat_ids) if chat_ids else 'none; message the bot with /start first')
