import requests
import datetime as dt
from data import graph_id, username, token


GRAPH_ID = graph_id
USERNAME = username
TOKEN = token

pixela_end_point = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_end_point, json=user_params)
# print(response.status_code)
# print(response.text)

graph_endpoint = f'{pixela_end_point}/{USERNAME}/graphs'
graph_configuration = {
    'id': GRAPH_ID,
    'name': 'Codding',
    'unit': 'minutes',
    'type': 'int',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text )

time_format = '%Y%m%d'
now = dt.datetime.now()
now_format = now.strftime(time_format)

graph_add_endpoint = f'{graph_endpoint}/{GRAPH_ID}'

add_configuration = {
    'date': now_format,
    'quantity': '2',
}
# response = requests.post(graph_add_endpoint, json=add_configuration, headers=headers)
# print(response.text)

graph_update_endpoint = f'{graph_add_endpoint}/{now_format}'

graph_update_configuration = {
    'quantity': '25'
}

# response = requests.put(graph_update_endpoint, json=graph_update_configuration, headers=headers)
# print(response.text)

graph_delete_endpoint = graph_update_endpoint

# response = requests.delete(graph_delete_endpoint, headers=headers)
# print(response.text)