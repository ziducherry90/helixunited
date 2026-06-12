import sys

file_path = 'C:/Users/WALTON/Downloads/Helix United/index.html'
dest_path = 'C:/Users/WALTON/Downloads/Untitled-1.html'

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
    'Ã°Å¸â€œâ€°': '📈',
    'Ã°Å¸â€œÂ ': '📍',
    'Ã°Å¸â€œÂ§': '📧',
    'Ã¢ï¿½Â°': '⏰'
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Restored and fixed safely.')
