import sqlite3

Database="AUTHDB"
Table="AUTHLOG"

def create_table(Database,Table):
  conn = sqlite3.connect(Database)
  c = conn.cursor()
  c.execute(f'CREATE TABLE {Table}(LOG_ID integer primary key AUTOINCREMENT, USER text, AUTH text);')
  conn.commit()
  conn.close()

def create_log(Database,Table):
  conn = sqlite3.connect(Database)
  c = conn.cursor()
  c.execute(f'CREATE TABLE {Table}(LOG_ID integer primary key AUTOINCREMENT, DATE text, STATUS text);')
  conn.commit()
  conn.close()

def log_insert(Database,Table,Status="OK"):
  DT=datetime.datetime.now()
  conn=sqlite3.connect(Database)
  c= conn.cursor()
  c.execute(f'''INSERT INTO {Table} (DATE, STATUS) VALUES ("{DT}",'{Status}'); ''')
  conn.commit()
  conn.close()


def display(Database, Table):
  conn = sqlite3.connect(Database)
  c = conn.cursor()
  c.execute(f'SELECT * FROM {Table};')
  return c.fetchall()
  conn.close()


#AUTHSCAN SQL

def authscan(Database,Table,user):
  conn= sqlite3.connect(Database)
  curs= conn.cursor()
  curs.execute(f'''Select Auth from {Table} WHERE USER == "{user}";''')
  try:
    for x in curs.fetchone():
      if x=="YES":
        return True
  except:
    return False
  conn.close()

def insert_data(Database,Table,User,Auth="YES"):
  conn = sqlite3.connect(Database)
  c = conn.cursor()
  c.execute(f'''INSERT INTO {Table} (USER,AUTH)  Values ("{User}","{Auth}"); ''') 
  conn.commit()
  conn.close()


def count(Database,Table, Column):
  conn=sqlite3.connect(Database)
  curs=conn.cursor()
  curs.execute(f'''Select COUNT({Column}) from {Table};''')
  return "Table {} Entries: {}".format(Table,curs.fetchone()[0])
  conn.commit()
  conn.close()

def add_column(Database,Table,Column):
  conn = sqlite3.connect(Database)
  c = conn.cursor()
  c.execute('ALTER TABLE {Table} ADD COLUMN {Column}')
  conn.commit()
  conn.close()

def del_data(Database,Table):
  conn = sqlite3.connect(Database)
  c = conn.cursor()  
  c.execute(f'''DELETE FROM {Table} WHERE x = "x"''')
  conn.commit()
  conn.close()

def update_data(Database,Table):
  conn = sqlite3.connect(Database)
  c = conn.cursor()
  c.execute(f''' UPDATE {Table}  SET x = "x"  WHERE x= "x"
  ''')
  conn.commit()
  conn.close()

def search(Database,Table):
  conn = sqlite3.connect(Database)
  curs = conn.cursor()
  curs.execute(f'''
  SELECT * FROM {Table}
  
  ''')
  return(curs.fetchall())
  conn.commit()
  conn.close()