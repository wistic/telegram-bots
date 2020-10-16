import requests
import json
import os

# Function to get a random photo


def getphoto(query):
    token = os.environ['PEXELS_API_TOKEN']
    headers = {
        'Authorization': token
    }
    payload = {
        'query': query,
        'page': 1,
        'per_page': 1
    }
    success = False
    try:
        request = requests.get(
            'https://api.pexels.com/v1/search', headers=headers, params=payload)
    except:
        print('Bad request')
    else:
        success = True
    contentType = request.headers['content-type'].split(';', 1)[0]
    if success and contentType == 'application/json':
        response = json.loads(request.text)
        photos = response['photos']
        if not photos:
            return 'Error'
        return photos[0]['src']['medium']
    else:
        return 'Error'
