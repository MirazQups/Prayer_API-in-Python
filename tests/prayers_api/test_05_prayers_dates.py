import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get dates prayer times')
def test_04_dates_prayer_times_for_shenzhen():
    response_body, status_code = response_get_times_this_dates()
    print(response_body)
    assert status_code == 200
