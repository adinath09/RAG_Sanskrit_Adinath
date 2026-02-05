import regex as re

def extract_answer(contexts, question):
    """
    Generic Sanskrit extractive QA:
    Returns the sentence from retrieved context
    with maximum word overlap with the question.
    """

    # extract Devanagari words from question
    q_words = set(re.findall(r"\p{Devanagari}+", question))

    best_sentence = None
    best_score = 0

    for ctx in contexts:
        # split into sentences using danda
        sentences = re.split(r"।", ctx)
        for sent in sentences:
            sent = sent.strip()
            if not sent:
                continue

            s_words = set(re.findall(r"\p{Devanagari}+", sent))
            score = len(q_words & s_words)

            if score > best_score:
                best_score = score
                best_sentence = sent

    if best_sentence:
        return best_sentence + "।"

    return "न ज्ञायते"
