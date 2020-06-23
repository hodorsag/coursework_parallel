import os
import time
import collections
import threading
paths = list()
directory = "D:\Coursework"


def inverted_index(plist, index):
    for i in plist:
        with open(i, "r") as f:
            lexems = f.read().split(" ")
            for lexem in lexems:
                for letter in lexem:
                    if letter.isalpha() or letter == "'":
                        continue
                    else:
                        lexem.replace(letter, "")
                    index[lexem].append(i)

def main():
    threads = []
    start = 0
    end = 0
    index = collections.defaultdict(list)
    for d, dirs, files in os.walk(directory):
        for f in files:
            if os.path.isdir(f):
                continue
            else:
                temp = os.path.join(d, f)
                paths.append(temp)

    thread_count = input("Input number of threads: ")

    chunk = len(paths)//int(thread_count)

    start = time.time()

    count = int(thread_count)

    for id in range(count):
         process = threading.Thread(target = inverted_index, args = (paths[id*chunk: id*chunk + chunk], index))
         process.start()
         threads.append(process)

    for i in threads:
        i.join()

    end = time.time()

    result = end - start

    print(f"Index size: ", {len(index)}, " Time: ", result)

if __name__ == "__main__":
    main()
