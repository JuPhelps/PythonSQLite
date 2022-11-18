import sqlite3




conn = sqlite3.connect('test.db')

cursor = conn.cursor()

#Create Table
table = """ CREATE TABLE IF NOT EXISTS tab1 (
id INTEGER PRIMARY KEY,
var1 REAL,
var2 TEXT,
var3 INTEGER)"""

#Create table 2
table = """ CREATE TABLE IF NOT EXISTS tab2 (
tab2_id INTEGER PRIMARY KEY,
var1 REAL,
var2 TEXT,
var3 INTEGER)"""

insert = """INSERT INTO tab1 (var1, var2, var3) VALUES(2.1, "Ally", 53)"""

select = """SELECT * FROM tab1"""

delete = """DELETE FROM tab1 WHERE var2="Helen" """

#cursor.execute(table)
#cursor.execute(insert)
a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)
conn.commit()

select = """SELECT var2, var3 FROM tab1"""
a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)

select = """SELECT id, var2, var3 FROM tab1 WHERE id=2"""
a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)

#cursor.execute(delete)

select = """SELECT var2, var3 FROM tab1"""
a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)
  
print("here")
select = """SELECT var2, var3 FROM tab1 WHERE var2="Louise" AND var3=10 """
a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)

print("here")
select = """SELECT var2, var3 FROM tab1 WHERE var2 LIKE "%Jam%" AND var3=10 """
a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)

conn.commit()
print("end")