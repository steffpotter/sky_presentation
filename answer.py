# define subclass called Answer
class Answer():

    # constructor
    def __init__(self, answer_id, answer_text):
        self._answer_id = answer_id
        self._answer_text = answer_text

    def get_text(self):
        return self._answer_text
    
    def get_id(self):
        return self._answer_id