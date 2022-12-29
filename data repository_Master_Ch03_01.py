import csv

with open('銀行利率.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(['銀行', '活期利率', '活期儲蓄利率'])
    writer.writerow(['國泰世華商業銀行', '0.010', '0.030'])
    writer.writerow(['玉山銀行', '0.010', '0.090'])
    writer.writerow(['中國信託銀行', '0.010', '0.050'])

with open('銀行利率.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    print(csv_header)
    for row in csv_reader:
        print('「{}」的活期利率為 {}，活期儲蓄利率為 {}'.format(row[0], row[1], row[2]))