# name    :	tests/test_job_seeker.py
# version :	0.0.1
# date    :	20230203
# author  :	Leam Hall
# desc    :	Test job_seeker.py

from datetime import datetime as dt
import unittest

import job_seeker


class TestJobSeeker(unittest.TestCase):

    def test_convert_date(self):
        date        = dt.now()
        expected    = str(date.year)
        result      = job_seeker.convert_date(dt.now())
        self.assertTrue(result.startswith(expected))

    def test_string_to_list(self):
        my_str      = "linux,  python,  ansible      "
        expected    = ["linux", "python", "ansible"]
        result      = job_seeker.string_to_list(my_str)
        self.assertTrue(result == expected)

    def test_job_defaults(self):
        j       = job_seeker.Job()
        date    = dt.now()
        year    = str(date.year)
        self.assertTrue(j.last_contact.startswith(year))
        self.assertTrue(j.first_contact.startswith(year))
        self.assertTrue(j.active == True)
        self.assertTrue(type(j.main_skills) == list)

    def test_job_data(self):
        data = {
            "last_contact":     "20230123",
            "first_contact":    "20230201",
            "poc_name":         "Fred Smythe",
            "notes":            "Great fit!",
            "active":           True,
            "url":              "https://example.com/r12345",
            "title":            "Senior Automation Engineer",
            "main_skills":      ["linux", "python", "ansible"]
        }
        j = job_seeker.Job(data)
        self.assertTrue(j.last_contact  == "20230123")
        self.assertTrue(j.first_contact == "20230201")
        self.assertTrue(j.poc_name      == "Fred Smythe")
        self.assertTrue(j.notes         == "Great fit!")
        self.assertTrue(j.active        == True)
        self.assertTrue(j.url           == "https://example.com/r12345")
        self.assertTrue(j.title         == "Senior Automation Engineer")
        self.assertTrue(j.main_skills   == ["linux", "python", "ansible"])


    
            

