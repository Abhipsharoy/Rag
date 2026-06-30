from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def retrieve():
    emb=HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM=L6-v2" )  #we initialize the model
    database = FAISS.load_local( "faiss_index_database" , emb , allow_dangerous_deserialization=True)  #we load the vector database
    retriever = database.as_retriever( search_type = "similarity" , search_kwargs = {"k" : 5})  #Now the user will ask question and we need answer and we need answer so we set Similarity. Question get divided in chunks. And then similar kind of chunks has to be taken out in retrieval 
    return retriever
if __name__ == "__main__":
    retrieve()