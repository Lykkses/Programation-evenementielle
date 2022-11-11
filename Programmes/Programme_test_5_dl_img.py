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