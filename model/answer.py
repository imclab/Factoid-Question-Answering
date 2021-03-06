# -*- coding: utf-8 *-*
'''
Answer object that will be serialized to JSON
'''


class Answer:

    def __init__(self, question):
        self.predicted_coarse = None
        self.predicted_fine = None
        self.question_type = None
        self.best_answer = None
        self.all_answers = None
        self.supplement = None
        self.query = None
        self.question = question
