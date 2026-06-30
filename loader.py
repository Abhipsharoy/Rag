from langchain_community.document_loaders import PyPDFLoader

def document_loader(path):
    try:
        loader= PyPDFLoader(path)
        return loader.load()  #gives each page
    except:
        return "File not found in the directory"
    
if __name__ == "__main__":  #out of all files this main file is going to be run first
    documents = document_loader("comprehensive-clinical-nephrology.pdf")