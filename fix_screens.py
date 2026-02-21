with open('index.html', 'r') as f:
    content = f.read()

# Вырезаем блок скриншотов
start = content.find('<!-- Скриншоты -->')
end = content.find('</section>', start) + len('</section>')
screens_block = content[start:end]

# Удаляем его с текущего места
content = content[:start] + content[end:]

# Вставляем после секции "12 ступеней"
insert_after = content.find('</section>', content.find('12 Ступеней Мастерства')) + len('</section>')
content = content[:insert_after] + '\n\n    ' + screens_block + content[insert_after:]

with open('index.html', 'w') as f:
    f.write(content)

print('Перенесено!')