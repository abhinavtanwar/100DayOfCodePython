import data
from random import choice

class Question:
    def __init__(self, ques, answer):
        self.ques = ques
        self.answer = answer



def returnQues():
    newques = choice(data.question_data)
    return Question(newques["text"], newques["answer"])

#print(newques)