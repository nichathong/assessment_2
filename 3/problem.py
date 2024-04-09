class Solution:
    #base case -> check if the len are the same
    def letterCasePermutation(self, s):

        def _backtrack(idx, current_permutation):
            if idx == len(s):
                result.append(current_permutation)
                return 
            #need to check if character is alphabet?
            if s[idx].isalpha():
                _backtrack(idx+1, current_permutation + s[idx].upper())
            else:
                _backtrack(idx+1, current_permutation + s[idx])

        result = []
        _backtrack(0, "")
        return result

