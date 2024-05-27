import psycopg2

conn = psycopg2.connect(database = "postgres", user = "user", host= 'localhost', password ="admin",port = 54320)