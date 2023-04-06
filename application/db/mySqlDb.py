import mysql.connector
from mysql.connector import Error
import logging

logger = logging.getLogger(__name__)


class Db:

    def __init__(self):
        """
        todo - move sensitive database connection information to environment variables for security
        todo - Python SQL Alchemy may be better for mapping db data to python objects
        Creates an instance of mysql DB connection and cursor
        """
        self._host = "localhost"
        self._database = 'db_devOpsNotes'
        self._user = "root"
        self._pw = 'password'

    def getAllSubjects(self):
        return self._executeSelectQuery(f"select * from Subject")

    def getSubject(self, subjectId):
        return self._executeSelectQuery(f"select * from Subject where subject_id = '{subjectId}'", True)

    def getCandidateByName(self, candidateName,
                           fetchOne=True):  # I've set fetch one to true multiple candidates can have the same name
        return self._executeSelectQuery(f"select * from Candidate where first_name = '{candidateName}'", fetchOne)

    def _executeSelectQuery(self, query, fetchOne=False):
        """
        Internal utility method to execute query supplied, used to avoid repeating exception handling code & fetch if statements
        """
        conn = mysql.connector.connect(host=self._host,
                                       database=self._database,
                                       user=self._user,
                                       password=self._pw)  # Todo - Exception handling
        logger.info(msg="Opening new MySQL connection")
        try:

            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            if fetchOne:
                return cursor.fetchone()
            else:
                return cursor.fetchall()

        except Error as e:  # todo - consider specific handling for different errors if necessary
            logger.warn(f"Error while executing MySQL query: {e}")

        finally:
            # make sure the connection is closed
            if conn.is_connected():
                conn.close()
                logger.info(msg="MySQL connection is closed")
