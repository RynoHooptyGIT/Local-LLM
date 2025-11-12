import ollama
from vector_store import VectorStore
from typing import List, Dict


class RAGQA:
    """Retrieval-Augmented Generation Question Answering system."""

    def __init__(self, vector_store: VectorStore, llm_model: str = "deepseek-r1:8b"):
        """
        Initialize the RAG QA system.

        Args:
            vector_store: VectorStore instance containing documents
            llm_model: Name of the Ollama LLM model to use
        """
        # TODO: Store the vector_store and llm_model as instance variables
        pass

    def ask(self, question: str, n_results: int = 5) -> Dict:
        """
        Ask a question and get an answer based on the document store.

        Args:
            question: The question to answer
            n_results: Number of relevant chunks to retrieve

        Returns:
            Dictionary with:
            - answer: The generated answer
            - sources: List of source documents used
            - relevant_chunks: The chunks used as context
        """
        # TODO: Step 1 - Search vector store for relevant chunks
        # Hint: Use self.vector_store.search(question, n_results)

        # TODO: Step 2 - Extract the document texts from search results
        # Hint: results["documents"][0] gives you the list of documents

        # TODO: Step 3 - Build a prompt with context and question
        # Format: "Context: {chunks}\n\nQuestion: {question}\n\nAnswer:"

        # TODO: Step 4 - Call Ollama to generate answer
        # Hint: Use ollama.chat() with model and messages

        # TODO: Step 5 - Extract unique sources from metadata
        # Hint: results["metadatas"][0] contains the metadata list

        # TODO: Step 6 - Return the formatted response
        pass
