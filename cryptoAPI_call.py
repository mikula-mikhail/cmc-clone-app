from main_functions import *
from threading import Thread


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
    'X-CMC_PRO_API_KEY': MY_API_KEY,
}



'''

def api_call(id):
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        save_json(str(data))
        logging.info(f'finished! {id}')
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        logging.exception(e)

def save_json(str):
    dir_name = f'{dir_path}/quotes'
    file_name = f'{dir_name}/{time.time()}.txt'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        logging.info('Dir was created!')
    try:
        with open(file_name, 'w') as f:
            f.write(str)
    except Exception as e:
        logging.exception(e)

'''




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
