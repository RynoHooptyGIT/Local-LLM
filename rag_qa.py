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
        self.vector_store = vector_store
        self.llm_model = llm_model

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
        result = self.vector_store.search(question, n_results)
        
        # Step 3 - Extract relevant chunks from search results
        chunks = result["documents"][0]

        # Step 4 - Create prompt for LLM, combining question and context
        context = "\n\n".join(chunks)
        prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"

        # Generate answer using Ollama LLM with model and message
        response = ollama.chat(model=self.llm_model, messages=[{'role': 'user', 'content': prompt}])
        answer = response['message']['content']

        # Step 5 - Format and return the response by telling user source documents that were used
        sources = list(set([meta['source'] for meta in result['metadatas'][0]]))
        
        # Return the answer, sources, and relevant chunks in a dictionary
        return {
            "answer": answer,
            "sources": sources,
            "relevant_chunks": chunks
        }