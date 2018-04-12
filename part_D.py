#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="db2", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()

# ## Uncomment after first run
# cur.execute('''DROP INDEX cup_yearIndx; DROP INDEX playedin_yearIndx;''')
# conn.commit()

print("D.Q1")
cur.execute('''EXPLAIN SELECT * from cup_matches, played_in WHERE cup_matches.year=played_in.year;''')
print(cur.fetchall())
conn.commit()


print("\nD.Q2")
cur.execute('''CREATE INDEX cup_yearIndx ON cup_matches (year);''')
conn.commit()
print("After cup_yearIndx")
cur.execute('''EXPLAIN SELECT * from cup_matches, played_in WHERE cup_matches.year=played_in.year;''')
print(cur.fetchall())
conn.commit()

print("\nD.Q3")
print("")   ## TODO: Explain => Different


print("\nD.Q4")
cur.execute('''CREATE INDEX playedin_yearIndx ON played_in (year);''')
conn.commit()
print("After playedin_yearIndx")
cur.execute('''EXPLAIN SELECT * from cup_matches, played_in WHERE cup_matches.year=played_in.year;''')
print(cur.fetchall())
conn.commit()


print("\nD.Q5")
print("")   ## TODO: Explain => Different
