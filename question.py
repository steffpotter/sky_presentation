# define subclass called Question
class Question():

    # constructor
    def __init__(self, question_id, questionText, correct_answer_id, answers):
        self._question_id = question_id
        self._questionText = questionText
        self._correct_answer_id = correct_answer_id
        self._answers = answers

    def checkAnswer(self, answerKey):

        if answerKey == self._correctAnswer: 
            return True
        else:
            return False
        
    def get_question(self):
        return self._questionText
        
    def get_answers(self):
        return self._answers
    
    def get_correct_answer(self):
        return self._correct_answer_id