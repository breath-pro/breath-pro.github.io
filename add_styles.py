with open('index.html', 'r') as f:
    content = f.read()

styles = '''
.screenshots { padding: 80px 0; background: #0a0a0a; }
.section-sub { text-align: center; color: #888; margin-bottom: 48px; font-size: 1.1rem; }
.screens-grid { display: flex; gap: 24px; justify-content: center; flex-wrap: wrap; }
.screen-item { text-align: center; }
.screen-item img { width: 220px; border-radius: 24px; box-shadow: 0 20px 60px rgba(0,0,0,0.5); }
.screen-item p { margin-top: 16px; color: #888; font-size: 0.9rem; }
'''

content = content.replace('</style>', styles + '</style>')

with open('index.html', 'w') as f:
    f.write(content)

print('Стили добавлены!')