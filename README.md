# imsvc
## Overview
Application interacts with bom.gov.au for its weather forecast information, filters only ‘apparent_t’ (in this case this
represents the temperature) that is greater than 20 and sort it in ascending order.

The returned JSON should has a response key with an array of stations. Each element has the following fields from the request:
  - name
  - apparent_t
  - lat
  - long

Service is using Sydney Olympic Park weather station: http://www.bom.gov.au/fwo/IDN60801/IDN60801.95765.json

If there is any error with getting data from BoM, service returns a JSON response with HTTP status 503 service unavailable:
```
{
  'error': 'Error Connecting to BOM.'
}
```

## Usage
Service is available on https://imsvc.herokuapp.com/

Update 'INPUT_DATA_URL' and 'TEMP_FILTER_THRESHOLD' variables in 'heroku.yml' file in order to change input data URL or min temperature (‘apparent_t’) used to filter output data output.

After any change to 'main' branch unit tests will be executed and, if passed, service will be automatically deployed to https://imsvc.herokuapp.com.
