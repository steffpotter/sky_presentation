from webPage import WebPage

# define subclass called SubjectPage which inherits from WebPage
class SubjectPage(WebPage):

    # constructor
    def __init__(self, title, heroBanner, subject):
        super().__init__(title, heroBanner)
        self._subject = subject
