from typing import List


class ListNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SList(object):
    def __init__(self):
        self.head = ListNode(None)
        self.size = 0
    
    def listSize(self):
        return self.size
    
    def is_empty(self):
        if self.size != 0: # if not 0, it's not empty
            return False
        else:
             return True

    def selectNode(self, index):
        if index >= self.size:
            print("Index Error")
            return None
        
        if index ==0:
            return self.head
        else:
            target = self.head
            for _ in range(index):
                target = target.next
            return target
    
    def printNodes(self, node:ListNode):
        current_node = node
        while current_node is not None:
            print(current_node.data, end= ' ')
            current_node = current_node.next
    
    def appendLeft(self, value):
        if self.is_empty():
            self.head = ListNode(value)
        else:
            self.head = ListNode(value, self.head)
        self.size += 1
    
    def insert(self, value, index):
        if self.is_empty():
            self.head= ListNode(value)
            self.size += 1
        elif index == 0: # if index is 0, put to the first node
            self.head = ListNode(value, self.head) # set the head
            self.size += 1 
        else:
            target = self.selectNode(index-1)
            if target == None:
                return
            
            new_node = ListNode(value)
            tmp = target.next # save target's next node for a while
            target.next = new_node # insert new node to the target's next node
            new_node.next = tmp
            self.size += 1
            


if __name__ == "__main__":
    head_node = ListNode(1)
    head_node.next = ListNode(5)
    head_node.next.next = ListNode(3)
    head_node.next.next.next= ListNode(4)

    my_list = SList(head_node)
    my_list.printNodes(head_node)
    my_list.insert('8', 2)
    print("------")
    my_list.printNodes(my_list)