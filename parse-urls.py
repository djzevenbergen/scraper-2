import os
import csv

if __name__ == "__main__":

    import csv
    with open('appliances.csv', newline='') as f:
        reader = csv.reader(f)
        f = open(f"testappliances.csv", "a")
        chunks = ''
        otherCount = 1
        for row in reader:
            if 'product-title' in row[1]:
                count = 0
                h = row[1].split("_")
                h = ",".join(h)
                f.write("\n" + str(otherCount) + "-- " + h + ",")
                print(row[1])
                otherCount += 1
            elif 'https://images-na.ssl-images-amazon.com/images/I/' in row[1]:
                s = "."
                if count == 0:
                    chunks = row[1].split('.')
                    temp = chunks[-2:]
                    f.write(s.join(chunks[0:-2]) + '.jpg' + ",")
                    print(row[1])
                    count += 1
                else:
                    chunks = row[1].split('.')
                    print(chunks)
                    if chunks[-2:] == temp:
                        f.write(s.join(chunks[0:-2]) + '.jpg' + ",")
                        print(row[1])

        f.close()
