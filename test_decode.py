import sys

file_path = 'C:/Users/WALTON/Downloads/Helix United/index.html'
dest_path = 'C:/Users/WALTON/Downloads/Untitled-1.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

try:
    # The file was originally UTF-8, but was read using Windows-1252 and saved as UTF-8.
    # To reverse: encode to Windows-1252 (getting original bytes back), decode as UTF-8.
    original_bytes = text.encode('windows-1252')
    fixed_text = original_bytes.decode('utf-8')
    
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(fixed_text)
    print("Perfectly restored all original emojis and characters!")
except Exception as e:
    print(f"Error: {e}")
