#!/usr/bin/env python

# name    :  parse_reqs.py
# version :  0.0.1
# date    :  20241021
# author  :  Leam Hall
# desc    :  Parse job reqs and get information.

import argparse
import os
import os.path
import pprint
import sys

REQDIR = "/home/leam/Desktop/Documents/JobSearch/active"
KEYWORDSDIR = "/home/leam/Desktop/Documents/JobSearch/keywords"

def make_word_list(file):
    """ Makes a list of lowercase items from a file. """
    word_list = list()
    with open(file, "r") as in_f:
        data = in_f.readlines()
        for word in data:
            word = word.strip()
            word = word.lower()
            word_list.append(word)
    return word_list
 
skills = dict()
all_lines = list()
odd_skills = list()
really_odd_skills = list()

def add_skill(skill_data, skill):
    """ Add/initialize skill into skill_data. """
    if skill in skill_data:
        skill_data[skill] += 1
    else:
        skill_data[skill] = 1

def scrub_word(word):
    """ Really scrub the word, usually in multi-word line. """
    word = word.replace(',', " ")
    word = word.replace('•', " ")
    word = word.replace('.', " ")
    word = word.replace('(', " ")
    word = word.replace(')', " ")
    word = word.replace('-', " ")
    word = word.strip()
    word = word.lower()
    return word
    
def scrub_skill(skill_data, skill, really_odd_skills):
    """ Really scrub the skill, usually in multi-skill line. """
    skill = scrub_word(skill)
    
    if " " in skill:
        skill_array = skill.split()
        for s in skill_array:
            s = scrub_word(s)
            if s in remove_words:
                continue
            else:
                add_skill(skill_data, s, remove_words)
    else:
        add_skill(skill_data, skill, remove_words)

        
remove_file = os.path.join(KEYWORDSDIR, "remove_words.txt")
remove_words = make_word_list(remove_file)
 
file_paths = []
for root, dirs, files in os.walk(REQDIR):
    for file in files:
        if file.endswith('.txt'):
            file_paths.append(
                os.path.join(os.path.abspath(root),
                file)
                )

for file in file_paths:
    with open(
        os.path.join(REQDIR, file), "r") as in_f:
            INQUALS = False
            data = in_f.readlines()
            for item in data:
                item = item.strip()
                if not len(item):
                    continue
                elif item == "ENDQUALS":
                    INQUALS = False
                elif item == "QUALS":
                    INQUALS = True
                elif INQUALS:
                    item = scrub_word(item)
                    all_lines += item.split()
                else:
                    continue

for item in all_lines:
    if item not in remove_words:
        add_skill(skills, scrub_word(item))


def value_getter(item):
    return item[1]

#sorted(skills.items(), key = value_getter)
#pprint.pp(skills)
for k,v in sorted(skills.items(), key = value_getter):
    print("{:3}  {}".format(v, k))

#possible_words = os.path.join(KEYWORDSDIR, "possible_words.txt")
#with open(possible_words, "w") as out_f:
#    for key in skills.keys():
#        out_f.write("{}\n".format(key))


