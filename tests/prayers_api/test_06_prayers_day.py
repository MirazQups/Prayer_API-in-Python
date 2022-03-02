import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get prayer day times')
def test_06_day_prayer_times_for_shenzhen():
    response_body, status_code = response_get_times_this_day()
    print(response_body)
    assert status_code == 200
