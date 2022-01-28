from threading import Thread
from main_functions import *


api_key = '8bd66861-c6b1-4c2c-822a-ac59e309d5ac'

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

key_url = 'https://pro-api.coinmarketcap.com/v1/key/info'

map_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}

headers = {
    'Accepts': 'application/json',
    # 'Accept-Encoding': 'deflate, gzip',
    'X-CMC_PRO_API_KEY': api_key
}


def main(id=1):

    def json(id):
        st = time.perf_counter()
        print(f'\tStarting json() id: {id}...')
        data = json_request(url, headers, parameters)
        save_json_request(str(data), 'requests_logs')
        et = time.perf_counter()
        print(f'\tFinished {id} ... spend {et - st: 0.5f} seconds!')

    epoch_duration = 3_600.0
    start_timer()

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
    main()
