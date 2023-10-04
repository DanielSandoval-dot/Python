# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:44:50 2023

@author: Daniel Sandoval

"""


import psycopg2

conn = psycopg2.connect(host="localhost", dbname = "COMPANY 1", user ="postgres", password = "admin", port = 5433)

cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXIST person1(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
);
""")

conn.commit()
cur.close()
conn.close()

