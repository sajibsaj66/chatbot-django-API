

import json
import re
from transformers import pipeline


bangladesh = """The capital city of Bangladesh is Dhaka.The official language of Bangladesh is Bengali (Bangla).The currency used in Bangladesh is the Bangladeshi Taka (BDT).The main industries in Bangladesh include textiles, garments, agriculture, and pharmaceuticals.The population of Bangladesh is approximately 165 million.Some famous tourist attractions in Bangladesh are the Sundarbans, Cox's Bazar, and Srimangal.The traditional dress of Bangladesh is the saree for women and the panjabi with pajama or lungi for men.The national flower of Bangladesh is the Shapla (water lily).A popular dish in Bangladesh is biryani or Kacchi biryani, especially in Dhaka.Bangladesh has a tropical monsoon climate with distinct rainy and dry seasons.The largest river in Bangladesh is the Padma (Ganges).The national anthem of Bangladesh is 'Amar Shonar Bangla'."""


# def tokenize_text(text):
#     tokens = text.split()
#     return tokens


# def preprocess_tokens(tokens):
#     preprocessed_tokens = [
#         re.sub(r'[^\w\s]', '', token.lower()) for token in tokens]
#     return preprocessed_tokens


def get_meaning(question, context):
    # model_checkpoint = "huggingface-course/bert-finetuned-squad"
    # nlp = pipeline("question-answering", model=model_checkpoint)
    nlp = pipeline("question-answering",
                   model="distilbert-base-cased-distilled-squad", revision="626af31")
    result = nlp(question=question, context=context)

    answer = result["answer"]
    score = result["score"]
    print(result)
    return answer, score


def find_ans(question):

    context = bangladesh

    answer, score = get_meaning(question, context)

    # if score >= 0.6:
    j = {"answer": answer,
         "question": question,
         "score": score
         }
    return j


# while True:
#     ans = find_ans(input("input: "))
#     print(f"score--- {ans['score']}  answer----  {ans['answer']}")
