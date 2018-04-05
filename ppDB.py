#!/usr/bin/python

import psycopg2
import string
import random

chars = string.ascii_uppercase + string.digits

conn = psycopg2.connect(database="db2", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

cur = conn.cursor()

######################## cup_matches ########################

cur.execute('''DROP TABLE cup_matches''')
print("DROP cup_matches")
conn.commit()

cur.execute('''CREATE TABLE cup_matches
      (mid INT PRIMARY KEY     NOT NULL,
      round           TEXT,
      year            INT,
      num_ratings     INT,
      rating         REAL);''')

print("CREATE cup_matches")
conn.commit()


for i in range(2680):
    round = ''.join(random.choice(chars) for _ in range(7))
    year = random.choice(range(1500, 2018))
    num_ratings = random.choice(range(0, 10000))
    rating = random.choice(range(0, 10))
    command = "INSERT INTO cup_matches VALUES ({}, '{}', {}, {}, {})".format(i, round, year, num_ratings, rating)
    cur.execute(command);
    conn.commit()
    # print("Records created successfully");


######################## played_in ########################

cur.execute('''DROP TABLE played_in''')
print("DROP played_in")
conn.commit()

cur.execute('''CREATE TABLE played_in
      (mid            INT,
      name           TEXT,
      year            INT,
      position        INT,
      PRIMARY KEY(mid, name));''')

print("CREATE played_in")
conn.commit()

for i in range(58960):
    year = random.choice(range(1500, 2018))
    position = random.choice(range(0, 7))
    if i < 118:
        name = 'pele' + str(i)
        command = "INSERT INTO played_in VALUES ({}, '{}', {}, {})".format(i, name, year, position)
        cur.execute(command);
        conn.commit()
    else:
        name = ''.join(random.choice(chars) for _ in range(5))
        command = "INSERT INTO played_in VALUES ({}, '{}', {}, {})".format(i, name + str(i), year, position)
        cur.execute(command);
        conn.commit()
    # print("Records created successfully");


#############################################################
cur.execute('''SELECT COUNT(*) FROM cup_matches;''')
print("cup_matches count: " + str(cur.fetchall()))

cur.execute('''SELECT COUNT(*) FROM played_in;''')
print("played_in count: " + str(cur.fetchall()))

conn.close()