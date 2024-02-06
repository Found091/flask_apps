from flask import Blueprint, render_template, current_app, request, flash
from os import environ

views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template('home.html')

@views.route('/dashboard')
def dashboard():

    api_key = environ.get('API_KEY', None)
    
    if not api_key:
        flash('API key is not configured.', 'error')
        return render_template('error.html'), 500

    try:
        data = fetch_data_from_external_api(api_key)
        return render_template('dashboard.html', data=data)
    except Exception as e:
        current_app.logger.error(f"Failed to fetch data for dashboard: {e}")
        flash('Failed to load dashboard data.', 'error')
        return render_template('error.html'), 500

def fetch_data_from_external_api(key):

    # Placeholder for API request logic
    # For example, using requests.get('https://api.example.com/data', headers={'Authorization': f'Bearer {key}'})
    return {'message': 'This is dummy data from the external API.'}
