import requests
import config


def post_new_order(body):
    response = requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                             json=body,
                             headers=config.HEADERS)

    return response


def get_order(track_id):
    return requests.get(config.URL_SERVICE + config.GET_ORDER_PATH + f'?t={track_id}')
