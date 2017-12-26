# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue

class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0
        
    def put(self, item):
        PriorityQueue.put(self, (item[0], self.counter, item[1]))
        self.counter += 1
        
    def get(self):
        return PriorityQueue.get(self)

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        curr = dummy
        q = MyPriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[2]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next
