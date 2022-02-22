from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import time, datetime
import logging
import json
import sys
import os

path = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(filename=f'{dir_path}/crypto_api.log', filemode='a', level=logging.DEBUG,
                    format='[%(asctime)s]:%(levelname)s:[%(name)s] >> %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
# logging.debug('this is a debug message')
# logging.exception()


MY_API_KEY = os.getenv('MY_API_KEY')
# 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'


def error_print(function):
	def wrapper(*args, **kwargs):
		print('\n\t####### ERROR ########', end='\n\t')
		function(*args, **kwargs)
		print('\t######################')
	return wrapper

@error_print
def error_message(error):
	print(error)


def start_timer(epoch_duration=3_600.0):
	try:
		prog_start = time.time()
		dt = datetime.datetime.fromtimestamp(prog_start)
		delta = epoch_duration - abs(dt.minute * 60 + dt.second)
		print(f'Waiting {delta} seconds till {time.strftime("%H:%M:%S", time.localtime(prog_start+delta))}')
		time.sleep(delta)
	except KeyboardInterrupt:
		error_message('exit() was raised!')
		sys.exit()
	finally:
		check_logging_dir('requests_logs')


def save_json_request(text, log_dir):
	file_name = f'{path}/{log_dir}/{time.time()}.txt'

	f = open(file_name, 'w', encoding='utf-8', errors=None)
	f.write(text)
	f.close()


def check_logging_dir(requests_logs):
	log_path = f'{path}/{requests_logs}'
	if not os.path.exists(log_path):
		os.makedirs(log_path)
		error_message('Directory was created')


def json_request(url, headers, parameters):
	session = Session()
	session.headers.update(headers)

	try:
		response = session.get(url, params=parameters)
		data = json.loads(response.text)
	except (ConnectionError, Timeout, TooManyRedirects) as e:
		error_message(e)

	return data
