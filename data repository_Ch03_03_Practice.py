import sqlite3
import requests
import csv
from bs4 import BeautifulSoup


connection = sqlite3.connect('上市股票清單.db')
cursor = connection.cursor()
cursor.execute('DELETE FROM stock')
command = "CREATE TABLE IF NOT EXISTS stock(id TEXT PRIMARY KEY, name TEXT, date TEXT, industry TEXT)"
cursor.execute(command)

url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'



headers = {
    'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.select('table')[1]

#cursor.execute('INSERT INTO stock VALUES ("2324", "仁寶", "2000/12/03", "資訊")')

for tr in table.select('tr')[2:]:
    try:
        stock_id = tr.select('td')[0].text.split('\u3000')[0] # 將空白分開兩個資料
        stock_name = tr.select('td')[0].text.split('\u3000')[1]
        stock_date = tr.select('td')[2].text
        stock_industry = tr.select('td')[4].text
        cursor.execute('INSERT INTO stock VALUES ("{}", "{}", "{}", "{}")'.format(stock_id, stock_name, stock_date, stock_industry))
    except:
        print("tr")
connection.commit()