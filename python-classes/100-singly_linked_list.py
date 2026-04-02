#!/usr/bin/python3
"""Singly linked list module."""


class Node:
    """Node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize Node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list."""

    def __init__(self):
        """Initialize list."""
        self.__head = None

    def __str__(self):
        """String rep."""
        res = []
        tmp = self.__head
        while tmp:
            res.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(res)

    def sorted_insert(self, value):
        """Insert node in sorted order."""
        new = Node(value)
        if self.__head is None or self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
