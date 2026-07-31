from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

head = ListNode(1, ListNode(2, ListNode(3,ListNode(4,ListNode(5)))))
#head = ListNode(1, ListNode(2, ListNode(3,ListNode(4))))
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        current = second;previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        dummy = ListNode()
        current_fin = dummy
        temp = 1
        slow = head;
        while slow and previous:
            if temp == 1:
                current_fin.next = slow
                slow = slow.next
                temp -= 1
            else:
                current_fin.next = previous
                previous = previous.next
                temp += 1
            current_fin = current_fin.next
        current_fin.next = slow if slow else previous
        return 
print(Solution().reorderList(head))
