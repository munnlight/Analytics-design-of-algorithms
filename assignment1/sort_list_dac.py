class Solution(object):
    def sortList(self, head):
        to_list = []
        temp = head

        while head != None:
            to_list.append(head.val)
            head = head.next
        
        to_list.sort()

        print(to_list)
        head = temp
        for i in to_list:
            temp.val = i
            temp = temp.next
        
        return head



li = [1, 2, 3, 4, 5, 100]

li.remove(100)
print(li)