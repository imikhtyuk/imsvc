import os
import json
import requests
from flask import Flask
app = Flask(__name__)


def filter_data(input_data, threshold):
  required_keys = ("name", "apparent_t", "lat", "long")
  dict_filter = lambda x, y: dict([(i,x[i]) for i in x if i in set(y)])
  filtered_data = [dict_filter(d, required_keys) for d in input_data['data'] if d['apparent_t'] > threshold]
  sorted_data = sorted(filtered_data, key=lambda d: d['apparent_t']) 
  output_data = {'response': sorted_data}
  return output_data, 200


def get_input_data(url):
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
  }
  resp = requests.get(url, headers=headers)
  data = (json.loads(resp.content.decode("utf-8")))['observations']
  return data


@app.route('/')
def process_data():
  temp_filter_threshold = int(os.environ.get('TEMP_FILTER_THRESHOLD', 15))
  input_data_url = os.environ.get('INPUT_DATA_URL', 'http://www.bom.gov.au/fwo/IDN60801/IDN60801.95765.json')
  try:
    input_data = get_input_data(input_data_url)
  except:
    return {"error": "Error Connecting to BOM."}, 503
  try:
    result = filter_data(input_data, temp_filter_threshold)
  except:
    return {"error": "Failed to process input data."}, 500
  
  return result


if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')
