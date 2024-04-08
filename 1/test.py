import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

deleteDuplicates = Solution.deleteDuplicates

# Initialize colorama
init(autoreset=True)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head

def compare_lists(head1, head2):
    curr1 = head1
    curr2 = head2

    while curr1 != None and curr2 != None:
        if curr1.val != curr2.val:
            return False
        curr1 = curr1.next
        curr2 = curr2.next

    if curr1 != None or curr2 != None:
        return False

    return True

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return f"Linked List output values: {values}"

class TestExample(unittest.TestCase):


    def run_test(self, input_values, expected_value):
        solution = Solution()
        output = deleteDuplicates(solution, *input_values)

        try:
            print(print_linked_list(output))
            self.assertTrue(compare_lists(output, expected_value))
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        print('Test Case 1:')
        self.run_test([create_linked_list([1,1,2])], create_linked_list([1,2]))
    
    @timeout(2)
    def test_case_2(self):
        print('Test Case 2:')
        self.run_test([create_linked_list([1,1,2,3,3])], create_linked_list([1,2,3]))

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()