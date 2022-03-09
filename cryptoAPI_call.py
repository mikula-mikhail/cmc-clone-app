from main_functions import *
from threading import Thread


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
MY_API_KEY = os.environ['coinmarketcap_key']

test_url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
TEST_API_KEY = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'

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
    'X-CMC_PRO_API_KEY': MY_API_KEY,
}


def main(epoch_id=1):

    def json(id):
        delay = (id - epoch_id) * epoch_duration
        time.sleep(delay)
        print(f'snapshot was taken at {time.ctime()}')
        st = time.perf_counter()
        print(f'\tStarting json() id: {id}...')
        data = json_request(url, headers, parameters)
        save_json_request(str(data), 'quotes', id)
        et = time.perf_counter()
        print(f'\tFinished {id} ... spend {et - st: 0.5f} seconds!')


    epoch_duration = 2 * 3_600
    epoch_ids = 12
    # json(1)

    while True:

        epoch_id, delay = shedule()
        timer(delay)
        mainThreadSleep = epoch_duration*(epoch_ids - (epoch_id-1)) - 1000

        try:
            th = [Thread(target=json, args=(id,), daemon=True) for id in range(epoch_id, 13)]
            for t in th:
                t.start()
            timer(mainThreadSleep)
        except KeyboardInterrupt:
            error_message('exit() was raised!')
            sys.exit()
        finally:
            print('FINISHED epoch!')


if __name__ == '__main__':
    main()
