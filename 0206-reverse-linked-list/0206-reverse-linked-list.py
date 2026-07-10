# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # 이전 노드가 없으므로 None

        current = head  # 연결리스트의 첫 노드인 head를 가리킴

        while current:  # 반복
            next_node = current.next

            current.next = prev # prev  current  (next_node=)current.next
            prev = current
            current = next_node
        return prev