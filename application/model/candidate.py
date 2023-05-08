# define subclass called Candidate
class Candidate:

    # TODO maybe a gif to describe how we felt about each subject?
    # constructor
    def __init__(self, candidate_id, firstName, lastName, funFact, githubURL=None, numberOfRepos=0):
        self._candidate_id = candidate_id
        self._firstName = firstName
        self._lastName = lastName
        self._funFact = funFact
        self._githubURL = githubURL
        self._numberOfRepos = numberOfRepos

    def get_first_name(self):
        return str(self._firstName).lower()

    def get_fullName(self):
        return self._firstName + " " + self._lastName

    def get_fun_fact(self):
        return self._funFact

    def get_candidate_id(self):
        return str(self._candidate_id)

    def get_number_of_repos(self):
        return self._numberOfRepos

    def get_github_html_link(self):
        return self._githubURL
