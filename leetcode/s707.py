class Node:
    def __init__(self, val):
        self.pre = None
        self.next = None
        self.val = val

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = Node(0)
        self._tail = Node(0)
        self._head.next = self._tail 
        self._tail.pre = self._head
        self._count = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self._count:
            return -1
        tmp_node = self._head.next         # 跳过头结点
        for _ in range(0, index):
            tmp_node = tmp_node.next
        return tmp_node.val 


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        add_node = Node(val)
        add_node.next = self._head.next
        add_node.pre = self._head
        self._head.next.pre = add_node
        self._head.next = add_node
        self._count += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        add_node = Node(val)
        add_node.next = self._tail
        add_node.pre = self._tail.pre
        self._tail.pre.next = add_node
        self._tail.pre = add_node
        self._count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self._count:
            pass
        else:
            tmp_node = self._head.next         # 跳过头结点
            for _ in range(0, index):
                tmp_node = tmp_node.next
            add_node = Node(val)
            add_node.next = tmp_node
            add_node.pre = tmp_node.pre
            tmp_node.pre.next = add_node
            tmp_node.pre = add_node
            self._count += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self._count:
            pass
        else:
            tmp_node = self._head.next
            for _ in range(0, index):
                tmp_node = tmp_node.next
            tmp_node.next.pre = tmp_node.pre
            tmp_node.pre.next = tmp_node.next
            self._count -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

if __name__ == "__main__":
    linkedList = MyLinkedList()
    linkedList.addAtHead(7)
    linkedList.addAtHead(2)
    linkedList.addAtHead(1)
    linkedList.addAtIndex(3,0)
    linkedList.deleteAtIndex(2)
    linkedList.addAtHead(6)
    linkedList.addAtTail(4)
    ret = linkedList.get(4)
    print(ret)
    linkedList.addAtHead(4)
    linkedList.addAtIndex(5,0)   #链表变为1-> 2-> 3
    linkedList.addAtTail(6)
    # ret = linkedList.get(1)            #返回2
    # print(ret)
    # linkedList.deleteAtIndex(1)  #现在链表是1-> 3
    # ret = linkedList.get(1)            #返回3
    # print(ret)
