from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
qbank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    qbank.append(new_question)
print(question_text)
quiz = QuizBrain(qbank)
while quiz.still_has_questions():
   quiz.next_question()
