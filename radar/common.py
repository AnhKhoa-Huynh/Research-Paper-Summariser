import hashlib
import html
import re
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode


def clean_text(value):
    text = html.unescape(re.sub(r'<[^>]+>', ' ', value or ''))
    return re.sub(r'\s+', ' ', text).strip()


def normalize_title(value):
    return re.sub(r'[^a-z0-9]+', ' ', (value or '').casefold()).strip()


def clean_url(value):
    if not value:
        return ''
    u = urlsplit(value)
    # Keep query parameters necessary for publisher article identification.
    pairs = [(k, v) for k, v in parse_qsl(u.query) if not k.lower().startswith(('utm_', 'fbclid', 'gclid'))]
    return urlunsplit((u.scheme.lower(), u.netloc.lower(), u.path.rstrip('/'), urlencode(pairs), ''))


def canonical_key(record):
    # Resolve cross-provider duplicates before source-specific identifiers.
    doi = (record.get('doi') or '').strip().lower().replace('https://doi.org/', '').replace('http://doi.org/', '')
    if doi:
        return 'doi:' + doi
    title = normalize_title(record.get('title'))
    if title:
        return 'title:' + hashlib.sha1(title.encode('utf-8')).hexdigest()[:20]
    return 'url:' + hashlib.sha1(clean_url(record.get('url')).encode()).hexdigest()[:20]


def parse_date(value):
    if not value:
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    try:
        t = datetime.fromisoformat(value.replace('Z', '+00:00'))
        return t if t.tzinfo else t.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        try:
            t = parsedate_to_datetime(value)
            return t if t.tzinfo else t.replace(tzinfo=timezone.utc)
        except (TypeError, ValueError, IndexError):
            return None


def slug(value, length=75):
    return re.sub(r'[^a-z0-9]+', '-', (value or '').lower()).strip('-')[:length].strip('-') or 'item'


def markdown_escape(value):
    return (str(value or '').replace('\\', '\\\\').replace('[', '\\[').replace(']', '\\]')
            .replace('|', '\\|').replace('`', '\\`'))


def within_lookback(published, now, days):
    p = parse_date(published)
    if p is None:
        return False  # never misrepresent undated items as new
    delta = now - p.astimezone(timezone.utc)
    return -3600 <= delta.total_seconds() <= 86400 * days
