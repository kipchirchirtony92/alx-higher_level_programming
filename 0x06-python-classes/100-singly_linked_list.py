#!/usr/bin/python3
"""Define classes of a singly linked list"""


class Node:
    """Rep a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """ Initailize the node
        Args: data(int) :-the data of the Node
              next_node :- the next new Node
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Getter method for the data"""
            return (self.__data)

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """Getter method of the next node of the Node class"""
            return (self.__next_node)

        @next_node.setter
        def next_node(self, value):
            if not isinstance(value, Node) and value is not None:
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list"""

    def __init__(self):
        """Initialize a new singlyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """sorted insert method - insert node in order
        Args: value (int): data of new node
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            curr = self.__head
            while (curr.next_node is not None and
                   curr.next_node.data < value):
                curr = curr.next_node
            new.next_node = curr.next_node
            curr.next_node = new

    def __str__(self):
        """string representation of singly linked list
        Returns:
            llstr: new-line separated list string
        """
        curr = self.__head
        llstr = ''
        if curr is None:
            llstr = ''
        elif curr.next_node is None:
            llstr += str(curr.data)
        else:
            while curr.next_node:
                llstr += str(curr.data) + '\n'
                curr = curr.next_node
            llstr += str(curr.data)
        return llstr
