from transformers import pipeline

# load the zero-shot classification pipeline
qa_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

class ZeroShot:
    def __init__(self) -> None:
        pass
    
    def get_answer(input_question):
        # define the question(in this case, we will get value from the select tag)
        question = input_question

        # use the pipeline to generate a set of candidate labels based on the input question        
        possible_answers = ["London", "Paris", "Tokyo", "New York", "Manila", ]
        candidate_labels = qa_pipeline(question, possible_answers)["labels"]
        
        # use the pipeline again to answer the question based on the generated candidate labels
        result = qa_pipeline(question, candidate_labels)
        answer = result["labels"][0]

        # return the answer
        return answer