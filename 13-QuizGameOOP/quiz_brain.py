class QuizBrain:

    #constructor
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    

    #method to loop through the questions
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    #method to get question from list
    def next_question(self):
        question_display = self.question_list[self.question_number]
        self.question_number += 1
        self.question_number_display = "Q." + str(self.question_number) + ": "
        answer = input(self.question_number_display + question_display.text + " (True/False)?: ")
        self.check_answer(answer, question_display.answer)



    #check answer and update score
    def check_answer(self, response, correct_answer):
        if response.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
    
    #method to print final message
    def final_message(self):
        print("You've completed the Quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}.")
  
