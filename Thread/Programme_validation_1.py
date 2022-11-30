import time
import concurrent.futures
import requests

img_urls = ['https://cdn.pixabay.com/photo/2022/11/08/21/15/cliffs-7579330_960_720.jpg']

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

end = time.perf_counter()

print(f'Finished in {round(end-start, 2)} second(s)')

import threading
import time

def task(i):
    print("Task {} started".format(i))
    time.sleep(1)
    print("Task {} finished".format(i))

start = time.perf_counter()

t1 = threading.Thread(target=task, args=(1,))
t1.start() # start the thread

t2 = threading.Thread(target=task, args=(2,))
t2.start() # start the thread

t1.join () # wait for the thread to finish
t2.join () # wait for the thread to finish

end = time.perf_counter()

print(f"Tasks ended in {round(end - start, 2)} second(s)")

import multiprocessing
import time

def task(i):
    print("Task {} started".format(i))
    time.sleep(1)
    print("Task {} finished".format(i))


if __name__ == "__main__":
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=task, args=(1,))
    p1.start() # start the process
    p1.join () # wait for the process to finish

    end = time.perf_counter()

    print(f"Tasks ended in {round(end - start, 2)} second(s)")
