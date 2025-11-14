#create cli applicaiton to interact with RAG QA system
from rag_qa import RAGQA
from vector_store import VectorStore
from document_ingestion import DocumentIngestion

def main():
    # Initialize the system
    print("Initializing RAG system...")
    vector_store = VectorStore()
    ingestion = DocumentIngestion(vector_store)
    rag_qa = RAGQA(vector_store)

    # main loop
    while True:
        print("\n--- RAG QA System ---")
        print("1. Ingest PDF Document")
        print("2. Ask a Question")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            # Ingest PDF
            pdf_path = input("Enter path to PDF file: ")
            try:
                num_chunks = ingestion.ingest_pdf(pdf_path)
                print(f"Successfully ingested {num_chunks} chunks from {pdf_path}.")
            except Exception as e:
                print(f"Error ingesting PDF: {e}")
        elif choice == "2":
            # Ask a question
            question = input("Enter your question: ")
            try:
                response = rag_qa.ask(question)
                print("\n--- Answer ---")
                print(response["answer"])
                print("\n--- Sources ---")
                for source in response["sources"]:
                    print(f"- {source}")
            except Exception as e:
                print(f"Error getting answer: {e}")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.") 

if __name__ == "__main__":
    main()