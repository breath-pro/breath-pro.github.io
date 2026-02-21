with open('index.html', 'r') as f:
    content = f.read()

new_styles = '''
    .screenshots { padding: 80px 0; background: #111 !important; }
    .section-sub { text-align: center; color: #888; margin-bottom: 48px; font-size: 1.1rem; }
    .screens-grid { display: flex !important; flex-direction: row !important; gap: 24px; justify-content: center; align-items: flex-start; }
    .screen-item { text-align: center; flex: 0 0 auto; }
    .screen-item img { width: 180px !important; height: auto !important; border-radius: 20px; box-shadow: 0 20px 60px rgba(0,0,0,0.6); display: block; margin: 0 auto; }
    .screen-item p { margin-top: 12px; color: #888; font-size: 0.85rem; }
'''

content = content.replace('</style>', new_styles + '</style>')

with open('index.html', 'w') as f:
    f.write(content)

print('CSS добавлен!')