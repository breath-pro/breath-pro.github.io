with open('index.html', 'r') as f:
    content = f.read()

block = '''
    <!-- Скриншоты -->
    <section class="screenshots">
        <div class="container">
            <h2 class="section-title">Простой и красивый интерфейс</h2>
            <p class="section-sub">Всё интуитивно понятно с первого запуска — никаких лишних кнопок, только практика</p>
            <div class="screens-grid">
                <div class="screen-item">
                    <img src="screen1.png" alt="Выбор техники">
                    <p>Выбор техники дыхания</p>
                </div>
                <div class="screen-item">
                    <img src="screen2.png" alt="Практика">
                    <p>Визуальный гид дыхания</p>
                </div>
                <div class="screen-item">
                    <img src="screen3.png" alt="Ступени">
                    <p>12 ступеней мастерства</p>
                </div>
            </div>
        </div>
    </section>'''

insert_pos = content.find('<!-- FAQ -->')
content = content[:insert_pos] + block + '\n\n    ' + content[insert_pos:]

with open('index.html', 'w') as f:
    f.write(content)

print('Готово!')