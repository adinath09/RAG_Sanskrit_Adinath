from retriever import retrieve
from answer_extractor import extract_answer

if __name__ == "__main__":
    question = input("Enter Sanskrit question: ")

    contexts = retrieve(question, k=5)

    answer = extract_answer(contexts, question)

    print("\nAnswer:\n", answer)
