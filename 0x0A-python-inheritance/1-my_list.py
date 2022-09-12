#!/usr/bin/python3
"""
1-my_list module
  - contains class MyList
"""


class MyList(list):
    """ class MyList """

    def print_sorted(self):
        return list.sort(self)
