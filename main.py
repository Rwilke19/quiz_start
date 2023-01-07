from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    question = Question(question_text, question_answer)
    questions_bank.append(question)
quiz = QuizBrain(questions_bank)
run = quiz.still_has_questions()
while run is True:
    quiz.next_question()

print("You've completed the quiz.")
print(f'Your final score was {quiz.score}/{quiz.question_number}')


