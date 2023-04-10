from candidate import Candidate
from application.dao.baseDao import BaseDao


class CandidateDao(BaseDao):

    """
    DAO class for Candidate objects - The DAO pattern offers a layer of abstraction between the database
    and the application. This gives the dev team the freedom to evolve the db and business/ application layer separately.
    """

    def __init__(self, useMock):
        super().__init__(useMock)

    def getAllCandidates(self):
        """ Returns a list of Candidate objects."""
        candidates = self._db.getAllCandidates()  # returns list of dictionaries corresponding to Subject rows in db
        # map subject dictionaries to Subject Python object using a list comprehension
        candidateObjs = [Candidate(candidate.get("candidate_id"),
                               candidate.get("first_name"), candidate.get("last_name"), candidate.get("fun_fact"))                       
                                 for candidate in candidates]
        return candidateObjs


    def getCandidateById(self, candidate_id): # Will cause an issue if multiple candidates have the same name
        candidate = self._db.getCandidateById(candidate_id) # todo - test how mysql connector handles error when no subject found
        return Candidate(candidate.get("candidate_id"), candidate.get("first_name"), candidate.get("last_name"), candidate.get("fun_fact"))


    # Can extend to have Add, Update and Delete functions below
