import time
import random
from multiprocessing import Process, Queue, freeze_support

if __name__ == '__main__':
    queue = Queue()

    while True:
        data = random.randint(1, 100)
        queue.put(data)
        time.sleep(1)