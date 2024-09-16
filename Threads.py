import threading
import time
import datetime


def txt_reader(txt_file_address):
    print(f'reading {txt_file_address} right now...')
    with open(txt_file_address) as file:
        print(file.readlines())
    print(f'{txt_file_address} is finally done reading')


addresses = ('1.txt', '2.txt', '3.txt')
threads = list()
for address in addresses:
    thread = threading.Thread(target=txt_reader, args=(address,))
    thread.start()
    threads.append(thread)

for address, thread in enumerate(threads):
    print(f'{address} is about to be finished')
    thread.join()
    print(f'thread {address} is finished.')

print(f'all threads are finished.')
