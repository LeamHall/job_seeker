# name    :	tests/test_job_seeker.py
# version :	0.0.1
# date    :	20230203
# author  :	Leam Hall
# desc    :	Test job_seeker.py

from datetime import datetime as dt
import unittest

import job_seeker


class TestJobSeeker(unittest.TestCase):

    def setUp(self):
        self.job_data = {
            "last_contact":     "20230123",
            "first_contact":    "20230201",
            "poc_name":         "Fred Smythe",
            "company":          "Some Great Place, LLC",
            "notes":            "Great fit!",
            "active":           True,
            "url":              "https://example.com/r12345",
            "title":            "Senior Automation Engineer",
            "main_skills":      ["linux", "python", "ansible"]
        }

        self.poc_data = {
            "name":     "Fred Smythe",
            "phone":    "555.555.1212",
            "email":    "fred@example.com",
            "company":  "Example, Inc",
            "first_contact":    "20230123",
            "last_contact":     "20230201",
        }


    def tearDown(self):
        pass

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
        j = job_seeker.Job(self.job_data)
        self.assertTrue(j.last_contact  == "20230123")
        self.assertTrue(j.first_contact == "20230201")
        self.assertTrue(j.poc_name      == "Fred Smythe")
        self.assertTrue(j.company       == "Some Great Place, LLC")
        self.assertTrue(j.notes         == "Great fit!")
        self.assertTrue(j.active        == True)
        self.assertTrue(j.url           == "https://example.com/r12345")
        self.assertTrue(j.title         == "Senior Automation Engineer")
        self.assertTrue(j.main_skills   == ["linux", "python", "ansible"])

    def test_poc_defaults(self):
        p       = job_seeker.POC()
        date    = dt.now()
        year    = str(date.year)
        self.assertTrue(p.name  == None)
        self.assertTrue(p.email == None)
        self.assertTrue(p.phone == None)
        self.assertTrue(p.first_contact.startswith(year))
        self.assertTrue(p.last_contact.startswith(year))
    
    def test_poc_data(self):
        p   = job_seeker.POC(self.poc_data)
        self.assertTrue(p.name          == "Fred Smythe")
        self.assertTrue(p.phone         == "555.555.1212")
        self.assertTrue(p.email         == "fred@example.com")             
        self.assertTrue(p.company       == "Example, Inc")
        self.assertTrue(p.first_contact == "20230123")
        self.assertTrue(p.last_contact  == "20230201")

    def test_poc_string(self):
        p       = job_seeker.POC(self.poc_data)
        results = p.__str__().split("\n")
        self.assertTrue(results[0] == 
            "Fred Smythe, (555.555.1212) fred@example.com  [Example, Inc]")
        self.assertTrue(results[1] ==
            "First Contact: 20230123, Last Contact: 20230201")


        
        
