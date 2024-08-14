import os
from datetime import datetime
time=datetime.now()
for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        filepath = os.path.abspath(file)
        filetime = os.path.getmtime(file)
        formatted_time = datetime.fromtimestamp(filetime)
        #formatted_time=time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(file)

        #filepath=[f for f in os.listdir() if os.path.isfile(f) ]
        print(f'Обнаружен файл: {file},Путь: {filepath}, Размер: {filesize} байт,Время изменения: {formatted_time},Родительская директория: {parent_dir}')