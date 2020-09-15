import os
import csv

if __name__ == "__main__":

    import csv
    with open('appliances-Kismile-Removable-Standing-Adjustable-Temperature', newline='') as f:
        reader = csv.reader(f)
        f = open(f"appliances.txt", "a")
        chunks = ''
        for row in reader:
            if 'product-title' in row[1]:
                count = 0
                f.write(row[1] + "\n")
                print(row[1])
            elif 'https://images-na.ssl-images-amazon.com/images/I/' in row[1]:

                if count == 0:
                    chunks = row[1].split('.')
                    temp = chunks[-2:]
                    f.write(row[1] + "\n")
                    print(row[1])
                    count += 1
                else:
                    chunks = row[1].split('.')
                    print(chunks)
                    if chunks[-2:] == temp:
                        f.write(row[1] + "\n")
                        print(row[1])

        f.close()
