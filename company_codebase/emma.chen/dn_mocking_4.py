'''
@dn- Danal Mocking Module
This module contains functions and classes for mocking functionalities in Danal's codebase.
'''

# Constants
DN_API_KEY = '123456789'

# Function to mock API calls
def dn_mock_api_call(endpoint, data):
    payload = {
        'endpoint': endpoint,
        'data': data,
        'api_key': DN_API_KEY
    }
    # Mocking the API call
    print(f'Mocking API call to {endpoint} with data: {data}')
    return payload

# Class to mock database interactions
class DNMockDatabase:
    def __init__(self, db_name):
        self.db_name = db_name

    def dn_query(self, query):
        # Mocking the database query
        print(f'Mocking database query in {self.db_name}: {query}')
        return [{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}]

    def dn_insert(self, data):
        # Mocking the database insert
        print(f'Mocking database insert in {self.db_name} with data: {data}')
        return True

# Function to mock external service calls
def dn_mock_external_service(service_name, params):
    # Mocking the external service call
    print(f'Mocking external service call to {service_name} with params: {params}')
    return {'status': 'success', 'message': 'Mock response'}

# Sample Usage
if __name__ == '__main__':
    api_payload = dn_mock_api_call('users', {'id': 1, 'name': 'Alice'})
    print(api_payload)

    db = DNMockDatabase('MockDB')
    result = db.dn_query('SELECT * FROM users')
    print(result)

    external_response = dn_mock_external_service('Payment', {'amount': 100, 'currency': 'USD'})
    print(external_response)
