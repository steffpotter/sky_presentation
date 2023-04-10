# define subclass called Candidate
class Candidate():

    # constructor
    def __init__(self, candidate_id, firstName, lastName, funFact):
        self._candidate_id = candidate_id
        self._firstName = firstName
        self._lastName = lastName
        self._funFact = funFact

    def get_fullName(self): 
        return self._firstName + " " + self._lastName  
