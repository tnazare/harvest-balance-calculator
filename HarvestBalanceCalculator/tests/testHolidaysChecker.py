import unittest
import null as null
from HarvestBalanceCalculator import HolidaysChecker

time_entries = [{
    "id": 718532068,
    "spent_date": "2017-01-01",
    "hours": 7.5,
    "notes": null,
    "is_locked": True,
    "locked_reason": "Item Approved and Locked for this Time Period",
    "is_closed": True,
    "is_billed": False,
    "timer_started_at": null,
    "started_time": null,
    "ended_time": null,
    "is_running": False,
    "billable": False,
    "budgeted": False,
    "billable_rate": null,
    "cost_rate": null,
    "created_at": "2017-12-16T16:56:17Z",
    "updated_at": "2018-02-05T17:52:36Z",
    "user": {
        "id": 1204040,
        "name": "Thibaut Nazare"
    },
    "client": {
        "id": 473572,
        "name": "Ingeno",
        "currency": "CAD"
    },
    "project": {
        "id": 3930249,
        "name": "Employés",
        "code": ""
    },
    "task": {
        "id": 2997206,
        "name": "Congé férié"
    },
    "user_assignment": {
        "id": 82666769,
        "is_project_manager": False,
        "is_active": True,
        "budget": null,
        "created_at": "2016-02-02T19:28:29Z",
        "updated_at": "2016-02-02T19:28:29Z",
        "hourly_rate": null
    },
    "task_assignment": {
        "id": 61581250,
        "billable": False,
        "is_active": True,
        "created_at": "2014-04-15T16:27:45Z",
        "updated_at": "2014-04-15T16:27:58Z",
        "hourly_rate": null,
        "budget": null
    },
    "invoice": null,
    "external_reference": null
}]
config = [{
    "id": 1,
    "name": "New Year's Day",
    "date": "2017-01-01",
    "movable": False,
    "rerunId": null
},
{
"id": 2,
"name": "Reprise 1er janvier",
"date": "2017-01-02",
"movable": True,
"rerunId" : 1
}]
holidayChecker = HolidaysChecker(config)


class TestHolidaysChecker(unittest.TestCase):
    def test_that_we_find_bank_holiday(self):
        self.assertEqual(True, holidayChecker.is_bank_holiday(time_entries[0]))

    def test_that_we_build_filter_correctly(self):
        holidayChecker.build_filter_for_checker()
        self.assertEqual(3, len(holidayChecker.bank_holidays_filter))


if __name__ == '__main__':
    unittest.main()
