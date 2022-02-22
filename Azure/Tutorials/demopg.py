import psycopg2

# Update connection string information
host = "aravind-demo-db.postgres.database.azure.com"
dbname = "demo"
user = "aravind@aravind-demo-db"
password = "MannyFortune27"
sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

# Drop previous table of same name if one exists
# cursor.execute("DROP TABLE IF EXISTS inventory;")
# print("Finished dropping table (if existed)")

# # Create a table
# cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
# print("Finished creating table")

# # Insert some data into the table
# cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
# cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
# cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
# print("Inserted 3 rows of data")

cursor.execute("SELECT * FROM inventory;")
rows=cursor.fetchall()

for row in rows:

    print(row)
# Clean up
conn.commit()
cursor.close()
conn.close()