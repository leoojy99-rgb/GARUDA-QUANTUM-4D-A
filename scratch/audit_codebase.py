import re
import os

base_dir = r'c:\Users\Administrator\Desktop\新建文件夹 (5)'
html_path = os.path.join(base_dir, 'index.html')
js_path = os.path.join(base_dir, 'app.js')
css_path = os.path.join(base_dir, 'style.css')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Check all getElementById calls in JS match an ID in HTML
js_ids = re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", js)
html_ids = set(re.findall(r'id=["\']([^"\']+)["\']', html))

missing_ids = []
for jid in set(js_ids):
    if jid not in html_ids:
        missing_ids.append(jid)

if missing_ids:
    print(f"FAILED: JS references IDs not in HTML: {missing_ids}")
else:
    print(f"PASSED: All {len(set(js_ids))} getElementById targets exist in HTML!")

# 2. Check CSS brackets
open_b = css.count('{')
close_b = css.count('}')
if open_b == close_b:
    print(f"PASSED: CSS brackets balanced ({open_b} pairs)")
else:
    print(f"FAILED: CSS brackets mismatch! Open: {open_b}, Close: {close_b}")

# 3. Check HTML basic tags
for tag in ['html', 'head', 'body', 'main', 'header', 'footer']:
    assert f'<{tag}' in html and f'</{tag}>' in html, f"Tag <{tag}> unclosed!"
print("PASSED: Major structural HTML tags matched!")
