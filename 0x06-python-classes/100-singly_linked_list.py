#!/usr/bin/python3
"""100-slighty_linkeed_list module

This module contains the class Node, which defines a node
of a slightly linked list by:
- Private instance attribute: data:
    - property def data(self): to retrieve it
    - property setter def data(self, value): to set it:
        - data must be an integer, otherwise raise
        a TypeError exception with the message:
         'data must be an integer'

- Private instance attribute: next_node:
    - property def next_node(self): to retrieve it
    - property setter def next_node(self, value): to set it:
        - next_node can be None or must be a Node, otherwise
        raise a TypeError exception with the message:
         'next_node must be a Node object'

- Instantiation with data and next_node:
    def __init__(self, data, next_node=None):

and another class SinglyLinkedList that defines a singly
linked list by:
- Private instance attribute: head(no setter or getter)

- Simple instantiation: def __init__(self):

- Should be printale:
    - print the entire list in stdout
    - one node number by line

- Public instance method: def sorted_insert(self, value):
  that inserts a new Node into the correct sorted position
  in the list (increasing order)

- without importing any module

"""


class Node:
    """class Node

    This class defines a node of a singly linked list

    """

    def __init__(self, data, next_node=None):
        """__init__ method

        This method is used to initialize data and next_node args

        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data method

        This method is used to retrieve the property of data

        """
        return self.__data

    @data.setter
    def data(self, value):
        """data.setter method

        This method is used to set the data value of Node object

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ next_node method

        This method is used to retrieve the property of next_node

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node.setter method

        This method is used to set the next_node value of Node object

        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class SlightlyLinkedList

    This class defines a singly linked list

    """
    # __head = None

    def __str__(self):
        """__str__method

        Method to print singly linked list

        """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self, head=None):
        """__init__ method

        This method is used to initialize head args

        """
        self.__head = head

    def sorted_insert(self, value):
        """sorted__insert method

        This method is used to sort the elements in a singly linked list

        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
