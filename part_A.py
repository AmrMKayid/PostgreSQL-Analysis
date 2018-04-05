#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="db2", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()


cur.execute('''DROP INDEX posIndx;''')
conn.commit()

print("A.Q1")
cur.execute('''EXPLAIN SELECT * from played_in WHERE position=1;''')
print(cur.fetchall())
conn.commit()


print("\nA.Q2")
print("cost=0.00..1113.00") ## TODO: change

print("\nA.Q3")
cur.execute('''CREATE INDEX posIndx ON played_in (position);''')
conn.commit()
print("After posIndex")
cur.execute('''EXPLAIN SELECT * from played_in WHERE position=1;''')
print(cur.fetchall())
conn.commit()

print("\nA.Q4")
print("cost=0.00..158.59")  ## TODO: change 

print("\nA.Q5")
print("")   ## TODO: Explain