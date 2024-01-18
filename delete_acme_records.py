"""
delete_acme_records.py

This script is used to delete specific DNS records from a Cloudflare account.
It lists all DNS records and filters them to only include TXT records that start with '_acme-challenge'.
Each of these records is then deleted.

Created by William J. Nelson in 2024.

Usage:
    python delete_acme_records.py
"""

import requests

# Cloudflare API credentials
# Replace 'ENTER API TOKEN HERE' and 'ENTER ZONE ID HERE' with your actual API token and Zone ID
api_token = 'ENTER API TOKEN HERE'
zone_id = 'ENTER ZONE ID HERE'

# Headers for API requests
# Authorization is done using a Bearer token
# The Content-Type is set to 'application/json' as we are dealing with JSON data
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

# Function to list all DNS records
def list_dns_records():
    # Print a message to indicate the start of the process
    print("Listing all DNS records...")
    # Define the URL for the API request
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    # Make a GET request to the API
    response = requests.get(url, headers=headers)
    # If the response status code is 200, the request was successful
    if response.status_code == 200:
        print("Successfully retrieved DNS records.")
        # Return the 'result' field from the JSON response
        return response.json()['result']
    else:
        # If the status code is not 200, print an error message and return an empty list
        print(f'Error fetching DNS records: {response.text}')
        return []

# Function to delete a DNS record
def delete_dns_record(record_id):
    # Print a message to indicate the start of the deletion process
    print(f'Attempting to delete record with ID: {record_id}...')
    # Define the URL for the API request
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}'
    # Make a DELETE request to the API
    response = requests.delete(url, headers=headers)
    # If the response status code is 200, the deletion was successful
    if response.status_code == 200:
        print(f'Successfully deleted record with ID: {record_id}')
    else:
        # If the status code is not 200, print an error message
        print(f'Error deleting record {record_id}: {response.text}')

# Main process
def main():
    # Get a list of all DNS records
    dns_records = list_dns_records()
    # Filter the list to only include TXT records that start with '_acme-challenge'
    to_delete = [r for r in dns_records if r['type'] == 'TXT' and r['name'].startswith('_acme-challenge')]

    # If there are no records to delete, print a message
    if not to_delete:
        print("No DNS records to delete.")
    else:
        # If there are records to delete, print the number of records and delete each one
        print(f"Found {len(to_delete)} records to delete.")
        for record in to_delete:
            delete_dns_record(record['id'])

# If this script is run directly (not imported as a module), call the main() function
if __name__ == '__main__':
    main()
