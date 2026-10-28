import re
import os

base_dir = r'c:\Users\Administrator\Desktop\新建文件夹 (5)'
html_path = os.path.join(base_dir, 'index.html')
js_path = os.path.join(base_dir, 'app.js')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Check all image paths
imgs = re.findall(r'src=["\'](\./assets/[^"\']+)["\']', html)
for img in imgs:
    full_path = os.path.join(base_dir, img.replace('/', os.sep))
    if not os.path.exists(full_path):
        print(f"ERROR: Missing image: {full_path}")
    else:
        print(f"OK: Image found -> {img}")

# 2. Check i18n keys
keys = re.findall(r'data-i18n=["\']([^"\']+)["\']', html)
missing = []
for k in set(keys):
    if f'{k}:' not in js:
        missing.append(k)

if missing:
    print(f"WARNING: Missing keys in translations: {missing}")
else:
    print(f"SUCCESS: All {len(set(keys))} unique i18n keys present in translations!")

# 3. Check for any literal raw double asterisks
if '**' in html or '**' in js:
    print("WARNING: Found literal '**' in code!")
else:
    print("SUCCESS: Zero raw '**' asterisks found!")
