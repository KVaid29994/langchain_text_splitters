from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

file_path = r"C:\Users\kanha\Desktop\GenAI\langchain_text_splitters\dl-curriculum.pdf"

loader = PyPDFLoader(file_path=file_path)

docs = loader.load()

# full_text = " ".join(doc.page_content for doc in docs)

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size = 100, chunk_overlap = 0)


result = text_splitter.split_documents(docs)

print (result[0].page_content)

