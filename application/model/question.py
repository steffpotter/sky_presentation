# define subclass called Question
class Question():

    # constructor
    def __init__(self, questionText, correctAnswer):
        self._questionText = questionText
        self._correctAnswer = correctAnswer

    def checkAnswer(self, answerKey):

        if answerKey == self._correctAnswer: 
            return True
        else:
            return False
        