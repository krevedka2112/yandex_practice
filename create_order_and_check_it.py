import request_builder
import client_data


def positive_asserts():
    order_response = request_builder.post_new_order(client_data.client_body)
    track_id = order_response.json()["track"]

    assert order_response.status_code == 201, (f"Expected '201' status code in response"
                                               f" but its: {order_response.status_code}")
    assert isinstance(track_id, int), (f"Expected 'id' in response to be int number"
                                       f" but its: {type(track_id).__name__}")

    order_data_response = request_builder.get_order(track_id)

    assert order_data_response.status_code == 200, (f"Expected '200' status code in response"
                                                    f" but its: {order_data_response.status_code}")
    order_data = order_data_response.json()["order"]
    assert order_data["firstName"] == client_data.client_body["firstName"], (
        f"Expected 'firstName' in client data to be{client_data.client_body['firstName']} "
        f"but its: {order_data['firstName']}")
    assert order_data["lastName"] == client_data.client_body["lastName"], (
        f"Expected 'lastName' in client data to be {client_data.client_body['lastName']} "
        f"but its: {order_data['lastName']}")
    assert order_data["address"] == client_data.client_body["address"], (
        f"Expected 'address' in client data to be {client_data.client_body['address']} "
        f"but its: {order_data['address']}")
    assert order_data["metroStation"] == client_data.client_body["metroStation"], (
        f"Expected 'metroStation' in client data to be {client_data.client_body['metroStation']} "
        f"but its: {order_data['metroStation']}")
    assert order_data["phone"] == client_data.client_body["phone"], (
        f"Expected 'phone' in client data to be {client_data.client_body['phone']} "
        f"but its: {order_data['phone']}")
    assert order_data["rentTime"] == client_data.client_body["rentTime"], (
        f"Expected 'rentTime' in client data to be {client_data.client_body['rentTime']} "
        f"but its: {order_data['rentTime']}")

    assert order_data["cancelled"] is False, (
        f"Expected flag 'cancelled' in client data to be False but its: {order_data['cancelled']}")
    assert order_data["finished"] is False, (
        f"Expected flag 'finished' in client data to be False but its: {order_data['finished']}")
    assert order_data["inDelivery"] is False, (
        f"Expected flag 'inDelivery' in client data to be False but its: {order_data['inDelivery']}")


# Роман Бусыгин, 24-я когорта — Финальный проект. Инженер по тестированию плюс
# Успешное создание заказа и проверка его получения
# Заполнены только обязательные поля, заказ не взят в работу
def test_create_order():
    positive_asserts()
