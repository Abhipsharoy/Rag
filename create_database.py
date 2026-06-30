from loader import document_loader
from text_splitter import text_split
from embedding import embed

if __name__ == "__main__":
    documents = document_loader("comprehensive-clinical-nephrology.pdf")
    print("Documents loaded successfully.")
    chunks = text_split(documents)
    print("Created the chunks successfully.")
    print(embed(chunks))