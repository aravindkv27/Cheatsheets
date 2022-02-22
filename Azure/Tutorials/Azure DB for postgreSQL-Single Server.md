# Using Python to connect and query data in Azure Database for PostgreSQL- Single Server

## First Create a Resource Group
<br>

**Using Azure CLI**

```
az group create --name dbdemo --location eastus
```

## Create a PostgreSQL Single Server

I perfer Portal to create a DB

```
Admin : aravind
Password: MannyFortune27
```    

**Using Azure CLI**

This will create a db with default settings eg., core, version etc.,

```
az postgres server create --name aravind-demo-db --resource-group demodb --location eastus --admin-user aravind --admin-password MannyFortune27
```

In Local Machine,

## Install azure cli and login into azure

```
azure login #Login into azure 
 ```

## To install postgresql 

```
sudo apt-get install postgresql-12
```

## Connect to the server with psql

```
psql --host=aravind-demo-db.postgres.database.azure.com --port=5432 --username=aravind@aravind-demo-db --dbname=postgres
```

## Create a Database 

```
CREATE DATABASE demo;
```

## To switch DB

```
\c demo<DATABASE-NAME>
```

## Creata a python file

```
import psycopg2

# Update connection string information
host = "<server-name>"
dbname = "<database-name>"
user = "<admin-username>"
password = "<admin-password>"
sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()
```
## Create a Table

```
cursor.execute(
    "CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);"
    )

print("Finished creating table")
```

## Insert Data into Table 

```
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
print("Inserted 3 rows of data")
```

## To Read Data

```
cursor.execute(SELECT * FROM <Table-name>;)
rows=cursor.fetchall()

for row in rows:
    print(row)
    
```

## To delete the Resource Group with all the resources

```
az group delete --name <RG-name> --yes
```