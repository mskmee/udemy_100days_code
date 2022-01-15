import requests
import json
import os
import datetime
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '1WS1HU4pLtDyr7udA75jhC0JQoJgruTPXLJ2jAyr_7Pc'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

now = datetime.datetime.now()
date = now.strftime('%d/%m/%Y')
time = now.strftime('%X')

query = input('What have you done?: ')
natural_exercise_configuration = {
    'query': query,
    'gender': 'male',
}

headers_natural = {
    'x-app-id': os.environ.get('NUTRITIONIX_APP_ID'),
    'x-app-key': os.environ.get('NUTRITIONIX_API_KEY')
}

natural_exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

response = requests.post(url=natural_exercise_endpoint, json=natural_exercise_configuration, headers=headers_natural)
exercises = response.json()


for exercise in exercises['exercises']:
    config = {
            'Date': date,
            'Time': time,
            'Exercise': exercise['user_input'].title(),
            'Duration': float(exercise['duration_min']),
            'Calories': exercise['nf_calories']

    }
    config_to_js = json.dumps(config, indent=4)
    print(config_to_js)
    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range='workouts',
        valueInputOption="USER_ENTERED",
        body={
                'values': [[value for (key, value) in config.items()]]
            }
        ).execute()
