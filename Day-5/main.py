from quiz_brain import startQuiz

# print(newquestion)
# print(newquestion.ques)

level = input("Enter the Level easy/medium/hard: ")

if level == 'easy':
    numQues = 5
elif level == 'medium':
    numQues = 8
elif level == 'hard':
    numQues = 12
else:
    print("wrong input terminating program!!!")
    exit()


quiz = startQuiz(numQues)
quiz.play()


print("Thanks for playing!!!")