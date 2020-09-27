import sqlite3
from model.demo import Demo
from contextlib import closing

db_name = "demo.db"
model_name = "produtos"

def con():
    return sqlite3.connect(db_name)

def listar():
    registros = []
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name}")
        rows = cursor.fetchall()
        for (id_produto, name, description, price, image, availibility, price_history, meta_tag, store_link) in rows:
            registros.append({"id_produto": id_produto, "name": name, "description": description, "price": price, "image": image, "availibility": availibility, "price_history": price_history, "meta_tag": meta_tag, "store_link": store_link})
        return registros
