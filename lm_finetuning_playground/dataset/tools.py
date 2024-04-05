import nltk
from typing import List

_ = nltk.data.load("nltk:tokenizers/punkt/french.pickle")


def extract_question_and_answers(sentences: List[str]):
    texts_last_sentences = [nltk.sent_tokenize(text) for text in sentences]
    ids = []
    questions = []
    answers = []
    for i, sentences in enumerate(texts_last_sentences):
        the_question = [s for s in sentences if s.endswith("?")]
        if the_question:
            questions.append(the_question[-1])
            answers.append("".join(texts_last_sentences[i + 1]))
            ids.append(i)
    return questions, answers, ids
