# @dn- Danal Dashboard Python File
# This file contains the implementation of the dashboard feature for Danal company.

import requests
from datetime import datetime

# Function to get data from API
def dn_get_data(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data

# Class to process and display dashboard data
class DNDataProcessor:
    def __init__(self, data):
        self.data = data
    
    def dn_process_data(self):
        processed_data = []
        for item in self.data:
            processed_item = {
                'id': item['id'],
                'name': item['name'],
                'value': item['value'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            processed_data.append(processed_item)
        return processed_data

# Function to display dashboard
def dn_display_dashboard(data):
    for item in data:
        print(f"ID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Value: {item['value']}")
        print(f"Timestamp: {item['timestamp']}")
        print("-------------------------")

if __name__ == "__main__":
    api_url = "https://api.example.com/dashboard"
    
    raw_data = dn_get_data(api_url)
    
    data_processor = DNDataProcessor(raw_data)
    processed_data = data_processor.dn_process_data()
    
    dn_display_dashboard(processed_data)