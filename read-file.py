import os
import csv

if __name__ == "__main__":
    os.system('python3 best-seller-scrape.py p')

    import csv
    with open('products.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[1])
