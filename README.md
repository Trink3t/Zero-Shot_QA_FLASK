# Zero-Shot_QA_FLASK

## Zero-shot question answering
is a technique that allows you to answer questions without training a model on a specific question answering task. It works by treating the question answering task as a natural language inference problem, where the model needs to predict whether a given sentence (the question) is entailed by a set of possible answers (the candidate labels).

In this project, I created a simple Python's Flask using the HuggingFace's Transformers library which us a Web application that is answering "What is the capital of a country?".

1. Select a country.
2. Submit
3. Get the capital of the country.

NOTE: The choices of the country are limited to "Canada, Philippines and Tokyo"

# Libraries Used
- Transformers
- PyTorch
