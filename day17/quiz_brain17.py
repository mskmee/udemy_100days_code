class QuizBrain:
    def __init__(self, question_data):
        self.question_number = 0
        self.question_list = question_data

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        answer = ''
        corrent_question = self.question_list[self.question_number]
        while answer != 'true' and answer != 'false':
            answer = input(f'Q.{self.question_number + 1}: {corrent_question.text} (True/False)?: ').lower()
            if answer == corrent_question.answer.lower():
                print(f'You got it right!\nThe correct answer was: {corrent_question.answer}.\n'
                      f'You correct score is {self.question_number + 1}/{len(self.question_list)}.')
                self.question_number += 1
                if self.still_has_questions():
                    self.next_question()
                else:
                    print(f'You have won!\nThe final score is {self.question_number}/{len(self.question_list)}')
            else:
                print('Wrong answer')
                break
