"""
This is the solution for the `2.Add Two Numbers LeetCode Problem`
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def transform_into_node(value: int) -> ListNode:
    node = ListNode()
    if (value // 10 == 0):
        node.val = value
        return node
    else:
        res = value % 10
        value = value // 10
        node.val = res
        node.next = ListNode(res, transform_into_node(value))
        return node


def normalize(n1: int, mult: int) -> int:
    return n1 * (10**mult)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        numOne: int = 0
        numTwo: int = 0
        x = 0
        while l1:
            numOne += normalize(l1.val, x)
            x += 1
            l1 = l1.next
        x = 0
        while l2:
            numTwo += normalize(l2.val, x)
            x += 1
            l2 = l2.next
        result: int = numOne + numTwo
        node = transform_into_node(result)
        return node
