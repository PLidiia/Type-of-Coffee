import sqlite3

# в виде ID представляются последние символов адреса данного кофе на сервисе яндекс маркет
ID = ['924574', '1511150', '58573388']
NAME_SORT = ['смесь арабики и робусты', 'смесь арабики и робусты', 'арабика']
DEGREE_FRIED = ['светлая', 'очень тёмная', 'средняя']
TYPE = ['seeds', 'milled', 'seeds']
DESCRIPTION = ['Кофе в зернах MacCoffee Pure Espresso Forte', 'Кофе молотый Peppos Coffee CREMA E AROMA',
               'Кофе для эспрессо Эфиопия Иргачефф Нат Tasty Coffee, в зернах']
PRICE = ['999', '384', '1605']
VOLUME = ['1000', '250', '1000']
con = sqlite3.connect('coffee.bd')
cur = con.cursor()
for item in range(3):
    cur.execute(
        "INSERT INTO info (ID, name_sort, degree_fried, type, description, price, volume) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (ID[item], NAME_SORT[item], DEGREE_FRIED[item], TYPE[item], DESCRIPTION[item],
         PRICE[item], VOLUME[item]))
    print('add')
    con.commit()
