import os
import csv

if __name__ == "__main__":

    import csv
    with open('appliances.csv', newline='') as f:
        reader = csv.reader(f)
        with open('applianceURLS.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            chunks = ''
            otherCount = 1
            for row in reader:
                if 'product-title' in row[1]:
                    count = 0
                    print(row[1])

                elif 'https://images-na.ssl-images-amazon.com/images/I/' in row[1]:
                    s = "."
                    if count == 0:
                        chunks = row[1].split('.')
                        temp = chunks[-2:]
                        filewriter.writerow([
                            s.join(chunks[0:-2]) + '.jpg'])
                        print(row[1])
                        count += 1
                    else:
                        chunks = row[1].split('.')
                        print(chunks)
                        if chunks[-2:] == temp:
                            filewriter.writerow([
                                s.join(chunks[0:-2]) + '.jpg'])
                            print(row[1])

        f.close()
