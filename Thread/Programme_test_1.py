import time

def task(i):
    print("Task {} started".format(i))
    time.sleep(1)
    print("Task {} finished".format(i))
start = time.perf_counter()

task (1)
end = time.perf_counter()
print (f"Tasks ended in {round(end -start, 2)} second(s)")