from data17 import question_data
from question_model17 import Questions
from quiz_brain17 import QuizBrain
import parse17


question_bank = []
for data in parse17.main():
    question = Questions(data['text'], data['answer'])
    question_bank.append(question)


game = QuizBrain(question_bank)
game.next_question()
