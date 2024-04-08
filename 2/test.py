import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution
from collections import deque

findNearestRightNode = Solution.findNearestRightNode

# Initialize colorama
init(autoreset=True)

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def array_to_tree(arr):
    if not arr:
        return
    node = root = TreeNode(arr[0])
    queue = deque()
    for i, value in enumerate(arr[1:]):
        if value is not None:  # A node to create?
            queue.append(TreeNode(value))
            if i % 2:  # At odd iterations we attach it as a right child
                node.right = queue[-1]
            else:  # At even iterations we attach it as a left child
                node.left = queue[-1]
        if i % 2 and queue:  # After odd iterations we grab a next parent
            node = queue.popleft()

    return root

def find_node(root, value):
    if not root:
        return None
    
    if root.val == value:
        return root
    
    left_result = find_node(root.left, value)
    if left_result:
        return left_result
    
    right_result = find_node(root.right, value)
    if right_result:
        return right_result

class TestExample(unittest.TestCase):


    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(findNearestRightNode(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        print('Test Case 1:')
        tree = array_to_tree([1,2,3,None,4,5,6])
        self.run_test([tree, find_node(tree, 4)], find_node(tree, 5))
    
    @timeout(2)
    def test_case_2(self):
        print('Test Case 2:')
        tree = array_to_tree([3,None,4,2])
        self.run_test([tree, find_node(tree, 2)], None)
    

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()