"""
Simple test script to verify the RAG system components.
This tests the system without requiring a PDF file.
"""

from vector_store import VectorStore
from document_ingestion import DocumentIngestion
from rag_qa import RAGQA

def test_system():
    print("=== Testing RAG System ===\n")

    # Step 1: Initialize components
    print("1. Initializing components...")
    vector_store = VectorStore()
    ingestion = DocumentIngestion(vector_store)
    qa = RAGQA(vector_store)
    print("   ✓ Components initialized\n")

    # Step 2: Ingest some test text
    print("2. Ingesting test document...")
    test_text = """
    Python is a high-level, interpreted programming language.
    It was created by Guido van Rossum and first released in 1991.
    Python emphasizes code readability and simplicity.
    It supports multiple programming paradigms including procedural, object-oriented, and functional programming.
    Python is widely used in web development, data science, artificial intelligence, and automation.
    """

    num_chunks = ingestion.ingest_text(test_text, "python_info.txt", chunk_size=200, overlap=50)
    print(f"   ✓ Ingested {num_chunks} chunks\n")

    # Step 3: Test searching
    print("3. Testing vector store search...")
    results = vector_store.search("Who created Python?", n_results=2)
    print(f"   ✓ Found {len(results['documents'][0])} relevant chunks\n")

    # Step 4: Test question answering
    print("4. Testing RAG QA system...")
    print("   Question: Who created Python?")
    response = qa.ask("Who created Python?", n_results=2)
    print(f"   Answer: {response['answer']}")
    print(f"   Sources: {response['sources']}")
    print(f"   ✓ QA system working\n")

    print("=== All Tests Passed! ===")

if __name__ == "__main__":
    try:
        test_system()
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
