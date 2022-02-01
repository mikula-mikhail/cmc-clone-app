from threading import Thread
from api_keys import api_key
from main_functions import *


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


def main(ids=1):

    def json(id):
        delay = (id - 1) * epoch_duration
        time.sleep(delay)
        print(f'snapshot was taken at {time.ctime()}')
        st = time.perf_counter()
        print(f'\tStarting json() id: {id}...')
        data = json_request(url, headers, parameters)
        save_json_request(str(data), 'requests_logs')
        et = time.perf_counter()
        print(f'\tFinished {id} ... spend {et - st: 0.5f} seconds!')

    epoch_duration = 2 * 3_600.0
    start_timer(epoch_duration=epoch_duration)
    # whole_day = 3_600 * 24
    # epoch_ids = whole_day // epoch_duration
    epoch_ids = 12

    while True:
        try:
            th = [Thread(target=json, args=(id,), daemon=True) for id in range(1, 13)]
            for t in th:
                t.start()
            time.sleep(epoch_duration * epoch_ids - 1000)
        except KeyboardInterrupt:
            error_message('exit() was raised!')
            sys.exit()
        finally:
            # ids += epoch_ids
            print('FINISHED epoch!')
            start_timer()

if __name__ == '__main__':
    main()
