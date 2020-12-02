'''' Scrape the Amazon.com using requests and Beautiful Soup. Increasing the speed
using the Threading/Processing/Pool in python'''
import csv
import sys
import os
import os.path
from os import path
import re
import threading
from multiprocessing import Process, Queue, Pool, Manager
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
__author__ = "DJ Zevenbergen based off of Tushar SEth's repo at https://github.com/tseth92/web-scraper"
__email__ = "tusharseth93@gmail.com"

# use proxies in requests so as to proxy your request via a proxy server
# as some sites may block the IP if traffic generated by an IP is too high
# proxies = ['165.139.46.17:8080',
#            '47.88.7.18:8088',
#            '198.199.120.102:3128',
#            '209.97.150.167:8080',
#            '142.93.57.37:80',
#            '207.154.231.213:3128',
#            '138.68.41.90:3128',
#            '138.68.41.90:8080']


proxies = {
    'http': 'http://24.172.34.114:49920',
    'https': 'http://24.172.34.114:49920',
}
startTime = time.time()
qcount = 0
links = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store ratings of the product
# names = []
no_pages = 2


def get_data(pageNo, q, lin):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    r = requests.get("https://www.amazon.com" + lin[1],
                     headers=headers)  # proxies={"https": "http://doogiedeej.gmail.com:ast6zs@gate2.proxyfuel.com:2000/"})  # , proxies=proxies)
    #      r = requests.get("https://www.amazon.com/s?k=laptops&page=" +
    #  str(pageNo), headers=headers)  # , proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content, "html5lib")
    # print(soup.encode('utf-8')) # uncomment this in case there is some non UTF-8 character in the content and
    # you get error

    response = r.content.decode('utf-8')
    resp = json.dumps(response)

    # for d in soup.findAll('ol.li'):
    print(soup)
    # with open("soupt.txt", "w") as file:
    #     file.write(str(soup))
    # for item in soup.select("li"):
    #     print(item.get_text())
    counter = 0
    for d in soup.find_all('li'):

        print(d.get_text())

        # for d in soup.findAll('div', attrs={'class': 'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        link = d.find('img')

        all = []
        if counter == 0:
            all.append('product-title' + lin[0])
        if link is not None:

            all.append(link.get('src'))
        else:
            all.append("unknown-product")

        counter += 1
        q.put(all)


    # print("---------------------------------------------------------------")
results = []
if __name__ == "__main__":
    os.system('python3 best-seller-scrape.py p')

    linkDict = {}

    with open('products.csv', newline='') as f:
        reader = csv.reader(f)
        count = 0
        for line in reader:
            if count >= 1:
                key = line[1].split("/")
                val = line[1]

                print('hi', key[1])

                # key = line[0]

                linkDict[key[1] + '_'+line[2] + '_' + line[3]] = val
            count += 1

    print(linkDict)


# for row in reader:
#     print(row[1])

    for link in linkDict.items():
        m = Manager()
        q = m.Queue()  # use this manager Queue instead of multiprocessing Queue as that causes error
        p = {}
        links = []
        time.sleep(10)
        # user decides which method to invoke: thread, process or pool
        if sys.argv[1] in ['t', 'p']:
            for i in range(1, no_pages):
                if sys.argv[1] in ['t']:
                    print("starting thread: ", i)
                    p[i] = threading.Thread(
                        target=get_data, args=(i, q, link))
                    p[i].start()
                elif sys.argv[1] in ['p']:
                    print("starting process: ", i)
                    p[i] = Process(target=get_data, args=(i, q, link))
                    p[i].start()
            # join should be done in seperate for loop
            # reason being that once we join within previous for loop, join for p1 will start working
            # and hence will not allow the code to run after one iteration till that join is complete, ie.
            # the thread which is started as p1 is completed, so it essentially becomes a serial work instead of
            # parallel
            for i in range(1, no_pages):
                p[i].join()
        else:
            pool_tuple = [(x, q) for x in range(1, no_pages)]
            with Pool(processes=8) as pool:
                print("in pool")
                results = pool.starmap(get_data, pool_tuple)

        while q.empty() is not True:
            qcount = qcount+1
            queue_top = q.get()
            links.append(queue_top[0])

        print("total time taken: ", str(
            time.time()-startTime), " qcount: ", qcount)
        # print(q.get())
        df = pd.DataFrame(
            {'Product Link': links})  # , 'Price': prices, 'Ratings': ratings})
        print(df)

        # if ()
        # df.to_csv('my_csv.csv', mode='a', header=False)

        # with open(r'name', 'a') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(fields)
        df.to_csv('appliances.csv', mode='a', index=True, encoding='utf-8')
