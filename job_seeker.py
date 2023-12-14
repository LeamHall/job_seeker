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
        self.searchables = [
            self.title.lower(),
            self.notes.lower(),
            self.company.lower(),
            self.url.lower(),
            self.poc_name.lower(),
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


def job_builder(line):
    _list = string_to_list(line)
    data = {
        "last_contact": _list[0],
        "first_contact": _list[1],
        "poc_name": _list[2],
        "company": _list[3],
        "notes": _list[4],
        "active": _list[5],
        "url": _list[6],
        "title": _list[7],
    }
    return Job(data)


class POC:
    """Stores the contact info for each Point of Contact"""

    def __init__(self, data={}):
        self.name = data.get("name", "")
        self.company = data.get("company", "")
        self.phone = data.get("phone", "")
        self.email = data.get("email", "")
        self.first_contact = data.get("first_contact", convert_date(dt.now()))
        self.last_contact = data.get("last_contact", convert_date(dt.now()))
        self.searchables = [
            self.name.lower(),
            self.company.lower(),
            self.email.lower(),
        ]

    def __str__(self):
        """Returns a formatted string with the POC info"""
        return "{}, ({}) {}  [{}]\nFirst Contact: {}, Last Contact: {}".format(
            self.name,
            self.phone,
            self.email,
            self.company,
            self.first_contact,
            self.last_contact,
        )


def poc_builder(line):
    _list = string_to_list(line)
    data = {
        "name": _list[0],
        "phone": _list[1],
        "email": _list[2],
        "company": _list[3],
        "first_contact": _list[4],
        "last_contact": _list[5],
    }
    return POC(data)


def convert_date(date):
    """Takes a datetime.datetime object and returns a YYYMMDD string"""
    return "{}{:0>2}{:0>2}".format(date.year, date.month, date.day)


def list_from_file(filename):
    """Takes a file, removes comments/empty lines, returns a list of each line"""
    lines = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) > 5 and not line.startswith("#"):
                lines.append(line)
    return lines


def parse_list(_list, _list_type, search):
    """Takes a list, and the element type, and prints any that match search"""
    items = []
    for element in _list:
        if search.lower() in element.lower():
            if _list_type == "poc":
                items.append(poc_builder(element))
            if _list_type == "job":
                items.append(job_builder(element))
    return items


def string_to_list(data, sep=";"):
    """Takes a sep separated string and converts it to a list"""
    return [e.strip() for e in data.split(sep)]


def items_from_file(filename, klass):
    """Takes a filename, and returns objects based on that file."""
    with open(filename, "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        result = [klass(row) for row in reader]

    return result


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


if __name__ == "__main__":
    datadir = "data"
    job_file = "jobs.txt"
    poc_file = "pocs.txt"

    try:
        poc_list = items_from_file(os.path.join(datadir, poc_file), POC)
        job_list = items_from_file(os.path.join(datadir, job_file), Job)
    except:
        print("Can't find the data files")
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a", "--add", help="add data, requires -r or -p", action="store_true"
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
        print("I am to add")

    if args.search:
        results = search_items(args.search, job_list, poc_list)
        for result in results:
            print(result, "\n")
