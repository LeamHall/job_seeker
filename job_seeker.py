#!/usr/bin/env python
# name:     job_seeker.py
# version:  0.0.1
# date:     20211129
# author:   Leam Hall
# desc:     Track data on job applications


from datetime import datetime as dt

class Job:
    """ Stores the job req data """ 
    def __init__(self, job_data = {}):
        self.last_contact   = job_data.get("last_contact", convert_date(dt.now()))
        self.first_contact  = job_data.get("first_contact", convert_date(dt.now()))
        self.poc_name       = job_data.get("poc_name", None)
        self.company        = job_data.get("company", None)
        self.notes          = job_data.get("notes", None)
        self.active         = job_data.get("active", True)
        self.url            = job_data.get("url", None)
        self.title          = job_data.get("title", None)
        self.main_skills    = job_data.get("main_skills", [])

 
class POC():
    """ Stores the contact info for each Point of Contact """
    def __init__(self, data = {}):
        self.name   = data.get('name', None)
        self.company        = data.get('company', None)
        self.phone          = data.get('phone', None)
        self.email          = data.get('email', None)
        self.first_contact  = data.get("first_contact", convert_date(dt.now()))
        self.last_contact   = data.get('last_contact', convert_date(dt.now()))

    def __str__(self):
        """ Returns a formatted string with the POC info """
        return "{}, ({}) {}  [{}]\nFirst Contact: {}, Last Contact: {}".format(
            self.name, 
            self.phone,
            self.email,
            self.company,
            self.first_contact,
            self.last_contact)

 
def convert_date(date):
    """ Takes a datetime.datetime object and returns a YYYMMDD string """
    return "{}{:0>2}{:0>2}".format(date.year, date.month, date.day)

def string_to_list(data, sep = ','):
    """ Takes a comma separated string and converts it to a list """ 
    return [ e.strip() for e in data.split(',') ]
 

datadir     = "data"
job_file    = "jobs.txt"
poc_file    = "pocs.txt" 

if __name__ == "__main__":

    print("Still working on all this.")

    # get args
    # -a    add
    # -r    show req if not add
    # -p    show pocs if not add
    # --poc_name
    # --poc_phone
    # --poc_email
    # -t    title
    # --skills
       
    ## set defaults
    
