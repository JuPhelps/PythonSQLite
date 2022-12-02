import sqlite3
import csv

conn = sqlite3.connect('test.db')
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()
conn.commit()
print("fk")
a =cursor.execute("""PRAGMA foreign_keys""")
for row in a:
  print(row)

#Create Table
table = """ CREATE TABLE IF NOT EXISTS tab1 (
id INTEGER PRIMARY KEY,
var1 REAL,
var2 TEXT,
var3 INTEGER
)"""
#cursor.execute(table)

#Create table 2
table = """ CREATE TABLE IF NOT EXISTS tab2 (
tab2_id INTEGER PRIMARY KEY,
var4 REAL,
var5 TEXT,
var6 INTEGER,
FOREIGN KEY (var6)
REFERENCES tab1 (id)
)"""

with open('testdata.csv') as fileobject:
  fdata = csv.reader(fileobject)
  print(len(list(fileobject)))
  fileobject.seek(0)
  for row in fdata:
    print(row)
    print(float(row[0]))
    print(row[1])
    print(int(row[2]))
    # insert = "INSERT INTO tab2 (var4,var5, var6) VALUES("+float(row[0])"+","+ row[1]+","+ int(row[2]))"
    insert = "INSERT INTO tab2 (var4,var5, var6) VALUES("+str(float(row[0]))+",\""+str(row[1])+"\","+row[2]+")"
    print(type(insert))
    print(insert)
    #cursor.execute(insert)
#conn.committ()
    
insert = """INSERT INTO tab1 (var1, var2, var3) VALUES(2.1, "Dr. Hubbard", 55),
(1.1, "Dr. Roberts", 867)"""
#cursor.execute(insert)
#insert = """INSERT INTO tab1 (var1, var2, var3) VALUES(2.1, "Ally", 53)"""

insert = """INSERT INTO tab2 (var4, var5, var6) VALUES (9.8, "Pete", 8)"""
print(insert)
#cursor.execute(insert)
conn.commit()
select = """SELECT *FROM tab2"""

#a = cursor.execute(select)
delete = """DELETE FROM tab1 WHERE id=6 """
cursor.execute(delete)
#cursor.execute(table)
#cursor.execute(insert)
print("tab2")
a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)
print("begingin join")
select = """SELECT var2, var5 FROM tab2 JOIN tab1 ON tab2.var6 = tab1.var3 """
select = """SELECT id, var2, tab2.var5, var6 FROM tab1 JOIN tab2 ON tab1.id = tab2.var6 """
a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)
print("split")
conn.commit()
select = """SELECT id, var2, var5, var6 FROM tab1 JOIN tab2 ON tab1.id = tab2.var6 WHERE tab2.var6=2"""
a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)
conn.commit()
print("end join")

select = """SELECT id, var2, var3 FROM tab1"""
#a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)

select = """SELECT id, var2, var3 FROM tab1 WHERE id=2"""
#a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)

#cursor.execute(delete)

select = """SELECT * FROM tab1"""
print("tab1")
a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)
  
select = """SELECT var2, var3 FROM tab1 WHERE var2="Louise" AND var3=10 """
#a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)

select = """SELECT var2, var3 FROM tab1 WHERE var2 LIKE "%Jam%" AND var3=10 """
#a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  print(row)

select = """SELECT * FROM tab2 """
#a = cursor.execute(select)
rows = a.fetchall()
for row in rows:
  #print(row.description)
  print(row)
#cursor.execute("""DROP TABLE tab2""")
conn.commit()

a = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'""")

print(cursor.fetchall())
rows = a.fetchall()
for row in rows:
  print(row)
print(cursor.description)
colnames = cursor.description
for row in colnames:
  print(row[0])
print("end")