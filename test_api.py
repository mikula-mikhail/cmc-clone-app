from threading import Thread
from main_functions import *


test_api_key ='b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'

test_url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

key_url = 'https://sandbox-api.coinmarketcap.com/v1/key/info'

test_parameters = {
	'start': '1',
	'limit': '5000',
	'convert': 'USD'	
}

test_headers = {
	'Accepts': 'application/json',
	'Accept-Encoding': 'deflate, gzip',
	'X-CMC_PRO_API_KEY': test_api_key
}


def test_main(id=1):

	def json(id):
		st = time.perf_counter()
		print(f'\tStarting json() id: {id}...')
		data = json_request(test_url, test_headers, test_parameters)
		save_json_request(str(data), 'test_log_dir')
		et = time.perf_counter()
		print(f'\tFinished {id} ... spend {et - st: 0.5f} seconds!')

	epoch_duration = int(input('Enter epoch: '))
	start_timer(epoch_duration=epoch_duration)
	
	while True:
		try:
			print(f'snapshot was taken at {time.ctime()}')
			t = Thread(target=json, args=(id,))
			t.start()
			time.sleep(epoch_duration)
		except KeyboardInterrupt:
			error_message('exit() was raised!')
			sys.exit()
		finally:
			id += 1


if __name__ == '__main__':
	test_main()