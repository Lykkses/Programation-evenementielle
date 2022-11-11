import threading
import time

def task(i):
    print("Task {} started".format(i))
    time.sleep(1)
    print("Task {} finished".format(i))

start = time.perf_counter()

t1 = threading.Thread(target=task, args=(1,))
t1.start() # start the thread
t1.join () # wait for the thread to finish

end = time.perf_counter()

print(f"Tasks ended in {round(end - start, 2)} second(s)")