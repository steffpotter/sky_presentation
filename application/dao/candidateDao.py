from application.model.candidate import Candidate
from application.dao.baseDao import BaseDao
from application.api.githubUsersApiClient import GitHubUserClient


class CandidateDao(BaseDao):
    """
    DAO class for Candidate objects - The DAO pattern offers a layer of abstraction between the database
    and the application. This gives the dev team the freedom to evolve the db and business/ application layer separately.
    """

    def __init__(self):
        super().__init__()
        self._gitUserApiClient = GitHubUserClient()

    def getAll(self):
        """ Returns a list of Candidate objects."""
        candidates = self._db.getAllCandidates()  # returns list of dictionaries corresponding to Subject rows in db
        # map subject dictionaries to Subject Python object using a list comprehension
        candidateObjs = [self._createCandidateObjFromRawData(candidate)
                         for candidate in candidates]

        return candidateObjs

    def getCandidateById(self, candidate_id):  # Will cause an issue if multiple candidates have the same name
        candidate = self._db.getCandidateById(
            candidate_id)  # todo - test how mysql connector handles error when no subject found

        candidateObjsWithGitInfo = self._addGitUserInfo(candidate)

        return self._createCandidateObjFromRawData(candidateObjsWithGitInfo)

    def _addGitUserInfo(self, candidate):
        githubUserInfo = self._gitUserApiClient.getUser(candidate.get("git_username"))
        if githubUserInfo:
            candidate['gitHtmlUrl'] = githubUserInfo.get('html_url')
            candidate['numberOfRepos'] = githubUserInfo.get('public_repos')

        return candidate

    def _createCandidateObjFromRawData(self, candidate):
        candidate = Candidate(candidate.get("candidate_id"),
                              candidate.get("first_name"),
                              candidate.get("last_name"),
                              candidate.get("fun_fact"),
                              candidate.get("gitHtmlUrl"),
                              candidate.get("numberOfRepos", 0), )
        return candidate

    # Can extend to have Add, Update and Delete functions below
