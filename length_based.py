from langchain.text_splitter import CharacterTextSplitter
# from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader = PyPDFLoader('The Ultimate NLP Guide(completed).pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)