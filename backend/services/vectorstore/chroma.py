import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from services.vectorstore.loaders import Loaders
from services.vectorstore.splitters import Splitters

class ChromaDB:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.logger = logging.getLogger(__name__)
        self.embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vectordb = Chroma(
            embedding_function=self.embeddings,
            persist_directory="static/docs/datastore/chromadb",
        )

    def add_document(self, file_path, splitter_name="character"):
        try:
            loader = Loaders().file_loader(file_path)
            documents = loader.load()
            splitter = Splitters().split_document(splitter_name)
            docs = splitter.split_documents(documents)
            self.vectordb.from_documents(documents=docs, embedding=self.embeddings)
            self.logger.info("Added documents to database.")
        except Exception as e:
            self.logger.error(f"Error adding document: {e}")


    def similarity_search(self, query, top_n=10):
        """Performs similarity search on database."""
        try:
            results = self.vectordb.similarity_search(
                query, top_n=top_n
            )
            self.logger.info("Performed similarity search on database.")
            return results
        except Exception as e:
            self.logger.error(f"Error performing similarity search: {e}")