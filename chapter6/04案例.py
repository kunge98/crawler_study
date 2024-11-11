from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import requests


if __name__ == '__main__':
    url = ''
    resp = requests.get(url)
    resp.encoding = 'utf-8'

    print(resp.text)