# Available Kernels and Languages

<img src="https://raw.githubusercontent.com/JorgeCardona/recursos/main/docker_hub/jupyterlab%20multilenguajes%20python3.11.7.png"/>

| Aplication| Port|
|-------------|--------|
| JupyterLab  | 8888   |
| Apache Spark UI| 4040   |
| Panel       | 5006   |
| Node.js     | 3000   |

# EXAMPLES BY LANGUAGE

| Language   | Example                                                                                     |
|-----------|---------------------------------------------------------------------------------------------|
| Java      | public class Main {<br>&nbsp;&nbsp;&nbsp;&nbsp;public static void greeting() {<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System.out.println("Hello, Java!");<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>}<br> Main.greeting();|
| Node.js   |const http = require('http');<br><br>// Create the server<br>const server = http.createServer((req, res) => {<br>&nbsp;&nbsp;&nbsp;&nbsp;// Configure the server response<br>&nbsp;&nbsp;&nbsp;&nbsp;res.statusCode = 200;<br>&nbsp;&nbsp;&nbsp;&nbsp;res.setHeader('Content-Type', 'text/plain');<br>&nbsp;&nbsp;&nbsp;&nbsp;res.end('Hello, from JupyterLab Container!');<br>});<br><br>// Define the port on which the server will run<br>const port = 3000;<br><br>// Start the server<br>server.listen(port, () => {<br>&nbsp;&nbsp;&nbsp;&nbsp;console.log('Node.js server is running at http://localhost:' + port + '/');<br>});<br> |
| Kotlin    |fun main() {<br>&nbsp;&nbsp;&nbsp;&nbsp;// Print "Hello, Kotlin!"<br>&nbsp;&nbsp;&nbsp;&nbsp;println("Hello, Kotlin!")<br><br>&nbsp;&nbsp;&nbsp;&nbsp;// Define a function to calculate the square of a number<br>&nbsp;&nbsp;&nbsp;&nbsp;fun calculateSquare(number: Int): Int {<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return number * number<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br><br>&nbsp;&nbsp;&nbsp;&nbsp;// Use the function to calculate the square of 5<br>&nbsp;&nbsp;&nbsp;&nbsp;val result = calculateSquare(5)<br>&nbsp;&nbsp;&nbsp;&nbsp;println("Square of 5: \$result")<br>}<br> main()|
| R         |# Print "Hello, R!"<br>cat("Hello, R!\n")<br><br># Define a function to calculate the square of a number<br>calculateSquare <- function(number) {<br>&nbsp;&nbsp;&nbsp;&nbsp;return (number * number)<br>}<br><br># Use the function to calculate the square of 5<br>result <- calculateSquare(5)<br>cat("Square of 5: ", result, "\n")<br> |
| Scala     | // Print "Hello, Scala!"<br>println("Hello, Scala!")<br><br>// Define a function to calculate the square of a number<br>def calculateSquare(number: Int): Int = {<br>&nbsp;&nbsp;&nbsp;&nbsp;number * number<br>}<br><br>// Use the function to calculate the square of 5<br>val result = calculateSquare(5)<br><br>// Print the result<br>println("The square of 5 is: " + result)<br> |

# Packages Installed

| Package | Version|
|-------------|--------|
| jupyterlab | 4.0.9 |
| jupyterlab-git | 0.50.0 |
| pyspark | 3.4.1 |
| pandas | 1.5.3 |
| apache-beam[interactive] | 2.48.0 |
| panel| 1.3.5 |
| Faker | 21.0.0 |
| itables | 1.6.3 |
| mysql-connector-python | 8.2.0|
| psycopg2 | 2.9.9 |
| pymongo | 4.6.1 |
|  <a href="https://mvnrepository.com/artifact/org.postgresql/postgresql" target="_blank">JDBC postgresql.jar</a> |42.6.0|
|  <a href="https://mvnrepository.com/artifact/com.mysql/mysql-connector-j" target="_blank">JDBC mysql-connector-j.jar</a> |8.0.33|
|  <a href="https://mvnrepository.com/artifact/org.mongodb" target="_blank">bson, mongodb-driver-sync, mongodb-driver-core</a> |4.11.1|
|  <a href="https://mvnrepository.com/artifact/org.mongodb.spark/mongo-spark-connector" target="_blank">mongo-spark-connector.jar</a> |2.13-10.2.1|


# EXAMPLES OF INSTALLED PACKAGES
## You can use the following examples for testing, just copy and paste the following code to test each package.

| Package       | Description                                               | Advantages                                                   | Disadvantages                                               | Example                                                     |
|---------------|-----------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| itables | Library for tabular data manipulation in Python. | SQL-like syntax for querying.<br>- Integration with Python and pandas.<br>- Efficient handling of large datasets.<br>- Simplified tabular data manipulation. | May be less efficient for advanced operations compared to specialized libraries.<br>- Documentation can be limited.<br>- Less optimized than traditional databases.|# **to enable itables**<br>from itables import init_notebook_mode<br>init_notebook_mode(all_interactive=True)|
| pyspark       | Library for distributed processing with Apache Spark       | - Distributed and scalable processing                        | - Complex configuration and management                      | from pyspark.sql import SparkSession<br><br># Create a SparkSession<br>spark = SparkSession.builder.appName("JorgeCardonaSpark").getOrCreate()<br><br># Perform a simple DataFrame operation<br>data = [('Nathalie', 0), ('Ana', 3), ('Diana', 7), ('Lucia', 10), ('Tatiana', 13), ('Angela', 17), ('Cecilia', 25), ('Alice', 31), ('Kristin', 35), ('Carolina', 37), ('Lina', 39), ('Marcela', 40), ('Maria', 42)]<br><br># Create a Dataframe<br>df = spark.createDataFrame(data, ["Name", "Age"])<br>df.show() <br>spark.stop()|
| pandas        | Library for data manipulation and analysis                | - Efficient data manipulation and analysis functions         | - Limitations in handling large volumes of data              | import pandas as pd<br><br>data = {<br>&nbsp;&nbsp;&nbsp;&nbsp;'Name': ["Nathalie", "Ana", "Diana", "Lucia", "Tatiana", "Angela", "Cecilia", "Alice", "Kristin", "Carolina", "Lina", "Marcela", "Maria"],<br>&nbsp;&nbsp;&nbsp;&nbsp;'Age': [0, 3, 7, 10, 13, 17, 25, 31, 35, 37, 39, 40, 42]<br>}<br>df = pd.DataFrame(data)<br>df |
| apache-beam   | Programming model for data processing                     | - High-level abstraction for data processing                 | - Requires knowledge of parallel programming                 | import apache_beam as beam<br><br>def regular_case_function(element):<br>&nbsp;&nbsp;&nbsp;&nbsp;return element.lower()<br><br>def to_uppercase_function(element):<br>&nbsp;&nbsp;&nbsp;&nbsp;return element.upper()<br><br>def calculate_length_function(element):<br>&nbsp;&nbsp;&nbsp;&nbsp;return len(element)<br><br>def calculate_square_function(element):<br>&nbsp;&nbsp;&nbsp;&nbsp;return element ** 2<br><br># Create a pipeline<br>with beam.Pipeline() as pipeline:<br>&nbsp;&nbsp;&nbsp;&nbsp;# Prepare a list of names to be processed<br>&nbsp;&nbsp;&nbsp;&nbsp;names_list = ["Nathalie", "Ana", "Diana", "Lucia", "Tatiana", "Angela", "Cecilia", "Alice", "Kristin", "Carolina", "Lina", "Marcela", "Maria"]<br><br>&nbsp;&nbsp;&nbsp;&nbsp;# Create a PCollection with the given data<br>&nbsp;&nbsp;&nbsp;&nbsp;data = pipeline \| beam.Create(names_list)<br><br>&nbsp;&nbsp;&nbsp;&nbsp;# Apply transformation functions to the data<br>&nbsp;&nbsp;&nbsp;&nbsp;regular_case_data = data \| beam.Map(regular_case_function)  # Transform to lowercase<br>&nbsp;&nbsp;&nbsp;&nbsp;uppercase_data = data \| beam.Map(to_uppercase_function)  # Transform to uppercase<br>&nbsp;&nbsp;&nbsp;&nbsp;length_data = data \| beam.Map(calculate_length_function)  # Apply transformation to calculate the length of each name<br>&nbsp;&nbsp;&nbsp;&nbsp;square_data = length_data \| beam.Map(calculate_square_function)  # Apply transformation to calculate the square<br><br>&nbsp;&nbsp;&nbsp;&nbsp;# Print the results of each transformation<br>&nbsp;&nbsp;&nbsp;&nbsp;length_data \| "Show_Length" >> beam.Map(print)  # Print length results<br>&nbsp;&nbsp;&nbsp;&nbsp;regular_case_data \| "Show_Lowercase" >> beam.Map(print)  # Print lowercase results<br>&nbsp;&nbsp;&nbsp;&nbsp;uppercase_data \| "Show_Uppercase" >> beam.Map(print)  # Print uppercase results<br>&nbsp;&nbsp;&nbsp;&nbsp;square_data \| "Show_Square" >> beam.Map(print)  # Print square results |
| Faker         | Library for generating simulated data                      | - Easy generation of simulated data                          | - Not suitable for production environments                   | `from faker import Faker`<br>`fake = Faker()`<br>`name = fake.name()`<br>`print(name)` |
| Panel         | Library for creating interactive dashboards and apps       | - Powerful dashboard and app creation capabilities           | - Requires learning the Panel library                        | import panel as pn<br><br>def model(n=5):<br>&nbsp;&nbsp;&nbsp;&nbsp;return "⭐"*n<br><br>pn.extension()<br><br>slider = pn.widgets.IntSlider(value=5, start=1, end=5)<br><br>interactive_model = pn.bind(model, n=slider)<br><br>layout = pn.Column(slider, interactive_model)<br><br>app = pn.serve(layout, port=5006, show=True)<br><br> #app.stop() <br><br> # ✨ Panel UI APP ```http://localhost:5006```  <a href=" http://localhost:5006" target="_blank">CLICK HERE </a>✨
|

# ⚠️ For this image, it is **not necessary to use the token** to access the notebooks ⚠️
# How to run the image.

#  TEMPORAL CONTAINER


## 🔥If you want to just test the image and do not keep the container when you finish running the container use the next command:
#### ``` docker run --name jorgecardona-labmultilanguage --rm -p 8888:8888 -p 4040:4040 -p 5006:5006 -p 3000:3000  jorgecardona/jupyterlabmultilanguagespython3117:v1```

# PERSISTENT CONTAINER

## 💦If you want to keep the container, save the notebooks, and continue working on this container use the next command:💦
#### ``` docker run --name jorgecardona-labmultilanguage -p 8888:8888 -p 4040:4040 -p 5006:5006 -p 3000:3000 jorgecardona/jupyterlabmultilanguagespython3117:v1```

#  ACCESS TO JUPYTER LAB AND SPARK UI 

##  🐱 access to JUPYTERLAB ```http://localhost:8888```  <a href=" http://localhost:8888" target="_blank">CLICK HERE </a> 🐱
## 🐶access to sparkUI with pySpark  ```http://localhost:4040```  <a href=" http://localhost:4040" target="_blank">CLICK HERE </a>🐶

# 🌀To run Spark for Scala, on the terminal execute ```spark-shell``` command to start it.🌀
<img src="https://github.com/JorgeCardona/recursos/blob/main/docker_hub/running_spark.png?raw=true"/>

## 🐍access to sparkUI Running directly Apache Spark ```http://localhost:4040```  <a href=" http://localhost:4040" target="_blank">CLICK HERE </a>🐍
<img src="https://github.com/JorgeCardona/recursos/blob/main/docker_hub/spark_ui.png?raw=true"/>

### ADDED SUPPORT TO CONNECT SPARK FOR EXTRACTION DATA FROM MySQL, MongoDB, AND PostgreSQL
# PING to databases MySQL, MongoDB, PostgreSQL
# USE TEMPORAL DOCKER IMAGES FOR TESTING,  delete  *--rm* on docker command to do persistent databases

# DOCKER FOR PostgreSQL
##  `docker run --name jorgecardona-postgres --rm -e POSTGRES_DB=spark -e POSTGRES_PASSWORD=12345678 -e POSTGRES_USER=admin -d -p 5432:5432 postgres:15.4`

# DOCKER FOR MySQL
##  `docker run --name jorgecardona-mysql --rm -e MYSQL_DATABASE=spark -e MYSQL_PASSWORD=12345678 -e MYSQL_USER=admin -e MYSQL_ROOT_PASSWORD=root -d -p 3306:3306 mysql:8.1.0`

# DOCKER FOR MongoDB
###  `docker run --name jorgecardona-mongodb --rm -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=12345678 mongodb/mongodb-community-server:6.0.7-ubuntu2204-20230812T065949Z`

# STRING CONNECTION FOR SPECIFIC MONGO DB HOST
# `mongodb://admin:12345678@localhost:27017` 

# STRING CONNECTION FOR LOCAL DOCKER MONGO DB
# `mongodb://admin:12345678@host.docker.internal:27017`

# CODE FOR TESTING CONNECTION TO DATABASES
```
def test_mongo_connection(host, port, database, collection, user=None, password=None):
    """
    # Configure MongoDB credentials
    host = "host.docker.internal"  # Replace with the IP address or hostname of your MongoDB server
    port = 27017  # Default port for MongoDB
    database = "spark"  # Name of the database you want to connect to
    collection = "users"  # Name of the collection
    user = "admin"  # Username (optional, if MongoDB is configured with authentication)
    password = "12345678"  # Password (optional, if MongoDB is configured with authentication)
    
    # If you want to use authentication, you need to provide credentials
    # mongodb://admin:12345678@localhost:27017
    
    # test the connection
    test_mongo_connection(host, port, database, collection)
    """
    
    from pymongo import MongoClient
    try:
        # Try to connect to the MongoDB server if have an user and password
        client = MongoClient(host, port, username=user, password=password)

        # Try to connect to the MongoDB server if you do not have an user and password
        if not user or not password:
            client = MongoClient(host, port)

        # Select the database
        db = client[database]

        # Perform a simple read operation to verify the connection
        # You can use any query here; for example, count_documents({})
        collection_loaded = db[collection]
        result = collection_loaded.find_one()

        if result:
            print("Connection successful. MongoDB server is accessible.", result)
        else:
            print("Connection successful, but no data was found in the database.")
        
        client.close()
    except Exception as e:
        print(f"Error connecting to the database: {e}")
                
def test_postgres_connection(host, port, database, user, password):
    """
    # Configure PostgreSQL credentials
    host = "host.docker.internal"  # Replace with the IP address or hostname of your PostgreSQL server
    port = 5432  # Default port for PostgreSQL
    database = "spark"  # Name of the database you want to connect to
    user = "admin"  # Username
    password = "12345678"  # Password
    
    # test the connection
    test_postgres_connection(host, port, database, user, password)
    """
    import psycopg2
    try:
        # Try to connect to the database
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        connection.close()
        print("Connection successful. PostgreSQL server is accessible.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
                
def test_mysql_connection(host, port, database, user, password):
    """
    # Configure MySQL credentials
    host = "host.docker.internal"  # Replace with the IP address or hostname of your MySQL server
    port = 3306  # Default port for MySQL
    database = "spark"  # Name of the database you want to connect to
    user = "admin"  # Username
    password = "12345678"  # Password
    
    # test the connection
    test_mysql_connection(host, port, database, user, password)
    """    
    import mysql.connector
    try:
        # Try to connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        connection.close()
        print("Connection successful. MySQL server is accessible.")
        
    except Exception as e:
        print(f"Error connecting to the database: {e}")
```

# INSERT AND LOAD DATA FROM DATABASES USING SPARK
```
def get_database_configuration(database_type = 'mysql', host = None, port = None, database = None, table = None, user = None, password = None, input_collection = None, output_collection = None):
    from pyspark.sql import SparkSession
    
    databases = {
        'mongodb': {
            'app_name': 'MongoDB_Connector',
            'format_type':'mongodb',
            'host': host if database_type == 'mongodb' and host else 'host.docker.internal',
            'port': port if database_type == 'mongodb' and port else 27017,
            'user': user if database_type == 'mongodb' and user else 'admin',
            'password': password if database_type == 'mongodb' and password else '12345678',
            'database': database if database_type == 'mongodb' and database else 'spark',
            'input_collection':  input_collection if database_type == 'mongodb' and table else 'users',
            'output_collection': output_collection if database_type == 'mongodb' and table else 'users',
            'driver': 'com.mongodb.spark.sql.DefaultSource',
            'url': f"mongodb://{user}:{password}@{host}:{port}" if database_type == 'mongodb' and host and port else 'mongodb://admin:12345678@host.docker.internal:27017',
            'spark_session': SparkSession.builder.master('local').appName("MongoDB_Connector").getOrCreate()
            },
        'postgres': {
            'app_name': 'PostgreSQL_Connector',
            'format_type':'jdbc',
            'host': host if database_type == 'postgres' and host else 'host.docker.internal',
            'port': port if database_type == 'postgres' and port else 5432,
            'user': user if database_type == 'postgres' and user else 'admin',
            'password': password if database_type == 'postgres' and password else '12345678',
            'database': database if database_type == 'postgres' and database else 'spark',
            'table': table if database_type == 'postgres' and table else 'users',
            'schema': 'public',
            'spark_jars': '/usr/local/spark/jars/postgresql-42.7.1.jar',
            'driver': 'org.postgresql.Driver',
            'url': f"jdbc:postgresql://{host}:{port}/{database}" if database_type == 'postgres' and host and port else 'jdbc:postgresql://host.docker.internal:5432/spark',
            'properties': {
                'user': user if database_type == 'postgres' and user else 'admin',
                'password': password if database_type == 'postgres' and password else '12345678',
                'driver': 'org.postgresql.Driver'
            },
            'spark_session': SparkSession.builder.master('local').appName("PostgreSQL_Connector").config("spark.jars", '/usr/local/spark/jars/postgresql-42.6.0.jar').getOrCreate()
            },
        'mysql': {
            'app_name': 'MySQL_Connector',
            'format_type':'jdbc',
            'host': host if database_type == 'mysql' and host else 'host.docker.internal',
            'port': port if database_type == 'mysql' and port else 3306,
            'user': user if database_type == 'mysql' and user else 'admin',
            'password': password if database_type == 'mysql' and password else '12345678',
            'database': database if database_type == 'mysql' and database else 'spark',
            'table': table if database_type == 'mysql' and table else 'users',
            'spark_jars': '/usr/local/spark/jars/mysql-connector-j-8.2.0.jar',
            'driver': 'com.mysql.cj.jdbc.Driver',
            'url': f"jdbc:mysql://{host}:{port}/{database}" if database_type == 'mysql' and host and port else 'jdbc:mysql://host.docker.internal:3306/spark',
            'properties': { 
                            'user': user if database_type == 'mysql' and user else 'admin', 
                            'password': password if database_type == 'mysql' and password else '12345678', 
                            'driver': 'com.mysql.cj.jdbc.Driver'
            },
            'spark_session': SparkSession.builder.master('local').appName("MySQL_Connector").config("spark.jars", '/usr/local/spark/jars/mysql-connector-j-8.0.33.jar').getOrCreate()
            }
    }
    return databases.get(database_type.lower(), databases.get('mysql'))
```

# TEST DATABASES INSERT DATA
```
def insert_data_to_database(database_configuration, database_type=None):
    from pyspark.sql.functions import monotonically_increasing_id
    
    spark_session = database_configuration.get('spark_session')
    app_name = database_configuration.get('app_name')
    format_type = database_configuration.get('format_type')
    url = database_configuration.get('url')

    data = [(1, "Ana"), (2, "Cecilia"), (3, "Nathalie"), (4, "Diana"), (5, "Gabriela"), (6, "Angela"), (7, "Tatiana"), (8, "Lucia"), (9, "Maria")]
    columns = ["Id", "Name"]
    sampleDF = spark_session.createDataFrame(data, columns) # sample dataframe

    try:
        message = f'Records Inserted Successfully in {app_name}'
        if database_type == 'mongodb':
            sampleDF_with_id = sampleDF.withColumn("id", monotonically_increasing_id()) # add column 'id' to DataFrame
        
            database = database_configuration.get('database')
            collection = database_configuration.get('output_collection')
            sampleDF_with_id.write.format("mongodb") \
            .option("connection.uri", url) \
            .option("database", database) \
            .option("collection", collection) \
            .mode("append") \
            .save()
        else: 
            driver = database_configuration.get('driver')
            dbtable = database_configuration.get('table')
            user = database_configuration.get('user')
            password = database_configuration.get('password')    
        
            sampleDF.write \
                .format(format_type) \
                .option("driver", driver) \
                .option("url", url) \
                .option("dbtable", dbtable) \
                .option("user", user) \
                .option("password", password) \
                .mode("ignore") \
                .mode("append") \
                .save()
    except Exception as e:
        message = f"Error inserting data: {str(e)}"
    finally:
        spark_session.stop() # stop Spark session
        return message
```

## MYSQL
```
# GET DATABASE CONFIGURATION
mysql_configuration = get_database_configuration(database_type = 'mysql')

# INSERT DATA INTO DATABASE AND CREATES THE TABLE
insert_data_to_database(mysql_configuration)
```

## POSTGRESQL
```
# GET DATABASE CONFIGURATION
postgres_configuration = get_database_configuration(database_type = 'postgres')

# INSERT DATA INTO DATABASE AND CREATES THE TABLE
insert_data_to_database(postgres_configuration)
```

## MONGODB
```
# GET DATABASE CONFIGURATION
mongodb_configuration = get_database_configuration(database_type = 'mongodb')

# INSERT DATA INTO DATABASE AND CREATES THE COLLECTION
insert_data_to_database(database_configuration=mongodb_configuration, database_type = 'mongodb')
```

# TEST DATABASES READ DATA

```
def read_data_from_database(database_type='mysql', host=None, port=None, database=None, table=None, user=None, password=None, input_collection=None, output_collection=None):
    
    database_configuration = get_database_configuration(database_type=database_type, host=host, port=port, database=database, table=table, user=user, password=password, input_collection=input_collection, output_collection=output_collection)
    spark_dataframe = database_configuration.get('spark_session')
    properties = database_configuration.get('properties')
    url = database_configuration.get('url')
    
    try:
        if database_type == 'mongodb':
            database = database_configuration.get('database')
            collection = database_configuration.get('input_collection')

            result = spark_dataframe.read.format("mongodb").option("connection.uri", url).option("database", database).option("collection", collection).load()
        else:
            table = database_configuration.get('table')
            
            if database_configuration.get('schema'):
                table = f"{database_configuration.get('schema')}.{database_configuration.get('table')}"
            result = spark_dataframe.read.jdbc(url=url, table=table, properties=properties)
    except Exception as e:
        # Handle the specific MongoDB exception in Spark
        print(f"Error reading data: {str(e)}")
        result = None  # Another action you may want to take in case of an exception
    finally:
        result.printSchema()  # Print schema
        result.show()  # Show rows
        df = result.toPandas() # converts to pandas
        spark_dataframe.stop()
        return df
```

## MYSQL
```
read_data_from_database(database_type = 'mysql')
```

## POSTGRESQL
```
read_data_from_database(database_type = 'postgres')
```

## MONGODB
```
read_data_from_database(database_type = 'mongodb')
```

## stop the container CONTAINER_ID or NAME
## `docker stop jorgecardona-labmultilanguage  jorgecardona-postgres  jorgecardona-mysql  jorgecardona-mongodb`

## re start stopped CONTAINER_ID or NAME
# `docker start -i jorgecardona-labmultilanguage`

## remove container CONTAINER_ID or NAME
# `docker rm jorgecardona-labmultilanguage`

## 🐳 ```Original Dockerfile for this image```  <a href=" https://raw.githubusercontent.com/JorgeCardona/recursos/main/docker_hub/jupyterlab_multilanguages_dockerfile/Java%2017%2C%20Spark%203.5.0%20-%20Python%203.11.7/Dockerfile" target="_blank">CLICK HERE </a>🐳