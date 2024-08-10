info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, stings):
    k = 1
    info_typle = []
    for i in stings:

        file = open(file_name, 'a',encoding='utf-8')
        t = file.tell()
        info_typle.append([(k, t),i])
        file.write(f'\n{i}')
        t = file.tell()
        k += 1
        #file.close()
    return tuple(info_typle)


result = custom_write('test.txt', info)
for i in result:
    print(i)