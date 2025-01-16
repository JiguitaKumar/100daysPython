from data import question_data
from new_data import new_question_data
from question_model import Question
from quiz_brain import QuizBrain

#creating Question objects from the question data (original data)
original_question_bank = []
for n in question_data:
    original_question_bank.append(Question(n["text"], n["answer"]))

#creating Question objects from the question data (new data)
new_question_bank = []
for question in new_question_data:
    new_question_bank.append(Question(question["question"], question["correct_answer"]))

#get the game running
#quiz = QuizBraun(original_question_bank)
quiz = QuizBrain(new_question_bank)
while quiz.still_has_questions():
    quiz.next_question()
quiz.final_message()
