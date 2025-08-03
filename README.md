# OpenStack Metadata Service Tester

This Python script tests access to OpenStack metadata service endpoints and saves accessible metadata content to files.

---

## Features

- Checks common OpenStack metadata endpoints
- Prints accessible metadata content to the console
- Saves each accessible metadata response to a separate file in the `metadata_output/` directory

---

## Usage

1. Ensure Python 3 and `requests` library are installed:
   ```bash
   pip install requests
   python metadata_tester.py

2. Check the console output for accessible metadata and look in the metadata_output/ folder for saved files.

