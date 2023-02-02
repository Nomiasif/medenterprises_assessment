import time
from features.business_utils.business_utils import BusinessLogic

class TestCases:

    utils_obj = BusinessLogic
    url_to_navigate = "https://www.shino.de/parkcalc/"

    def create_logic_class_instance(self):
        utils_obj = BusinessLogic()
        return utils_obj

    def test_valet_parking_happy_path(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Valet Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="01:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        time.sleep(3)


