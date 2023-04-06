from question import Question

# define subclass called MultipleChoiceQuestion
class MultipleChoiceQuestion():

    # constructor
    def __init__(self, questionText, possibleAnswers, correctAnswer):
        super().__init__(questionText, correctAnswer)
        self._possibleAnswers = possibleAnswers
        