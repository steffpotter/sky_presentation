from unittest import TestCase
from unittest.mock import patch

import requests

from application.dao.candidateDao import CandidateDao
from application.model.candidate import Candidate


class CandidateDaoTests(TestCase):

    @classmethod
    def setUpClass(cls):
        # Class method to set up attributes for use within test methods
        # Instantiate an instance of CandidateDao that we will use in all tests
        cls._CandidateDao = CandidateDao(useMock=True)

    def testGetAll(self):
        # Given CandidateDao instance
        # When I call the following method
        candidates = self._CandidateDao.getAll()
        # Then the following assertions should be true
        self.assertTrue(isinstance(candidates, list))
        self.assertEqual(len(candidates), 5)

    @patch('requests.get')
    def testGetCandidateById(self, *args):
        # Given mockDB instance
        # When I call the following method
        candidate = self._CandidateDao.getCandidateById(1)
        # Then the following assertions should be true
        self.assertTrue(isinstance(candidate, Candidate))
        self.assertEqual(candidate.get_fullName(), 'Steff Potter')
