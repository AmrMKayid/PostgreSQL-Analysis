#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="db2", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()


cur.execute('''DROP INDEX ratingIndx;''')
conn.commit()

print("C.Q1")
cur.execute('''EXPLAIN SELECT * from cup_matches WHERE rating*3 > 20;''')
print(cur.fetchall())
conn.commit()



print("\nC.Q2")
print("cost=0.00..58.20") ## TODO: change


print("\nC.Q3")
cur.execute('''CREATE INDEX ratingIndx ON cup_matches (rating);''')
conn.commit()
print("After posIndex")
cur.execute('''EXPLAIN SELECT * from cup_matches WHERE rating*3 > 20;''')
print(cur.fetchall())
conn.commit()

print("\nC.Q4")
print("cost=0.00..58.20") ## TODO: change

print("\nC.Q5")
print("")   ## TODO: Explain => Same!!