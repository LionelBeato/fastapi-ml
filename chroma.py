import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=["This is a document", "This is another document", "dogs wear hats", "dogs wear overalls"],
    metadatas=[{"source": "my_source"}, {"source": "my_source"}, {"source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2", "id3", "id4"]
)

results = collection.query(
    query_texts=["What dogs wear"],
    n_results=2
)