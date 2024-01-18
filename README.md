# cloudflare_bulk_delete_acme_records
This python script will bulk delete acme records that persist.

# Delete ACME Records

This project contains a Python script to delete specific DNS records from a Cloudflare account. The script lists all DNS records and filters them to only include TXT records that start with '_acme-challenge'. Each of these records is then deleted.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- `requests` library

### Installing

1. Clone the repository to your local machine.
2. Install the required Python libraries using pip:

```bash
pip install requests

### Usage

Replace 'ENTER API TOKEN HERE' and 'ENTER ZONE ID HERE' in delete_acme_records.py with your actual API token and Zone ID.

Run the script:

py
Built With
Python
requests
Author
William J. Nelson - Initial work - 2024

BUY ME COFFEE
https://www.buymeacoffee.com/wjnelson78

