from dateutil.parser import parse
import null as null


class HolidaysChecker:
    def __init__(self, config):
        self.config = config
        self.bank_holidays_filter = []

    def is_bank_holiday(self, time_entry):
        for holidayEntry in self.config:
            holyday_date = parse(holidayEntry["date"]).date()
            time_entry_spent_date = parse(time_entry["spent_date"]).date()
            print(holyday_date)
            print(time_entry_spent_date)
            if holyday_date == time_entry_spent_date:
                return True
        return False

    def build_filter_for_checker(self):
        for bank_holiday in self.config:
            if bank_holiday["movable"] and bank_holiday["rerunId"] != null:
                self.add_movable_bank_holiday_to_filter(bank_holiday, 1)
            else:
                self.add_bank_holiday_to_filter(bank_holiday)

    def add_movable_bank_holiday_to_filter(self, bank_holiday, moove_allowance):
        pass

    def add_bank_holiday_to_filter(self, bank_holiday):
        pass

# def checkTimeEntry(self, time_entry):
#     if time_entry["spent_date"]
