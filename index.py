import os
import time
import collections
import threading
paths = list()
directory = "A:\Coursework"


def inverted_index(plist, index):
    for i in plist:
        with open(i, "r") as f: # открываем первый файл только чтением как f (как переприсваиванием)
            lexems = f.read().split(" ") # читаем строку до пробела и впихиваем её в лексемы
            for lexem in lexems:
                for letter in lexem:
                    if letter.isalpha() or letter == "'":
                        continue
                    else:
                        lexem.replace(letter, "")
                    index[lexem].append(i)

def main():
    threads = [] # список потоков
    start = 0 # начало и конец отсчёта времени
    chunks = []
    end = 0
    index = collections.defaultdict(list) # создаем словарь (ключ и значение) где слово ключ, а список путей - значение
    for d, dirs, files in os.walk(directory): # вносим в один большой список все пути к файлам
        for f in files:
            if os.path.isdir(f):
                continue
            else:
                temp = os.path.join(d, f)
                paths.append(temp)

    thread_count = input("Input number of threads: ")

    chunk = len(paths) // int(thread_count) # то, сколько должен будет взять каждый поток

    start = time.time()

    count = int(thread_count) # преобразование кол-ва потоков из строки в инт

    if len(paths) % count == 0: # считаем сколько должен будет взять каждый поток
        for i in range(count + 1):
            chunks.append(i * chunk)
    else:
        for i in range(count):
            chunks.append(i * chunk)
        chunks.append(len(paths))

    #print(chunks)
    for id in range(count):
        process = threading.Thread(target=inverted_index, args=(paths[chunks[id]: + chunks[id + 1]], index)) # создание потока
        process.start() # начало работы потока
        threads.append(process) # запихиваем поток в список потоков

    for i in threads: # ждем завершение свех потоков
        i.join()

    end = time.time()

    result = end - start

    print(f"Index size: ", {len(index)}, " Time: ", result)

if __name__ == "__main__":
    main()
