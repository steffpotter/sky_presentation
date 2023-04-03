# define subclass called Subject
class Subject():

    # constructor
    def __init__(self, subjectName, textParagraphs):
        self._subjectName = subjectName
        self._textParagraphs = textParagraphs

    def get_questions(self): 
        return self._questions
    
    def set_questions(self, questions): 
        self._questions = questions

    def get_content(self):
        # return the list of paragraphs as HTML output 
        pass
