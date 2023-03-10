# This class contains the locators needed for the assessment
class TestLocators:
    parking_type_dd = "//select[@id='ParkingLot']"
    calculate_btn = "//input[@name='Submit']"
    parking_entry_date = "//input[@id='StartingDate']"
    parking_entry_time = "//input[@id='StartingTime']"
    parking_exit_date = "//input[@id='LeavingDate']"
    parking_exit_time = "//input[@id='LeavingTime']"
    entry_time_am = "//input[@name='StartingTimeAMPM' and @value='AM']"
    entry_time_pm = "//input[@name='StartingTimeAMPM' and @value='PM']"
    exit_time_am = "//input[@name='LeavingTimeAMPM' and @value='AM']"
    exit_time_pm = "//input[@name='LeavingTimeAMPM' and @value='PM']"
    verify_cost = "//td//span[@class='SubHead']"