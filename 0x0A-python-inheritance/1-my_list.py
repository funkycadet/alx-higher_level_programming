#!/usr/bin/python3
"""
1-my_list module
  - contains class MyList
"""


class MyList(list):
    """ class MyList """

    def print_sorted(self):
      list_ = self.copy()
      list_.sort()
      print(list_)
