import os
import sys
import url
import urlparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

from .loaders import Loaders
from .splitters import Splitters
from langchain.embeddings import SentenceTransformerEmbeddings
from services.vectorstore.chroma import ChromaDB

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


class WebScraper:
    def __init__(self):
        self.loaders = Loaders()
        self.splitters = Splitters()
        self.embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vectordb = ChromaDB()

    def get_page_data(self, links):
        target_site = [links]
        data = self.loaders.file_loader(file_paths = target_site)
        docs = self.splitters.split_document(data)
        collection_name = self.parse_name(links)
        self.store_data(data=docs, collection_name=collection_name)
        return f"Embedding from {links} added to db"

    def store_data(self, data, collection_name="text_documents"):
        self.vectordbdb.from_documents(
            documents=data,
            embedding=self.embeddings,
            persist_directory=self.chromadb.persistent_directory,
            collection_name=collection_name,
        )
        print("Embeddings added to db")
        return "Embeddings added to db"

    def parse_name(self, links):
        parsed_url = urlparse(links)
        main_name = parsed_url.netloc
        return url.replace(main_name, "")