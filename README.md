[![<LeamHall>](https://circleci.com/gh/LeamHall/job_seeker.svg?style=shield)](https://app.circleci.com/pipelines/github/LeamHall/job_seeker?branch=master&filter=all)

# job_seeker

Tracks job applications and contacts


## Logic

- Given -r `req number`, print out that job request
- Given -p `POC name`, prints out that Point of Contact
- [TODO] Given -a, and -r or -p, and data, adds to the end of the file
- Given -r or -p, and -s `string`, searches the relevant file and prints 
    any job or poc that matches `string`
- - An empty `string` prints all jobs or pocs
- - Not really going to use wildcards or regexs yet
    
## Examples

### List of Points of Contact

```
./job_seeker.py -p
Fred Smythe, (555.555.1212) fred@example.com  [Example, Inc]
First Contact: 20230123, Last Contact: 20202102 

Jayne Johnson, (123.456.7890) jj@otherexample.com  [Other Recruiter, LLC]
First Contact: 20221212, Last Contact: 20221212 

Jason Jayson, (br-549) jay@whocares.com  [Whocares, Inc]
First Contact: 20230101, Last Contact: 20230101
```

### Find a specific contact's info

```
./job_seeker.py -p -s smythe
Fred Smythe, (555.555.1212) fred@example.com  [Example, Inc]
First Contact: 20230123, Last Contact: 20202102
```

### Find jobs that mention linux

```
./job_seeker.py -j -s linux
Senior Automation Engineer
Active: y  Notes: linux, ansible, python
Some Great Place, LLC,  https://example.com/r12345
Fred Smythe 
Last chat: 20230123, First chat: 20230201
```



 
