import re

file_path = 'C:/Users/WALTON/Downloads/Untitled-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    'Ã¢â‚¬â€': '—',
    'Ã¢â‚¬â€œ': '–',
    'Ã¢â‚¬Â¦': '…',
    'Ã‚Â©': '©',
    'Ã‚Â·': '·',
    'Ã°Å¸Â â€ ': '🏆',
    'Ã°Å¸â€œÂ·': '📷',
    'dY?+': '🏆',
    'dY^': '🥈',
    '?': '🥉',
    'sT': '⚙️',
    'o"': '✅',
    'o ': '❌',
    'o?,?': '✍️',
    's': '⚽',
    '+"': '📝',
    '+': '📈',
    '+?': '⬅️',
    '+\'': '➡️'
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Replaced')
