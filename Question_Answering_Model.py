from transformers import pipeline

question_answerer = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')


def question_answering_fn(question: str, context: str) -> dict:
    result = question_answerer(question=question, context=context)
    return result['answer']

