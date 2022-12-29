import sqlite3

connection = sqlite3.connect('股票清單.db')
cursor = connection.cursor()
command = 'CREATE TABLE IF NOT EXISTS stock(id TEXT PRIMARY KEY, name TEXT, date TEXT)'
cursor.execute(command)

# cursor.execute('INSERT INTO stock VALUES ("1101", "台泥", "1962/02/09")')
# cursor.execute('INSERT INTO stock VALUES ("1102", "亞泥", "1962/06/08")')
# cursor.execute('INSERT INTO stock VALUES ("1103", "嘉泥", "1969/11/14")')
# connection.commit() # 更新資料庫內容

# cursor.execute('UPDATE stock SET date = "1969/11/15" WHERE id = "1103"')
# connection.commit()
# cursor.execute('DELETE FROM stock WHERE id = "1103"')
# connection.commit()

cursor.execute('Select * FROM stock')
stocks = cursor.fetchall()
for stock in stocks:
    print(f'證卷代號:{stock[0]} 名稱:{stock[1]} 上市日期:{stock[2]}')

cursor.execute('Select * FROM stock WHERE id= 1101')
stocks = cursor.fetchone()
print('證卷代號:{} 名稱:{} 上市日期:{}'.format(stock[0],stock[1],stock[2]))

connection.close()