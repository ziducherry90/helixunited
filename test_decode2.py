import re

file_path = 'C:/Users/WALTON/Downloads/Helix United/index.html'
dest_path = 'C:/Users/WALTON/Downloads/Untitled-1.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

if text.startswith('\ufeff'):
    text = text[1:]

def fix_match(m):
    try:
        return m.group(0).encode('windows-1252').decode('utf-8')
    except:
        return m.group(0)

fixed_text = re.sub(r'[\x80-\xFF]+', fix_match, text)

with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(fixed_text)

print('Restored successfully.')
