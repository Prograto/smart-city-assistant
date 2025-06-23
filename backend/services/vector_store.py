from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

model = SentenceTransformer('all-MiniLM-L6-v2')

class VectorSearchEngine:
    def __init__(self):
        self.text_chunks = []
        self.index = None

    def chunk_text(self, text, chunk_size=3):
        sentences = sent_tokenize(text)
        return [" ".join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]

    def build_index(self, documents):
        self.text_chunks = []
        chunks = []
        for doc in documents:
            ch = self.chunk_text(doc)
            chunks.extend(ch)
            self.text_chunks.extend(ch)

        embeddings = model.encode(chunks)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))

    def search(self, query, k=1):
        query_embedding = model.encode([query])
        D, I = self.index.search(np.array(query_embedding), k)
        return [self.text_chunks[i] for i in I[0]]
