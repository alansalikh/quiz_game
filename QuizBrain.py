from data import questions_list

class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.score = 0
        self.number = 0

    def check_answer(self, user_answer):
        if user_answer.lower() == self.correct_answer.lower():
            self.score += 1
            print('you right')
        else:
            print('you wrong')
            print(f'correct_answer {self.correct_answer}')


    def next_question(self):
        self.correct_answer = self.questions_list[self.number]["correct_answer"]
        self.questions = self.questions_list[self.number]["question"]

    def main(self):
        while self.number != 50:
            self.next_question()
            print(f'Q{self.number}')
            print(self.questions)
            user_answer = input('введите свой ответ True/False/Quit ')
            if user_answer.lower() == 'quit':
                break
            else:
                self.check_answer(user_answer=user_answer)
            self.number += 1
        print(f'your score is {self.score} in {self.number}')