import json

import requests

auth_response = requests.post('https://restful-booker.herokuapp.com/auth', json={"username": "admin",
                                                                                 "password": "password123"})
token = auth_response.json().get('token')

booking_info = {
    "firstname": "Mikhail",
    "lastname": "Surikov",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2023-12-01",
        "checkout": "2023-12-08"
    },
    "additionalneeds": "Breakfast and Lunch"
}
create_booking_response = requests.post('https://restful-booker.herokuapp.com/booking', json=booking_info)
my_booking_id = create_booking_response.json().get('bookingid')
check_my_booking_response = requests.get(f'https://restful-booker.herokuapp.com/booking/{my_booking_id}')
print(json.dumps(check_my_booking_response.json(), indent=4))
new_booking_info = {
    "bookingdates": {
        "checkin": "2023-12-05",
        "checkout": "2023-12-08"
    }
}
edit_booking_response = requests.patch(f'https://restful-booker.herokuapp.com/booking/{my_booking_id}',
                                       json=new_booking_info, cookies=dict(token=f'{token}'))
new_check_my_booking_response = requests.get(f'https://restful-booker.herokuapp.com/booking/{my_booking_id}')
print(json.dumps(new_check_my_booking_response.json(), indent=4))
delete_booking_response = requests.delete(f'https://restful-booker.herokuapp.com/booking/{my_booking_id}',
                                          cookies=dict(token=f'{token}'))
print(delete_booking_response.text)
check_deleted_response = requests.get(f'https://restful-booker.herokuapp.com/booking/{my_booking_id}')
print(check_deleted_response)
