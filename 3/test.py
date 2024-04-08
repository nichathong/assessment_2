import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

letterCasePermutation = Solution.letterCasePermutation

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(sorted(letterCasePermutation(solution, *input_values)), sorted(expected_value))
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        print('Test Case 1:')
        self.run_test(["a1b2"], ["a1b2","a1B2","A1b2","A1B2"])
    
    @timeout(2)
    def test_case_2(self):
        print('Test Case 2:')
        self.run_test(["3z4"], ["3z4","3Z4"])

    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()