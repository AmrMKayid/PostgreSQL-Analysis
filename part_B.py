#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="db2", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()

# ## Uncomment after first run
# cur.execute('''DROP INDEX nameIndx;''')
# conn.commit()

print("B.Q1")
cur.execute('''EXPLAIN SELECT * from played_in WHERE name like '%pele%';''')
print(cur.fetchall())
conn.commit()

print("\nB.Q2")
print("cost=0.00..1113.00") ## TODO: change


print("\nA.Q3")
cur.execute('''CREATE INDEX nameIndx ON played_in (name);''')
conn.commit()
print("After nameIndx")
cur.execute('''EXPLAIN SELECT * from played_in WHERE name like '%pele%';''')
print(cur.fetchall())
conn.commit()

print("\nB.Q4")
print("cost=0.00..1113.00") ## TODO: change

print("\nB.Q5")
print("")   ## TODO: Explain => Same