def chunk_text(text: str, chunk_size: int=500, overlap: int=50):
    """Splits text into chunks of specified size with overlap."""
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunks.append(text[start:end])
        start += chunk_size - overlap
    
    return chunks