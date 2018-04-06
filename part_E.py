#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="db2", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()

print("E.Q1")
cur.execute('''EXPLAIN SELECT * FROM cup_matches, played_in WHERE cup_matches.mid=played_in.mid;''')
print(cur.fetchall())
conn.commit()


print("\nE.Q2")
cur.execute('''SET enable_mergejoin = FALSE;''')
cur.execute('''EXPLAIN SELECT * FROM cup_matches, played_in WHERE cup_matches.mid=played_in.mid;''')
print(cur.fetchall())
conn.commit()

print("\nE.Q3")
cur.execute('''SET enable_hashjoin = FALSE;''')
cur.execute('''EXPLAIN SELECT * FROM cup_matches, played_in WHERE cup_matches.mid=played_in.mid;''')
print(cur.fetchall())
conn.commit()