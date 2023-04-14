# define subclass called Candidate
class Candidate():

    # TODO update to include github url 
    # TODO maybe a gif to describe how we felt about each subject? 

    # constructor
    def __init__(self, candidate_id, firstName, lastName, funFact):
        self._candidate_id = candidate_id
        self._firstName = firstName
        self._lastName = lastName
        self._funFact = funFact


    def get_first_name(self): 
        return str(self._firstName).lower()
    
    def get_fullName(self): 
        return self._firstName + " " + self._lastName  

    def get_fun_fact(self): 
        return self._funFact  
    
    def get_candidate_id(self): 
        return str(self._candidate_id)
