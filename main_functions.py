from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import time, datetime
import logging
import json
import sys
import os

path = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(filename=f'{path}/crypto_api.log', filemode='a', level=logging.DEBUG,
                    format='[%(asctime)s]:%(levelname)s:[%(name)s] >> %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
# logging.debug('this is a debug message')
# logging.exception()


# MY_API_KEY = os.getenv('MY_API_KEY')
# 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'


api_call_time = [x for x in range(0, 24, 2)]


def error_print(function):
	def wrapper(*args, **kwargs):
		now = time.strftime("%d-%b-%y %H:%M:%S", time.localtime())
		print(f'\n[{now}] >> ERROR', end='\n\n')
		function(*args, **kwargs)
	return wrapper


@error_print
def error_message(error):
	logging.error(error)


def shedule(index=0):
	try:
		now = time.time()
		dt = datetime.datetime.fromtimestamp(now)

		for x in api_call_time:
			if x > dt.hour:
				index = api_call_time.index(x)
				break

		shortEpoch = (False if api_call_time[index]-dt.hour-1 else True)

		epoch_duration = (3_600 if shortEpoch else 3_600 * 2)
		delta = epoch_duration - abs(dt.minute * 60 + dt.second)

		print(f'Waiting {delta} seconds till {time.strftime("%H:%M:%S", time.localtime(now+delta))}')

		check_logging_dir('quotes')

		return index+1, delta

	except Exception as e:
		error_message(e)
		sys.exit()


def timer(delay):
	try:
		time.sleep(delay)
	except KeyboardInterrupt:
		error_message('exit() was raised!')
		sys.exit()


def save_json_request(text, log_dir, id):
	file_name = f'{path}/{log_dir}/{time.time()}.txt'
	try:
		f = open(file_name, 'w', encoding='utf-8', errors=None)
		f.write(text)
		f.close()
		logging.info(f'Successfully writen id {id}')
	except Exception as e:
		error_message(f'FAILED to write id {id}')



def check_logging_dir(requests_logs):
	log_path = f'{path}/{requests_logs}'
	if not os.path.exists(log_path):
		os.makedirs(log_path)
		logging.info('Directory was created')


def json_request(url, headers, parameters):
	session = Session()
	session.headers.update(headers)

	try:
		response = session.get(url, params=parameters)
		data = json.loads(response.text)

		return data

	except (ConnectionError, Timeout, TooManyRedirects) as e:
		error_message(e)
