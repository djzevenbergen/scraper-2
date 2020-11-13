from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
import urllib3


def get_proxies():
    url = 'https://hidemy.name/api/proxylist.txt?country=US&maxtime=1700&type=hs&out=plain&lang=en&utf&code=709444465162232'
    response = requests.get(url)
    parser = response.text
    print(parser)
    # proxies = set()
    # for i in parser:
    #     proxy = i
    #     print(i)
    #     proxies.add(proxy)
    # return proxies
    return parser


if __name__ == "__main__":
    thing = get_proxies()
    proxies = thing.split()
    print(proxies)
    # If you are copy pasting proxy ips, put in the list below
    # proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
    # proxies = get_proxies()

    proxy_pool = cycle(proxies)

    url = 'https://httpbin.org/ip'
    for i in range(1, len(proxies) - 1):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)
        try:
            response = requests.get(
                url, proxies={"https": "http://" + proxy, "http": "http://" + proxy})
            print(response.json())
        except:
            # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
            # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
            print("Skipping. Connnection error")
