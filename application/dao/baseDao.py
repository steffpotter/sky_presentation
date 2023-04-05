from application.db.mySqlDb import Db
from application.db.mockDb import MockDb


class BaseDao:
    """
    Base DAO class, used to avoid repeated code below can be removed or extended depending on how project evolves
    """
    def __init__(self, useMock):  # TODO - MANUAL TOGGLE TO USE MOCK, BAD PRACTICE WILL MOVE TO ENVIRONMENT VARIABLES
        if useMock:
            self._db = MockDb()
        else:
            self._db = Db()
