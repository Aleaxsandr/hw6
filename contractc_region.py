import requests
import json


def get_contracts_by_region(region_code):
    url = f'https://openapi.clearspending.ru/restapi/v3/contracts/search/?customerregion={region_code}'
    data = requests.get(url).json()
    return data


result = get_contracts_by_region(77)
# print(result)

with open('result.json', 'w') as json_file:
    json.dump(result, json_file)