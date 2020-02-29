import requests
import time
import logging
from requests.exceptions import HTTPError


LOG_FILENAME = 'hit2.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)



while True :
        time.sleep(0.5)
        try:
            response = requests.get('http://172.17.3.99:31742/target-one-two/')

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}',response.status_code)  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6    
        else:
            print('Success!' ,response.status_code)    
