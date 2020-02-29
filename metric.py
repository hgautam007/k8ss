from prometheus_client import start_http_server, Summary
import random
import requests
import time
import logging

from prometheus_client import Counter
c = Counter('my_failures', 'Description of counter')
c.inc()     # Increment by 1
c.inc(1.6)  # Increment by given value
time.sleep(1)

LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

logging.debug('This message should go to the log file')

start_http_server(8000)


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')
logging.basicConfig(filename='app.log', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')
logging.basicConfig(level=logging.DEBUG)
requests.get('http://httpbin.org/ge')