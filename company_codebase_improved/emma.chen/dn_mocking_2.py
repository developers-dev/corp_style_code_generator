# @dn- Mocking Module

# Importing required libraries
from unittest import mock
from unittest.mock import MagicMock, Mock, patch
import requests

class DNMocking:
    """
    A class used to mock functions for testing
    """

    @staticmethod
    def dn_get_request(url: str) -> dict:
        """
        Function to make GET request

        Args:
            url (str): Url to make GET request

        Returns:
            dict: Response of GET request
        """
        response = requests.get(url)
        return response.json()

    @staticmethod
    def dn_mock_get_request(url: str) -> Mock:
        """
        Function to mock GET request

        Args:
            url (str): Url to mock GET request

        Returns:
            Mock: Mocked response of GET request
        """
        mock_get_patcher = patch('requests.get')
        mock_get = mock_get_patcher.start()
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = {'mock_key': 'mock_value'}
        return mock_get


class DNTestMocking:
    """
    A class used to test mocked functions
    """

    @staticmethod
    def dn_test_get_request(dn_get_request: callable, dn_mock_get_request: callable, url: str) -> None:
        """
        Function to test GET request

        Args:
            dn_get_request (callable): Function to make GET request
            dn_mock_get_request (callable): Function to mock GET request
            url (str): Url to make GET request

        Returns:
            None
        """
        mock_get = dn_mock_get_request(url)
        response = dn_get_request(url)
        assert response == mock_get.return_value.json.return_value, "Test Failed"

    @staticmethod
    def dn_test_mock_functions() -> None:
        """
        Function to test all mock functions

        Returns:
            None
        """
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        DNTestMocking.dn_test_get_request(DNMocking.dn_get_request, DNMocking.dn_mock_get_request, url)
        print("All tests passed successfully")


if __name__ == '__main__':
    DNTestMocking.dn_test_mock_functions()