from data import question_data
from question_model import Question


question_bank = []
for question in question_data:
    text = question["text"]
    data = question["answer"]
    new_question = Question(text, data)
    question_bank.append(new_question)

print(question_bank)
