# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #方法一：不加思索的初学者
        # rel1 = reverseListnode(l1)
        # rel2 = reverseListnode(l2)

        # head = ListNode(0)
        # current = head
        # cin = 0

        # # 两个链表都有值的情况
        # while rel1 and rel2:
        #     sum_val = rel1.val + rel2.val + cin
        #     new_node = ListNode(sum_val % 10)
        #     current.next = new_node
        #     current = current.next
        #     cin = sum_val // 10  

        #     rel1 = rel1.next
        #     rel2 = rel2.next

        # # 只剩 l1
        # while rel1:
        #     sum_val = rel1.val + cin
        #     new_node = ListNode(sum_val % 10)
        #     current.next = new_node
        #     current = current.next
        #     cin = sum_val // 10
        #     rel1 = rel1.next

        # # 只剩 l2
        # while rel2:
        #     sum_val = rel2.val + cin
        #     new_node = ListNode(sum_val % 10)
        #     current.next = new_node
        #     current = current.next
        #     cin = sum_val // 10
        #     rel2 = rel2.next

        # # 最后还有进位
        # if cin:
        #     current.next = ListNode(1)

        # l3 = reverseListnode(head.next)
        # return l3


        #方法二：初学者代码语法优化
        # r1 = reverseListnode(l1)
        # r2 = reverseListnode(l2)

        # head = ListNode(0)
        # current = head
        # carry = 0

        # while r1 or r2 or carry:
        #     v1 = r1.val if r1 else 0
        #     v2 = r2.val if r2 else 0

        #     sum_val = v1 + v2 + carry
        #     carry = sum_val // 10
        #     current.next = ListNode(sum_val % 10)
            
        #     current = current.next

        #     r1 = r1.next if r1 else None
        #     r2 = r2.next if r2 else None
        
        # return reverseListnode(head.next)

        #栈操作（先进后出性质和本题关系很大）
        s1, s2 = [], []

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        ans = None
        while s1 or s2 or carry:
            v1 = 0 if not s1 else s1.pop()
            v2 = 0 if not s2 else s2.pop()
            val = v1 + v2 + carry

            carry = val // 10
            current = ListNode(val % 10)
            current.next = ans
            ans = current
        
        return ans
def reverseListnode(l: ListNode) -> ListNode:
    cur = l
    prev = None
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev

def create_list(arr):
    dummy = ListNode()
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def print_list(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

if __name__ == "__main__":
    l1 = create_list([1,2,3,2])  # 1→2→3→2 代表数字 1232
    l2 = create_list([3,4,5])    # 3→4→5 代表数字 345

    print("l1：", end="")
    print_list(l1)
    print("l2：", end="")
    print_list(l2)

    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)

    print("结果：", end="")
    print_list(res)