import logging
import os
import requests
LOG=logging.getLogger(__name__)


def telegram_send(text,session=None):
    token=os.getenv('TELEGRAM_BOT_TOKEN','').strip()
    chat_id=os.getenv('TELEGRAM_CHAT_ID','').strip()
    if not token or not chat_id:return False
    try:
        resp=(session or requests.Session()).post(
            f'https://api.telegram.org/bot{token}/sendMessage',
            data={'chat_id':chat_id,'text':text,'disable_web_page_preview':'true'},timeout=25)
        resp.raise_for_status()
        return bool(resp.json().get('ok',False))
    except (requests.RequestException,ValueError) as exc:
        LOG.warning('Telegram notification failed (%s)',type(exc).__name__)
        return False
