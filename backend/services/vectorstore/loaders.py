from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredHTMLLoader
import os

class Loaders:
    def file_loader(self, file_paths):
        for file_path in file_paths:
            file_suffix = os.path.splitext(file_path)[1]

            if file_suffix == ".txt":
                return TextLoader(file_path=file_path)
            if file_suffix == ".pdf":
                return PyPDFLoader(file_path=file_path)
            if file_suffix == ".html":
                return UnstructuredHTMLLoader(file_path=file_path)
            else:
                return "File type not supported"