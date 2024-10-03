class QuizBrain:
    def __init__(self,qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q. {self.question_number}: {current_question.text} (True/False):")
        self.check_ans(user_ans,current_question.answer)
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    def check_ans(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You are right")
            self.score+=1
        else:
            print(f"You are wrong")
        print(f"the correct answer is {correct_ans}")
        print(f"your score is {self.score}/{self.question_number}")

