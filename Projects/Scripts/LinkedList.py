# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:01:13 2020

@author: Rishav Nath Pati
"""


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None


class SLinkedList:
    def __init__(self):
        self.head_val = None

    def listprint(self):  # Linked List printer
        printval = self.head_val
        while printval is not None:
            print(printval.data_val + "->", end=" ")
            printval = printval.next_val

    def atBegining(self, new_data):  # Add at the begining
        NewNode = Node(new_data)
        NewNode.next_val = self.head_val
        self.head_val = NewNode

    def insertAfter(self, prev, new_data):  # Add in between 2 nodes
        temp_head = self.head_val
        if temp_head is not None:
            if temp_head.data_val == prev:
                print(temp_head.data_val)
                NewNode = Node(new_data)
                NewNode.next_val = prev.next_val
                prev.next_val = NewNode
                return
            print("Previous value not present in the list")
            return

        if prev is None:
            print("The mentioned node is absent")
            return

        if temp_head is not None:
            if temp_head.data_val == prev:
                break

    NewNode = Node(new_data)
    NewNode.next_val = prev.next_val
    prev.next_val = NewNode

    def atEnd(self, new_data):  # Add at the end
        NewNode = Node(new_data)
        if self.head_val is None:
            self.head_val = NewNode
            return
        last = self.head_val
        while last.next_val:
            last = last.next_val
        last.next_val = NewNode

    def removeNode(self, remove_key):
        global prev
        temp_head = self.head_val
        if temp_head is not None:
            if temp_head.data_val == remove_key:
                self.head_val = temp_head.next_val
                print("Value was deleted from head node")
                return
        while temp_head is not None:
            if temp_head.data_val == remove_key:
                break
            prev = temp_head
            temp_head = temp_head.next_val
        if temp_head is None:
            print("Value to be deleted not found")
            return

        prev.next_val = temp_head.next_val


list = SLinkedList()
list.head_val = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")
list.head_val.next_val = e2
e2.next_val = e3

begin = input("Enter value to be inserted at begining: ")
list.atBegining(begin)

mid = input("Enter value to be inserted: ")
mid_input_data = input("Enter value after which new data is to be inserted: ")
list.insertAfter(mid_input_data, mid)

end = input("Enter value to be inserted at the end: ")
list.atEnd(end)

list.removeNode("Sunday")

print("\n*******LINKED LIST*******")
list.listprint()
print("NULL")
