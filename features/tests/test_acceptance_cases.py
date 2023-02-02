import time
from features.business_utils.business_utils import BusinessLogic

class TestCases:

    utils_obj = BusinessLogic
    url_to_navigate = "https://www.shino.de/parkcalc/"

    def create_logic_class_instance(self):
        utils_obj = BusinessLogic()
        return utils_obj

    def test_valet_parking_less_than_5_hours(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Valet Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="01:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 12.00")
        assert resultant_cost


    def test_valet_parking_for_5_hours(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Valet Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="03:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 12.00")
        assert resultant_cost


    def test_valet_parking_more_than_5_hours(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Valet Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="11:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 18.00")
        assert resultant_cost


    def test_valet_parking_more_than_single_day(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Valet Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/04/2023", parking_time="11:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 36.00")
        assert resultant_cost


    def test_short_term_parking_for_1_hour(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Short-Term Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="11:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 2.00")
        assert resultant_cost


    def test_short_term_parking_for_11hours_30mins(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Short-Term Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="09:30", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 23.00")
        assert resultant_cost


    def test_short_term_parking_for_12hours(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Short-Term Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 24.00")
        assert resultant_cost


    def test_short_term_parking_for_more_than_12hours_single_day(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Short-Term Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="11:30", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 24.00")
        assert resultant_cost


    def test_short_term_parking_for_more_than_single_day(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Short-Term Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/04/2023", parking_time="11:30", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 27.00")
        assert resultant_cost


    def test_economy_parking_for_1_hour(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Economy Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="11:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 2.00")
        assert resultant_cost


    def test_economy_parking_for_3hours_30mins(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Economy Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="01:30", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 8.00")
        assert resultant_cost


    def test_economy_parking_for_5_hours(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Economy Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="03:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 9.00")
        assert resultant_cost


    def test_economy_parking_for_more_than_single_day(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Economy Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/04/2023", parking_time="11:45", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 13.00")
        assert resultant_cost


    def test_long_term_garage_parking_for_1_hour(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Long-Term Garage Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="11:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 2.00")
        assert resultant_cost


    def test_long_term_garage_parking_for_6_hours(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Long-Term Garage Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="04:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 12.00")
        assert resultant_cost


    def test_long_term_garage_parking_for_more_than_6_hours_single_day(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Long-Term Garage Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="11:30", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 12.00")
        assert resultant_cost


    def test_long_term_garage_parking_for_more_than_single_day(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Long-Term Garage Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/04/2023", parking_time="11:30", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 16.00")
        assert resultant_cost


    def test_long_term_garage_parking_for_whole_week(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Long-Term Garage Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/10/2023", parking_time="10:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 72.00")
        assert resultant_cost


    def test_long_term_surface_parking_for_1_hour(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Long-Term Surface Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="11:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 2.00")
        assert resultant_cost


    def test_long_term_surface_parking_for_5_hours(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Long-Term Surface Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="03:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 10.00")
        assert resultant_cost


    def test_long_term_surface_parking_for_more_than_5_hours_single_day(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Long-Term Surface Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="11:30", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "PM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 10.00")
        assert resultant_cost


    def test_long_term_surface_parking_for_more_than_single_day(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Long-Term Surface Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/04/2023", parking_time="11:30", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 14.00")
        assert resultant_cost


    def test_long_term_surface_parking_for_whole_week(self):
        utils_obj = self.create_logic_class_instance()
        utils_obj.open_browser()
        utils_obj.navigate_to_page(self.url_to_navigate)
        utils_obj.select_parking_type("Long-Term Surface Parking")
        utils_obj.select_parking_date_time(parking_date="02/03/2023", parking_time="10:00" , parking_mode="Entry")
        utils_obj.select_time_mode("Entry","AM")
        utils_obj.select_parking_date_time(parking_date="02/10/2023", parking_time="10:00", parking_mode="Exit")
        utils_obj.select_time_mode("Exit", "AM")
        utils_obj.click_calculate_btn()
        resultant_cost = utils_obj.verify_result("$ 60.00")
        assert resultant_cost





