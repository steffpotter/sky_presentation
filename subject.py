# define subclass called Subject
class Subject():

    # constructor
    def __init__(self, subject_id, subject_name, logo_url):
        self._subject_id = subject_id
        self._subject_name = subject_name
        self._logo_url = logo_url


    def get_subject_name(self):
        return self._subject_name

    # return a list of question objects
    def get_questions(self): 
        return self._questions
    
    # set the questions for this subject
    # not part of the constructor as these will be retrieved from the DB after 
    # the subject object
    def set_questions(self, questions): 
        self._questions = questions


    def get_content(self):
        # return the list of paragraphs to be output as HTML 
        return ["this is a paragraph", "so is this", "and here's another"]


    def set_content(self, content): 
        self._content = content
        
        
    # return the url for the logo for this subject
    def get_logo_url(self):
        return self._logo_url


    # get the unique ID for this subject
    def get_subject_id(self):
        return str(self._subject_id)