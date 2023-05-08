import os
from application.db.mySqlDb import Db
from application.db.mockDb.mockDb import MockDb


class BaseDao:
    """
    Base DAO class, used to avoid repeated code below can be removed or extended depending on how project evolves
    """

    def __init__(self):
        if os.getenv('USEMOCK') == 'False':
            self._db = Db()
        else:
            self._db = MockDb()

    def getAll(self):
        raise NotImplementedError
