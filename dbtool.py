#for testing 
from faker import Faker
import sqlite3
# import uuid

con=sqlite3.connect('users.db')
cur=con.cursor()

def create_mock_users(user_num=20):
    users={}
    for i in range(user_num):
        username=Faker().profile()["username"]
        password=Faker().password()
        users[username]=password
        # cur.execute(f'INSERT INTO users VALUES ("{uuid.uuid4()}","{username}","{password}")')
        cur.execute(f'INSERT INTO users VALUES ("{username}","{password}")')

    con.commit()    
    cur.close()
    con.close()

    return users

def initialize():
    # cur.execute('CREATE TABLE IF NOT EXISTS users ("id" INTEGER, "username" TEXT, "password" TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS users ("username" TEXT, "password" TEXT)')
    create_mock_users()

initialize()