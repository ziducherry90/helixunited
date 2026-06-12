file_path = 'C:/Users/WALTON/Downloads/Untitled-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Fix comments
text = re.sub(r'// A.*?\s+', '// ', text)
text = re.sub(r'A\?\?,+', '', text)

replacements = {
    "A,?~A ": "👤",
    "A,?oA": "📝",
    "A,?o?1": "📋",
    "AA": "⚽",
    "A??~ ": "📈 ",
    "A,?o": "-",
    "A\"?o": "✅",
    "A\"?": "❌",
    "A,?o": "📝",
    "A,A??": "🥇",
    "A,AE+": "🥈",
    "AAA?": "🥉",
    "A,Ar": "🏟️",
    "A,?AA_A,A?": "👟",
    "A,Ac": "🎩",
    "A,A A ": "🧤",
    "A,?s": "🎂",
    "A,?oA?": "📍"
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Cleaned up the remaining mangled emojis safely.')
