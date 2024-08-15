info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, stings):
    k = 1
    t = 0
    info_typle = []
    file = open(file_name, 'w', encoding='utf-8')
    for i in stings:
        info_typle.append(((k, t), i))
        file.write(f'\n{i}')
        t = file.tell()
        k += 1
    return info_typle


result = custom_write('test.txt', info)
for i in result:
    print(i)
