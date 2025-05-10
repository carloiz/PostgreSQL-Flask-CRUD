import psycopg2

conn = psycopg2.connect(database="sampledb",host="localhost",user="postgres",password="1234",port="5432")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS members (id serial PRIMARY KEY, name varchar(100), age integer, address varchar(100))''')

cur.execute('''INSERT INTO members (name,age,address) VALUES ('carlo',28,'QC'),('cathleen',26,'Caloocan')''')

conn.commit()

cur.close()
conn.close()