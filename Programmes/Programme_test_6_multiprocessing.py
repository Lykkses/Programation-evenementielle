#multiprocessing

import multiprocessing
import time

def task(i):
    print("Task {} started".format(i))
    time.sleep(1)
    print("Task {} finished".format(i))

if __name__ == "__main__":
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task, args=(1,))
    p1.start()
    p1.join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

