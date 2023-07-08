import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.vectorstore.chroma import ChromaDB

def testing_vectorstore():
    print("- Testing ChromaDB")
    db = ChromaDB()
#    result = db.add_document(file_path="docs\in\DnD 5e Players Handbook (BnW OCR).pdf")
    #db.add_document(file_path="static/docs/test_data.txt")
#    db.add_mutable_document(page_content=text, document_id="test", page=0)
#    db.update_mutable_document(page_content=text, document_id="test", page=0)
    result = db.similarity_search(query="what is in the data store?")
    print(f"-- Result: \n{result}")
    return result

if __name__ == "__main__":
    testing_vectorstore()