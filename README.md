<h1>Project Description</h1>

<p>This project is a Python application that implements gRPC-based similarity search <br>
functionality. It consists of both client and server components for adding items to a search <br>
index, searching for similar items, and retrieving search results.</p>

<h3>Features</h3>
<p>● Add Items:You can add items to the search index by making gRPC requests to the server. <br>
Each item consists of an item_id and a description.</p>

<p>● Search Items: The server allows you to search for items similar to a given query. <br>
The search query consists of a description.</p>

<p>● AGet Search Results: You can retrieve the search results from the server.</p>

<h1>📍How to install: </h1>


<details><summary><h2>⬇Manual start:</h2></summary><br>
<h4>1 - Connect venv:</h4> 

```
python3 -m venv venv
```

<h4>2 - Activate it:</h4>
<p>For Windows</p>

``` 
.\venv\Scripts\activate
```

<p>For MacOS</p>

``` 
source venv/bin/activate 
```

<h4>3 - Install libraries:</h4>

```
pip install -r requirements.txt
```

<h4>Create DB in PostgreSQL:</h4>

```
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    item_id VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);
```


<h4>Create Your .env</h4>
In order to run the application, you need to set up a .env file with the following configuration:

```
DB_NAME=<your_database_name>
DB_USER=<your_database_user>
DB_PASSWORD=<your_database_password>
DB_HOST=<your_database_host>
DB_PORT=<your_database_port>
```

<h4>Create pb2: </h4>

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. similarity_search.proto
```

<h4>Run server:</h4>

```
python server.py
```

<h4>Run client:</h4>

```
python client.py
```

<h4>Run tests:</h4>

```
python -m unittest tests/test_server.py
```

</details>



<details><summary><h2>🐳How to connect Docker Compose:</h2></summary><br/>
<h4>UP Docker-compose:</h4>

```
docker-compose up --build
```

</details>

