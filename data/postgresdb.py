import sqlite3

conn = sqlite3.connect('register.db')
c = conn.cursor()

def initdb():
    conn.execute("CREATE TABLE public.register (name varchar NOT NULL,"
                                         "familly_name varchar NOT NULL,"
                                         "age varchar NOT NULL,"
                                         "birthday varchar NOT NULL,"
                                         "hobby varchar NULL,"
                                         "email varchar NULL,"
                                         "password varchar NULL)")



def save(name, familly, hobby, new_hobby):
    c.execute("INSERT INTO public.register (name, familly_name, age, birthday, email)")

def update():
    pass

def delete():
    pass

def select():
    return None





