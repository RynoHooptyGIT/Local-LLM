import ollama
import numpy as np
from typing import List, Dict


class VectorStore:
    """A simple vector store using Ollama embeddings."""

    def __init__(self, embedding_model: str = "nomic-embed-text"):
        self.embedding_model = embedding_model
        self.documents: Dict[str, str] = {}  # id -> text
        self.embeddings: Dict[str, np.ndarray] = {}  # id -> embedding vector
        self.metadata: Dict[str, dict] = {}  # id -> metadata

    def _get_embedding(self, text: str) -> np.ndarray:
        """Get embedding vector for text using Ollama."""
        response = ollama.embeddings(model=self.embedding_model, prompt = text)
        embedding_vector = np.array(response.embedding)
        
        return embedding_vector
    
    def _cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Calculate cosine similarity between two vectors."""
        similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        return similarity


    def add_documents(self, texts: List[str], metadatas: List[dict], ids: List[str]):
        """Add documents to the vector store."""
        for text, metadata, doc_id in zip(texts, metadatas, ids):
            embedding = self._get_embedding(text)
            self.documents[doc_id] = text
            self.embeddings[doc_id] = embedding
            self.metadata[doc_id] = metadata


    def search(self, query: str, n_results: int = 5) -> Dict:
        """Search for documents similar to the query."""
        query_embedding = self._get_embedding(query)
        similarities = {}

        for doc_id, embedding in self.embeddings.items():
            similarity = self._cosine_similarity(query_embedding, embedding)
            similarities[doc_id] = similarity

        # Sort by similarity and return top n_results
        sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        top_docs = sorted_similarities[:n_results]

        # Return the results (double-nested lists to match ChromaDB format)
        return {
            "ids": [[doc_id for doc_id, _ in top_docs]],
            "documents": [[self.documents[doc_id] for doc_id, _ in top_docs]],
            "metadatas": [[self.metadata[doc_id] for doc_id, _ in top_docs]],
            "distances": [[1 - similarity for _, similarity in top_docs]]
        }