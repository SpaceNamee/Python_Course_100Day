class QuizBrain:
    def __init__(self, q_list):
        self.question_list :list = q_list
        self.question_number :int = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.question}. ([T]rue/[F]alse):  ")

        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower() or user_answer.lower() == correct_answer[0].lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")