import os
import threading
import time

paths = list()
directory = "D:\Coursework"


def inverted_index(f, index):
    word = ''
    with open(f, "r") as file:
        while True:
            letter = file.read(1)
            if letter == '':
                if len(word) < 4:
                    word = ''
                    break
                else:
                    if word in index:
                        if f in index[word]:
                            word = ''
                            break
                        else:
                            index[word].append(f)
                            word = ''
                            break
                    else:
                        index[word] = list()
                        index[word].append(f)
                        word = ''
                        break
            if letter.isalpha() or letter == "'":
                word += letter.lower()
            else:
                if len(word) < 4:
                    word = ''
                else:
                    if word in index:
                        if f in index[word]:
                            word = ''
                        else:
                            index[word].append(f)
                            word = ''
                    else:
                        index[word] = list()
                        index[word].append(f)
                        word = ''


index = dict(list())
thread_id = []
threads = []

for d, dirs, files in os.walk(directory):
    for f in files:
        if os.path.isdir(f):
            continue
        else:
            temp = os.path.join(d, f)
            paths.append(temp)

thread_count = input("Input number of threads: ")

chunk = len(paths)//int(thread_count)

for i in range(0, int(thread_count)):
    thread_id.append(i)

start = time.process_time()

# for i in range(0, len(paths)):
#     inverted_index(paths[i], index)

for id in thread_id:
    threads.append(threading.Thread(target=inverted_index, args=(paths[id], index)))

print(len(threads))

for id in thread_id:
    threads[id].start()

for id in thread_id:
    threads[id].join()

end = time.process_time()

result = end - start

print(f"Index size: ", {len(index)}, " Time: ", result)
