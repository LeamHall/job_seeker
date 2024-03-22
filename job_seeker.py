#!/usr/bin/env python
# name:     job_seeker.py
# version:  0.0.1
# date:     20211129
# author:   Leam Hall
# desc:     Track data on job applications

import argparse
import csv
from datetime import datetime as dt
import os.path
import sys


class Job:
    """Stores the job req data"""

    def __init__(self, job_data={}):
        self.title = job_data.get("title", "")
        self.active = job_data.get("active", "y")
        self.notes = job_data.get("notes", "")
        self.company = job_data.get("company", "")
        self.url = job_data.get("url", "")
        self.poc_name = job_data.get("poc_name", "")
        self.last_contact = job_data.get(
            "last_contact", convert_date(dt.now())
        )
        self.first_contact = job_data.get(
            "first_contact", convert_date(dt.now())
        )
        self.make_raw_data()
        self.searchables = [
            self.title.lower(),
            self.notes.lower(),
            self.company.lower(),
            self.url.lower(),
            self.poc_name.lower(),
            self.raw_data.lower(),
        ]

    def __str__(self):
        if self.active == "y":
            self.active = "Yes"
        else:
            self.active = "No"
        return "Title: {}\nActive: {}\nNotes: {}\nCompany: {} ({})\nPOC:  {} \nLast contact: {}\nFirst contact: {}".format(
            self.title,
            self.active,
            self.notes,
            self.company,
            self.url,
            self.poc_name,
            self.last_contact,
            self.first_contact,
        )

    def make_raw_data(self):
        """Creates the line properly."""
        self.raw_data = ";".join(
            [
                self.poc_name,
                self.company,
                self.active,
                self.url,
                self.title,
                self.notes,
                self.first_contact,
                self.last_contact,
            ]
        )


class POC:
    """Stores the contact info for each Point of Contact"""

    def __init__(self, data={}):
        self.poc_name = data.get("poc_name", "")
        self.company = data.get("company", "")
        self.phone = data.get("phone", "")
        self.email = data.get("email", "")
        self.first_contact = data.get("first_contact", convert_date(dt.now()))
        self.last_contact = data.get("last_contact", convert_date(dt.now()))
        self.make_raw_data()
        self.searchables = [
            self.poc_name.lower(),
            self.company.lower(),
            self.email.lower(),
            self.raw_data.lower(),
        ]

    def make_raw_data(self):
        """Creates the line properly."""
        self.raw_data = ";".join(
            [
                self.poc_name,
                self.company,
                self.phone,
                self.email,
                self.first_contact,
                self.last_contact,
            ]
        )

    def __str__(self):
        """Returns a formatted string with the POC info"""
        return "{}, ({}) {}  [{}]\nFirst Contact: {}, Last Contact: {}".format(
            self.poc_name,
            self.phone,
            self.email,
            self.company,
            self.first_contact,
            self.last_contact,
        )


def builder(data, klass):
    if type(data) is dict:
        return klass(data)
    _list = string_to_list(data)
    today = convert_date(dt.now())
    if klass == POC:
        if len(_list) < 5:
            _list.append(today)
        if len(_list) < 6:
            _list.append(today)
        data = {
            "poc_name": _list[0],
            "phone": _list[1],
            "email": _list[2],
            "company": _list[3],
            "first_contact": _list[4],
            "last_contact": _list[5],
        }
        return POC(data)
    elif klass == Job:
        if len(_list) < 7:
            _list.append(today)
        if len(_list) < 8:
            _list.append(today)
        data = {
            "poc_name": _list[0],
            "company": _list[1],
            "active": _list[2],
            "url": _list[3],
            "title": _list[4],
            "notes": _list[5],
            "first_contact": _list[6],
            "last_contact": _list[7],
        }
        return Job(data)


def convert_date(date):
    """Takes a datetime.datetime object and returns a YYYMMDD string"""
    return "{}{:0>2}{:0>2}".format(date.year, date.month, date.day)


def string_to_list(data, sep=";"):
    """Takes a sep separated string and converts it to a list"""
    return [e.strip() for e in data.split(sep)]


def items_from_file(filename, klass):
    """Takes a filename, and returns objects based on that file."""
    with open(filename, "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        results = [builder(row, klass) for row in reader]

    return results


def search_items(search_term, *lists):
    """
    Searches the values of each item in a list of objects.
    Returns a list of objects with the search_term.
    """
    results = []
    for _list in lists:
        for item in _list:
            for searchable in item.searchables:
                if search_term.lower() in searchable:
                    results.append(item)
                    break
    return results


def write_file(filename, data, string):
    """Writes the data in the proper format."""
    with open(filename, "w") as f:
        f.write(string + "\n")
        for item in data:
            f.write(item.raw_data + "\n")


if __name__ == "__main__":
    datadir = "data"
    job_file = os.path.join(datadir, "jobs.txt")
    poc_file = os.path.join(datadir, "pocs.txt")
    JOB_STRING = "poc_name;company;active;url;title;notes"
    POC_STRING = "poc_name;phone;email;company"
    INFO_STRING = """
                Here are the formats, use semi-colons to separate data.
                Sections can be empty, just include the semi-colon seperator.
                Contact dates will default to the date of entry.
                """
    try:
        poc_list = items_from_file(poc_file, POC)
        job_list = items_from_file(job_file, Job)
    except Exception as e:
        print("Can't find the data files", e)
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a", "--add", help="add DATA, requires -j or -p", action="store_true"
    )
    parser.add_argument(
        "-j", "--job", help="use the Job info", action="store_true"
    )
    parser.add_argument(
        "-p", "--poc", help="use the POC info", action="store_true"
    )
    parser.add_argument("-s", "--search", help="SEARCH for", default="")
    args = parser.parse_args()

    if args.add:
        print(INFO_STRING)
        print("Jobs: \n\t {}".format(JOB_STRING))
        print("POCs: \n\t {}".format(POC_STRING))
        data = input("> ")
        if args.job:
            job_list.append(builder(data, Job))
            write_file(
                job_file, job_list, JOB_STRING + ";first_contact;last_contact"
            )
        elif args.poc:
            poc_list.append(builder(data, POC))
            write_file(
                poc_file, poc_list, POC_STRING + ";first_contact;last_contact"
            )
        else:
            print("I am to add, but you give me no details.")
            sys.exit(1)

    if args.search:
        results = search_items(args.search, job_list, poc_list)
        for result in results:
            print(result, "\n")
