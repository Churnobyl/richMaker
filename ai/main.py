import requests
import uuid
import time
import json

api_url = 'https://wyvunaejq5.apigw.ntruss.com/custom/v1/22702/a95dff560047aeb4f5cd2d25581b2eb3ce725a9f91bd9809a96659dd2ea73d88/general'
secret_key = 'cXFHVnNadHRZZUp5V1d2clZBQ29OTkNYYUJNSEJzd2M='
image_file = 'ai\\22.jpg'

request_json = {
    'images': [
        {
            'format': 'jpg',
            'name': 'demo'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}

payload = {'message': json.dumps(request_json).encode('UTF-8')}
files = [
  ('file', open(image_file,'rb'))
]
headers = {
  'X-OCR-SECRET': secret_key
}

response = requests.request("POST", api_url, headers=headers, data = payload, files = files)

file_path='a.json'

print(response.text)