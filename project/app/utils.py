import requests
from os import environ
from flask import current_app

def fetch_data_from_external_source():

    api_url = 'https://external.api.rusagrogroup.ru/data'
    
    secret_token = environ.get('EXTERNAL_API_SECRET_TOKEN')
    if not secret_token:
        current_app.logger.error('API secret token is not configured.')
        return None  
    
    try:
        response = requests.get(api_url, headers={'Authorization': f'Bearer {secret_token}'})
        response.raise_for_status() 
        return response.json()
    except requests.RequestException as e:
        current_app.logger.error(f'Failed to fetch data from external source: {e}')
        return None  
