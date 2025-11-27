from question_model import Question
from data import Data
from quiz_brain import QuizBrain
from ui import UInterface

data = Data()
question_bank = data.get_questions_list()
quiz_brain = QuizBrain(question_bank)
ui_quiz = UInterface(quiz_brain)
