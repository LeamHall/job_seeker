# name    :	tests/test_job_seeker.py
# version :	0.0.1
# date    :	20230203
# author  :	Leam Hall
# desc    :	Test job_seeker.py

# pylint: skip-file

from datetime import datetime as dt
import os.path
import tempfile
import unittest

import job_seeker


class TestJobSeeker(unittest.TestCase):
    def setUp(self):
        self.job_data_1 = {
            "last_contact": "20230123",
            "first_contact": "20230201",
            "poc_name": "Fred Smythe",
            "company": "Some Great Place, LLC",
            "notes": "linux, ansible, python",
            "active": "y",
            "url": "https://example.com/r12345",
            "title": "Senior Automation Engineer",
        }

        self.poc_data_1 = {
            "poc_name": "Fred Smythe",
            "phone": "555.555.1212",
            "email": "fred@example.com",
            "company": "Example, Inc",
            "first_contact": "20230123",
            "last_contact": "20230201",
        }

        self.job_data_2 = {
            "last_contact": "20230123",
            "first_contact": "20230201",
            "poc_name": "Jason Jayson",
            "company": "Can't read resume, Inc",
            "notes": "windows server, powershell",
            "active": "n",
            "url": "https://whocares.com",
            "title": "Winderz admin",
        }

        self.poc_data_2 = {
            "name": "Jason Jayson",
            "phone": "br-549",
            "email": "jay@whocares.com",
            "company": "Whocares, Inc",
            "first_contact": "20230101",
            "last_contact": "20230101",
        }

        self.company_data_1 = {
            "key": "sGPL",
            "name": "Some Great Place, LLC",
            "job_url": "https://www.sgpl.com/jobs",
        }

        self.test_dir = tempfile.TemporaryDirectory()
        self.data_file = os.path.join(self.test_dir.name, "data.txt")
        with open(self.data_file, "w") as f:
            f.write("\n\n\n#bogus line\ngood line\n\n\n")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_convert_date(self):
        date = dt.now()
        expected = str(date.year)
        result = job_seeker.convert_date(dt.now())
        self.assertTrue(result.startswith(expected))

    def test_string_to_list(self):
        my_str = "linux;  python;  ansible      "
        expected = ["linux", "python", "ansible"]
        result = job_seeker.string_to_list(my_str)
        self.assertTrue(result == expected)

    def test_job_defaults(self):
        j = job_seeker.Job()
        date = dt.now()
        year = str(date.year)
        self.assertTrue(j.last_contact.startswith(year))
        self.assertTrue(j.first_contact.startswith(year))
        self.assertTrue(j.active == "y")

    def test_job_data(self):
        j = job_seeker.Job(self.job_data_1)
        self.assertTrue(j.last_contact == "20230123")
        self.assertTrue(j.first_contact == "20230201")
        self.assertTrue(j.poc_name == "Fred Smythe")
        self.assertTrue(j.company == "Some Great Place, LLC")
        self.assertTrue(j.notes == "linux, ansible, python")
        self.assertTrue(j.active == "y")
        self.assertTrue(j.url == "https://example.com/r12345")
        self.assertTrue(j.title == "Senior Automation Engineer")

    def test_builder(self):
        job = job_seeker.builder(self.job_data_1, job_seeker.Job)
        self.assertTrue(job.title == "Senior Automation Engineer")

    def test_poc_defaults(self):
        p = job_seeker.POC()
        date = dt.now()
        year = str(date.year)
        self.assertFalse(p.poc_name)
        self.assertFalse(p.email)
        self.assertFalse(p.phone)
        self.assertTrue(p.first_contact.startswith(year))
        self.assertTrue(p.last_contact.startswith(year))

    def test_poc_data(self):
        p = job_seeker.POC(self.poc_data_1)
        self.assertTrue(p.poc_name == "Fred Smythe")
        self.assertTrue(p.phone == "555.555.1212")
        self.assertTrue(p.email == "fred@example.com")
        self.assertTrue(p.company == "Example, Inc")
        self.assertTrue(p.first_contact == "20230123")
        self.assertTrue(p.last_contact == "20230201")

    def test_poc_string(self):
        p = job_seeker.POC(self.poc_data_1)
        results = p.__str__().split("\n")
        self.assertTrue(
            results[0]
            == "Fred Smythe, (555.555.1212) fred@example.com  [Example, Inc]"
        )
        self.assertTrue(
            results[1] == "First Contact: 20230123, Last Contact: 20230201"
        )

    def test_searchables(self):
        j = job_seeker.Job(self.job_data_1)
        self.assertIn("fred smythe", j.searchables)
        p = job_seeker.POC(self.poc_data_1)
        self.assertIn("fred smythe", p.searchables)

    def test_company_info(self):
        c = job_seeker.Company(self.company_data_1)
        self.assertEqual(c.key, "sgpl")
        self.assertEqual(c.name, "Some Great Place, LLC")
        self.assertEqual(c.job_url, "https://www.sgpl.com/jobs")
