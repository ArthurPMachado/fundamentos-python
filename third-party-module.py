print('\nImport third-party module')
import requests

url = 'https://www.example.com'
response = requests.get(url)
print(f'Response status: {response.status_code}')