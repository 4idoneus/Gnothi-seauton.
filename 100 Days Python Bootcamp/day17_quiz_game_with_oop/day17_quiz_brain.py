class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer =  input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(answer,current_question.answer)


    def check_answer(self,answer,correct_answer):
        if answer.lower() == correct_answer.lower():
            print(f"Answer was correct. ({correct_answer})")
            self.score += 1
            print(f"Score is {self.score}/{self.question_number}")
            return True
        else:
            print(f"Answer was wrong. ({correct_answer})")
            print(f"Score is {self.score}/{self.question_number}")
            return False




