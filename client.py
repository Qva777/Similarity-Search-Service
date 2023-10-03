import grpc
import similarity_search_pb2
import similarity_search_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = similarity_search_pb2_grpc.SimilaritySearchStub(channel)

    # Testing method AddItem
    item = similarity_search_pb2.Item(id="item1", description="This is item 1.")
    response = stub.AddItem(similarity_search_pb2.AddItemRequest(item=item))
    print("AddItem response:", response)

    # Testing method SearchItems
    query = "item"
    search_response = stub.SearchItems(similarity_search_pb2.SearchItemsRequest(query=query))
    print("SearchItems response:", search_response)

    # Testing method GetSearchResults
    search_id = search_response.search_id
    results_response = stub.GetSearchResults(similarity_search_pb2.GetSearchResultsRequest(search_id=search_id))
    print("GetSearchResults response:", results_response)


if __name__ == '__main__':
    run()

