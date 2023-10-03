import os
import time
import grpc
import psycopg2

import similarity_search_pb2
import similarity_search_pb2_grpc

from dotenv import load_dotenv
from concurrent import futures

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# load data from.env
load_dotenv()


# gRPC
class SimilaritySearchServicer(similarity_search_pb2_grpc.SimilaritySearchServicer):
    def __init__(self):
        # Connect to PgSQL
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_PASSWORD")
        db_port = os.getenv("DB_PORT")

        print("DB_NAME:", db_name)
        print("DB_USER:", db_user)
        print("DB_PASSWORD:", db_password)
        print("DB_HOST:", db_host)
        print("DB_PORT:", db_port)

        try:
            self.conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port
            )
            print("Database connection established successfully.")
        except Exception as e:
            print("Error connecting to the database:", e)

    @staticmethod
    def calculate_cosine_similarity(query, items):
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform([query] + [item[1] for item in items])
        cosine_similarities = cosine_similarity(X)
        return cosine_similarities[0][1:]

    def AddItem(self, request, context):
        # Add Method in DB
        item_id = request.item.id
        item_description = request.item.description

        with self.conn.cursor() as cur:
            # Check if identical item exist
            cur.execute("SELECT item_id FROM items WHERE item_id=%s;", (item_id,))
            if cur.fetchone() is not None:
                return similarity_search_pb2.AddItemResponse(success=False,
                                                             message=f"Item with ID '{item_id}' already exists.")

            # Added new element in DB
            cur.execute("INSERT INTO items (item_id, description) VALUES (%s, %s);", (item_id, item_description))
            self.conn.commit()

        return similarity_search_pb2.AddItemResponse(success=True,
                                                     message=f"Item with ID '{item_id}' added successfully.")

    def SearchItems(self, request, context):
        # Get the query from the request
        query = request.query

        # Retrieve all items from the database
        with self.conn.cursor() as cur:
            cur.execute("SELECT item_id, description FROM items;")
            items = cur.fetchall()

        # Calculate the cosine similarity between the query and items
        similarity_scores = self.calculate_cosine_similarity(query, items)

        # Create a list of SearchResult objects
        search_results = []
        for i, (item_id, item_description) in enumerate(items):
            similarity_score = similarity_scores[i]
            search_result = similarity_search_pb2.SearchResult(
                id=item_id,
                description=item_description,
                similarity_score=similarity_score
            )
            search_results.append(search_result)
        search_id = f"search_{time.time()}"
        return similarity_search_pb2.SearchItemsResponse(search_id=search_id)

    def GetSearchResults(self, request, context):
        return similarity_search_pb2.GetSearchResultsResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    similarity_search_pb2_grpc.add_SimilaritySearchServicer_to_server(SimilaritySearchServicer(), server)
    server.add_insecure_port('[::]:50051')

    server.start()
    print("Server started. Listening on port 50051.")
    try:
        # Keep the server running and wait for incoming requests until manually stopped
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
