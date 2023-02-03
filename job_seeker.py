#!/usr/bin/env python
# name:     job_seeker.py
# version:  0.0.1
# date:     20211129
# author:   Leam Hall
# desc:     Track data on job applications

### Design Philosophy
# 
# Compatible with Python 3.6
# Only use pure python and the standard library 
# Use semi-colon (';') separated text files for data storage
# If submitting code; "no tests" == "no code"
# Maintain a semblance of PEP 8
# 4 spaces per indentation
# Within a block, align assignments and comparisons
# - I am old, and keeping visual organization helps me follow the code


from datetime import datetime as dt

class Job:
    """ Stores the job req data """ 
    def __init__(self, job_data = {}):
        self.last_contact   = job_data.get("last_contact", convert_date(dt.now()))
        self.first_contact  = job_data.get("first_contact", convert_date(dt.now()))
        self.poc_name       = job_data.get("poc_name", None)
        self.notes          = job_data.get("notes", None)
        self.active         = job_data.get("active", True)
        self.url            = job_data.get("url", None)
        self.title          = job_data.get("title", None)
        self.main_skills    = job_data.get("main_skills", [])

 
class POC():
    """ Stores the contact info for each Point of Contact """
    def __init__(self, data = {}):
        self.name = data['name']
        self.email = data['email']
        self.phone = data.get('phone', None)
        self.last_contact = data.get('last_contact', None)

def convert_date(date):
    """ Takes a datetime.datetime object and returns a string,
        in the format YYYYMMDD.
    """
    return "{}{:0>2}{:0>2}".format(date.year, date.month, date.day)

def string_to_list(data, sep = ','):
    """ Takes a comma seperated string and converts it to a list """ 
    return [ e.strip() for e in data.split(',') ]
 

datadir     = "data"
job_file    = "jobs.txt"
poc_file    = "pocs.txt" 

if __name__ == "__main__":

    print("Still working on all this.")

    datadir = "data"
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
    
    # Logic:
    # Given -r <req number>, print out that job request
    # Given -p <POC name>, prints out that Point of Contact
    # Given -r or -p, and -s <string>, searches the relevant file and prints 
    ##  any job or poc that matches <string>
    ##  An empty <string> prints all jobs or pocs
    ##  Not really going to use wildcards or regexs yet
    # Given -a, and -r or -p, and data, adds to the end of the file
    # 
