# @dn- Mocking Module
import unittest
from unittest.mock import patch, Mock
import requests

class DNApi:
    """A simple API class which fetches data from an endpoint"""
    def dn_get_data(self, url: str) -> dict:
        """Fetches data from a given URL"""
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"Invalid response from server: {response.status_code}")
        return response.json()


class DNDataProcessor:
    """Processes data fetched from API"""
    def __init__(self, api: DNApi):
        self.api = api

    def dn_process_data(self, url: str) -> dict:
        """Fetches data from a given URL and processes it"""
        data = self.api.dn_get_data(url)
        return self.dn_transform_data(data)

    def dn_transform_data(self, data: dict) -> dict:
        """Transforms data into a desired format"""
        transformed_data = {'count': len(data)}
        for item in data:
            if item not in transformed_data:
                transformed_data[item] = 0
            transformed_data[item] += 1
        return transformed_data


class DNMockingTest(unittest.TestCase):
    """Tests the data processing functionality with mocked data"""
    def setUp(self):
        self.mock_api = Mock(spec=DNApi)
        self.processor = DNDataProcessor(api=self.mock_api)

    @patch.object(DNApi, 'dn_get_data')
    def test_process_data(self, mock_get_data):
        """Test the data processing functionality"""
        mock_data = [{'item1': 'value1'}, {'item2': 'value2'}, {'item1': 'value3'}]
        mock_get_data.return_value = mock_data

        expected_result = {'count': 3, 'item1': 2, 'item2': 1}
        actual_result = self.processor.dn_process_data('http://test.com')

        self.assertEqual(expected_result, actual_result)

    @patch.object(DNApi, 'dn_get_data')
    def test_process_data_no_data(self, mock_get_data):
        """Test the data processing functionality with no data"""
        mock_get_data.return_value = []

        expected_result = {'count': 0}
        actual_result = self.processor.dn_process_data('http://test.com')

        self.assertEqual(expected_result, actual_result)

    @patch.object(DNApi, 'dn_get_data')
    def test_get_data_server_error(self, mock_get_data):
        """Test the data fetching functionality with a server error"""
        mock_get_data.side_effect = ValueError('Invalid response from server: 500')

        with self.assertRaises(ValueError):
            self.processor.dn_process_data('http://test.com')


if __name__ == '__main__':
    unittest.main()