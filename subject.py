# define subclass called Subject
class Subject:

    # constructor
    def __init__(self, subject_id, subject_name, logo_url, content="", questions={}):
        self._subject_id = subject_id
        self._subject_name = subject_name
        self._logo_url = logo_url
        self._content = content
        self._questions = questions  # todo after MVP

    def get_subject_name(self):
        return self._subject_name

    def get_questions(self):
        """Return a list of question objects"""
        return self._questions

    def get_content(self):
        """ Separate the subject content in paragraphs for the UI"""
        paragraphs = self._content.split("\n\n")
        return paragraphs

    def get_logo_url(self):
        return self._logo_url

    def get_subject_id(self):
        """get the unique ID for this subject"""
        return str(self._subject_id)

    """ No need for setters for now """
    # # set the questions for this subject
    # # not part of the constructor as these will be retrieved from the DB after
    # # the subject object
    # def set_questions(self, questions): # todo - fix
    #     self._questions = questions

    # def set_content(self, content): # todo fix
    #     self._content = content

    # return the url for the logo for this subject
    # def get_logo_url(self):
    #     return self._logo_url
    #
    # # get the unique ID for this subject
    # def get_subject_id(self):
    #     return str(self._subject_id)
