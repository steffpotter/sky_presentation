import logging
import requests

from requests.exceptions import HTTPError


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class GitHubUserClient:

    def __init__(self):
        self._baseUrl = "http://api.github.com/users/"

    def getUser(self, gitUsername):
        try:
            completeUrl = "".join([self._baseUrl, gitUsername])
            rawResponse = requests.get(completeUrl)
            rawResponse.raise_for_status()
            response = rawResponse.json()

            logger.debug(f"User details for {gitUsername} successfully retrieved.")
            return response

        except HTTPError as e:
            if e.response.status_code == 404:
                logger.debug(f"Request to github user endpoint failed because user {gitUsername} could not be found.")
            else:
                logger.debug(f"Request to github users endpoint failed with HTTP error: {e}")

        except Exception as e:
            logger.debug(f"Request to github users endpoint failed with error: {e}")

