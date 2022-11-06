#!/usr/bin/python3
""" Module that contains a function to read text file """


def read_file(filename=""):
    """ Function that reads data from file  """
    with open(filename, 'r', encoding="utf-8") as file:
        file_data = file.read()
        print(file_data, end='')
