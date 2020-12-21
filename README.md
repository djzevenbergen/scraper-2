##
by dj zevenbergen using Tushar SEth's repo at https://github.com/tseth92/web-scraper
##
1. On line 33 of best-seller-scrape.py, replace the url with the Amazon best seller category that you wish to scrape
    - the output of this script is a 'products.csv' file with every product url, star rating, and price
2. On line 179 of post-scrape.py, change 'appliances.csv' to be the name of whichever category you're scraping
3. Run 'python3 post-scrape.py p' or 'python3 post-scrape.py t'
    - 'p' means it using 'Process' and 't' means it's using 'Threading' 
    - https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python
    - If it starts adding rows of just 'product link' to appliances.csv and your terminal looks like the code block below, Amazon has flagged your IP, and you'll need to use a proxy. If someone could figure out how to use the rotating proxies in post-scrape.py on line 31, that would solve this for the most part, but I couldn't get it to work.

``` 
starting thread:  1
total time taken:  28.096547842025757  qcount:  119
Empty DataFrame
Columns: [Product Link]
Index: []
```

4. To parse the URLs into a CSV with product title, stars, price, and then image URLS, change lines 7 and 9 of 'parse-urls.py' to match the category that you're scraping. then run 'python3 parse-urls.py'

5. If you want just the URLS in a list, change lines 7 and 9 of 'just-urls.py' to match the category that you're scraping and then run 'python3 parse-urls.py'

6. If you want the asins for all of the products, run 'python3 asins.py'

7. What this really needs is a working proxy rotator and to be automated. 