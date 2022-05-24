## Azure Storage Services

### Azure Blob Storage

- BLOB (Binary Large Object)- file.
- Unstructured data
- Blob stoarge contains container.
- Each container contains different blobs
- png, svg, exe, txt.
- Three stoarge tiers
    - Hot- Frequently accessed data
    - Cool - Infrequently accessed data(lower availability, high durability)
    - Archive - rarely accessed data

### Azure Queue Storage

- Storage for small piece of data
- designed for scalable asynchronous processing

### Azure Table Storage

- Semi structured data
- part of table storage.
- NoSQL db
    - no need for foreign joins, keys or strict schema
- designed for fast access
- Many programmes and ides

### Azure file storage

 - same like a blob storage
 - Difference between blog and file storage
        - Blobs- file
        - Container- share
        - blob storage- file storage
 - The main difference is way of access them via SMP protocol.
 - if we need file shared drive protocol we use file storage
 - BLOB and File Storage. They are both file storage services but BLOB has TONS and TONS of features for programming applications which need file storage capability where File Storage service is very simple and only purpose is Share Drive connectivity.
 - File Storage is so much more expensive than BLOB storage while functionality is less extensive.

 ### Azure storage account

- it offers a group of storage services
- used to store files, messages and semi structured data.
- Highly scalable upto petabytes of data
- Highly durable
- cheapest per GB storage


### Azure Disk Storage
- used for virtual machine.
- Disk emulation in the cloud.
- comes with different sizes, types(SSD, HDD) and tiers
- Disk can be unmanaged and managed.

## Azure Database Services

- Structured and semi-structured data

### Azure Cosmos DB

- Ability to replicate geographically
- available in many region.
- low-latency database
- Globally distributed NoSQL semi-structured database service
- schema-less
- Allows multiple api's like sql, mongodb, cassandra, table storage, germlin(graph database).

### Azure SQL Database

- Relational database in the cloud(PaaS)(DBaaS- database as a service)
- Structured data service defined using schema and relationship
- Rich query capabilities
- High-performance, reliable, fully managed and secure db for building applications.
- Most stable version.

### Azure SQL

- SQL Database
- Managed Instance
- SQL Data warehouse
- SQL VM in server
- bit costly