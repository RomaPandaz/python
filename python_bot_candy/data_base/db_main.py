import sqlite3

con = sqlite3.connect('data_base/db_bot.db')
cur = con.cursor()

def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS candy (id_tg INTEGER PRIMARY KEY,
                    name VARCHAR, count_candy INTEGER, username VARCHAR)''')
    con.commit()

def add_player(player: tuple):
    cur.execute('''INSERT INTO candy (id_tg, name, count_candy, username) VALUES (?, ?, ?, ?)''',
                player)
    con.commit()

def set_candy_db(set_candy: int, tg_id: int):
    cur.execute('''UPDATE candy SET count_candy=? WHERE id_tg=?''', (set_candy, tg_id))
    con.commit()

def select_count(tg_id):
    result = cur.execute('''SELECT (count_candy) FROM candy WHERE candy.id_tg=?''',
                          (tg_id,)).fetchall()
    return result[0][0]