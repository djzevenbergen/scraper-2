import os
import csv

if __name__ == "__main__":

    import csv
    with open('products.csv', newline='') as f:
        reader = csv.reader(f)
        with open('asins.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            chunks = ''
            otherCount = 1
            for row in reader:

                chunks = row[1].split('/')
                if len(chunks) > 1:
                    print(chunks[3])
                    filewriter.writerow([chunks[3]])

        f.close()
