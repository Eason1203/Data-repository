import requests
import csv
from bs4 import BeautifulSoup

url = 'http://www.taiwanrate.com/'

headers = {
    'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
#print(response.text)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

table = soup.select('table#table1')[0]

# for td in table.select('tr.bodytablehead td'):
#     fieldnames.append(td.text.strip())
# #print(fieldnames)

# for tr in table.select('tr'):
#     for td in tr.select('td'):
#      fieldnames.append(td.text.strip())
# #print(fieldnames)

# for tr in table.select('tr')[1:]:
#      fieldnames.append(td.text.strip())
#      print([td.text.strip() for td in tr.select('td')])

#print(fieldnames)
#fieldnames=[td.text.strip() for td in table.select('tr.bodytablehead td')]
#print(fieldnames)

# with open('銀行利率查詢利率比較表3.csv', mode='w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     fieldnames = [td.text.strip() for td in table.select('tr.bodytablehead td')]
#     writer.writerow(fieldnames)
#     for tr in table.select('tr')[1:]:
#         writer.writerow([td.text for td in tr.select('td')])

fieldnames=[]

with open('銀行利率查詢利率比較表5.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for tr in table.select('tr'):
        writer.writerow([td.text.strip() for td in tr.select('td')])
        # for td in tr.select('td'):
        #    fieldnames.append(td.text.strip())
    #print(fieldnames)    
    #writer.writerow(fieldnames)

with open('銀行利率查詢利率比較表6.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for tr in table.select('tr'):
        for td in tr.select('td'):
            writer.writerow([td.text.strip()])
    #print(fieldnames)    
    #writer.writerow(fieldnames)


#   with open('銀行利率查詢利率比較表2.csv', mode='w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     fieldnames = [td.text.strip() for td in table.select('tr.bodytablehead td')]
#     writer.writerow(fieldnames)
#     for tr in table.select('tr')[1:]:
#         writer.writerow([td.text for td in tr.select('td')])