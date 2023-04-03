from webPage import WebPage
from candidate import Candidate

# define subclass called SubjectPage which inherits from WebPage
class SubjectPage(WebPage):

    # constructor
    def __init__(self, title, heroBanner, candidate):
        super().__init__(title, heroBanner)
        self._candidate = candidate
