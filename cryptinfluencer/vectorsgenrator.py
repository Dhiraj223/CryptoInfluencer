from sentence_transformers import SentenceTransformer
from typing import List, Dict, Union
import uuid

class VectorStore:
    """
    A class for storing, indexing, and retrieving text data using vector embeddings,
    optimized for Retrieval-Augmented Generation (RAG).
    """

    def __init__(self, embedding_model_name: str = 'all-MiniLM-L6-v2'):
        """
        Initialize the VectorStore.

        Args:
            embedding_model_name (str): The name of the sentence transformer model to use for embeddings.
        """
        self.vectors = []  # List of tuples (id, embedding, chunks)
        self.model = SentenceTransformer(embedding_model_name)

    def add_texts(self, chunks: List[Dict[str, Union[str, int]]], user_id: str) -> None:
        """
        Add text chunks to the vector store.

        Args:
            chunks (List[Dict[str, Union[str, int]]]): A list of text chunks with their metadata.
        """
        for _, chunk in enumerate(chunks):
            embedding = self.model.encode(chunk['text'])
            metadata  = {
                "user_id" : user_id,
                "text" : chunk["text"]
            }
            self.vectors.append((f"{user_id}-{uuid.uuid4()}", embedding.tolist(), metadata))