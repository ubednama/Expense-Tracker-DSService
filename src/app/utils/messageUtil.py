import re

class MessageUtil:
    def isBankSMS(self, message):
        words_to_search = ['spent', 'card', 'bank', 'debit']
        pattern  = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_search) + r')\b'
        return bool(re.search(pattern, message, flags=re.IGNORECASE))