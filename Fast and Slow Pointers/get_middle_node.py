from linked_list import LinkedList

# The code in "linked_list.py" can be used to create a linked list out of a list. 
# The code in "linked_list_traversal.py" can be used to traverse the linked list.
# The code in "linked_list_reversal.py" can be used to reverse the linked list.

def get_middle_node(head):

    # Replace this placeholder return statement with your code
    if head is None:
        return False
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == Null:
            return slow
        

    # return head

def main():

    input = [1,2,3,4,5]

    input_linked_list = LinkedList()
    input_linked_list.create_linked_list(input)

    get_middle = get_middle_node(input_linked_list.head)

    print(get_middle)
if __name__ == "__main__":
    main()