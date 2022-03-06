# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:46:26 2020

@author: Rishav Nath Pati
"""


from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'rishavnathpati'  # <- enter username here
insta_password = 'csug/194/18'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # activity
    session.like_by_tags(["natgeo"], amount=10)