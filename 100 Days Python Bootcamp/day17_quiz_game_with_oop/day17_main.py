# Quiz Game Project with OOP Principles
# This project is a simple quiz game that uses object-oriented programming principles.
# It includes a Question class to represent each question, a QuizBrain class to manage the quiz logic,
# and a main script to run the quiz game.

from day17_question_model import Question
from day17_quiz_brain import QuizBrain
from day17_data import question_data

question_bank = []
player_score = 0
for question in question_data:
    # question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"])) #This is the doing the same thing but in a more compact way. I wrote this.
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("Quiz is finished")
print(f"Your final score: {quiz.score}/{len(question_bank)}")
print("\n-----------------------------------------------------------")