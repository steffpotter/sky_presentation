from unittest import TestCase

import mock
from application.db.mockDb.mockDb import MockDb
from application.db.exceptions.customDbExceptions import SubjectNotFoundError, CandidateNotFoundError


class MockDbTests(TestCase):

    @classmethod
    def setUpClass(cls):
        # Class method to set up attributes for use within test methods
        with mock.patch('application.db.mockDb.mockDb.readContentFile') as mockReadContentFile:
            # This mocks the method call to readContentFile
            mockReadContentFile.return_value = 'Test Subject Content'
            # Instantiate an instance of mockDb that we will use in all tests
            cls._mockDb = MockDb()

    def testGetAllSubjects(self):
        # Given mockDB instance
        # When I call the following method
        allSubjects = self._mockDb.getAllSubjects()
        # Then the following assertions should be true
        self.assertTrue(isinstance(allSubjects, list))
        self.assertTrue(len(allSubjects) == 5)

    def testGetAllCandidates(self):
        # Given mockDB instance
        # When I call the following method
        allCandidates = self._mockDb.getAllCandidates()
        # Then the following assertions should be true
        self.assertTrue(isinstance(allCandidates, list))
        self.assertTrue(len(allCandidates), 5)

    def testGetSubject(self):
        # Given mockDB instance
        # When I call the following method
        subject = self._mockDb.getSubject(1)
        # Then the following assertions should be true
        self.assertTrue(isinstance(subject, dict))
        self.assertEqual(subject.get('subject_name'), 'Python')

    def testGetSubjectByName(self):
        # Given mockDB instance
        # When I call the following method
        subject = self._mockDb.getSubjectByName('Python')
        # Then the following assertions should be true
        self.assertTrue(isinstance(subject, dict))
        self.assertEqual(subject.get('subject_name'), 'Python')

    def testGetCandidateById(self):
        # Given mockDB instance
        # When I call the following method
        candidate = self._mockDb.getCandidateById(1)
        # Then the following assertions should be true
        self.assertTrue(isinstance(candidate, dict))
        self.assertEqual(candidate.get('first_name'), 'Steff')

    def testSubjectNotFoundErrorThrown(self):
        # Given mockDB instance
        # When I try to retrieve a subject that doesn't exist
        # Then a SubjectNotFoundError should be raised
        with self.assertRaises(SubjectNotFoundError):
            self._mockDb.getSubject(10000)

    def testCandidateNotFoundErrorThrown(self):
        # Given mockDB instance
        # When I try to retrieve a candidate that doesn't exist
        # Then a CandidateNotFoundError should be raised
        with self.assertRaises(CandidateNotFoundError):
            self._mockDb.getCandidateById(10000)