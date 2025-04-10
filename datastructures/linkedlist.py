#done
from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Iterator, Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.count = 0
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        #check that all the items in sequence are of the same type
        # if not isinstance()
        llist = LinkedList(data_type=data_type)
        for item in sequence:
            llist.append(item)
        return llist

    def append(self, item: T) -> None:
        if type(item) != self.data_type:
            raise ValueError("Data is the wrong type")
        node = LinkedList.Node(data=item)

        if self.empty:
            self.head = self.tail = node
        else:
            node.previous =node
            if self.tail:
                self.tail.next = node
            self.tail = node
        self.count +=1

    def prepend(self, item: T) -> None:
       # check that item the same type
       new_node = LinkedList.Node(data= item)
       new_node.next = self.head
       if self.head:
           self.head.previous = new_node
       self.head = new_node
       self.count += 1
    def insert_before(self, target: T, item: T) -> None:
        #Raise ValueError if the target does not exist
        #Raise TypeEror if the target is not the right type
        #Raise TypeError if the item is not the right type

        travel = self.head

        while travel:
            
            if travel.data == target:
                break

            travel = travel.next


        if travel is None:
            raise ValueError(f'The target value {target} was not found in the linked list.')
        
        if travel is self.head:
            self.prepend(item)
            return
        
        #Not the head
        
        
    def insert_after(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_after is not implemented")

    def remove(self, item: T) -> None:
        travel = self.head
        data = item
        self.count -= 1
        while travel:
            if travel.data == item == self.head:
                self.pop_front()
            elif travel.data == item == self.tail:
                self.pop()
            elif travel.data == item:
                travel.next.previous = travel.previous
                travel.previous.next = travel.next
                travel.previous = None
                travel.next = None
        self.count -= 1
        return data



    def remove_all(self, item: T) -> None:
        travel = self.head
        while travel:
            next_node=travel.next
            if travel.data == item == self.head:
                self.pop_front()
            elif travel.data == item == self.tail:
                self.pop()
            elif travel.data == item:
                travel.next.previous = travel.previous
                travel.previous.next = travel.next
                travel.previous = None
                travel.next = None
            self.count -= 1
        travel = next_node

    def pop(self) -> T:
        if self.tail is None:
            raise IndexError('There is no tail to pop')
        data = self.tail.data
        count -= 1
        if self.head is not self.tail:
            self.tail = self.tail.previous
            self.tail.next = None
            return data
        else:
            self.clear()
            return data
        



    def pop_front(self) -> T:
        if self.head is None:
                raise IndexError('There is no head to pop')
        data = self.head.data
        count -= 1
        if self.head is not self.tail:
            self.head = self.head.nect
            self.head.previous = None
            return data
        else:
            self.head = self.tail = None
            return data
        
        
    @property
    def front(self) -> T:
        if self.head is None:
            raise ValueError('Head is None')
        return self.head.data
    
    @property
    def back(self) -> T:
        if self.tail is None:
            raise ValueError('Tail is None')

        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
       return self.count

    def clear(self) -> None:
        raise NotImplementedError("LinkedList.clear is not implemented")

    def __contains__(self, item: T) -> bool:
        raise NotImplementedError("LinkedList.__contains__ is not implemented")

    def __iter__(self) -> Iterator[T]:
        
        self.travel_node = self.head
        return self
    

    def __next__(self) -> T:
        
        if self.travel_node is None:
            raise StopIteration
        
        data = self.travel_node.data
        self.travel_node = self.travel_node.next

        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
