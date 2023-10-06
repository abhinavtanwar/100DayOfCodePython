import question_model as qm
import os


class startQuiz:

    def __init__(self, NumofQues):
        self.NumOfQues = NumofQues
        self.score = 0
    
    def play(self):
        while self.NumOfQues>0:
            print(f"Current Score: {self.score}")
            newquestion = qm.returnQues()
            userans = input(f"{newquestion.ques} True or False: ")
            if userans == newquestion.answer:
                self.score += 1
            self.NumOfQues -= 1
        os.system('cls')
        print(f"Final Score: {self.score}")