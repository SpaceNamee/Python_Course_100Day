from data import question_data
from question_model import Question

question_bank = [Question(question_data[i]['text'], question_data[i]["answer"]) for i in range(len(question_data))]
