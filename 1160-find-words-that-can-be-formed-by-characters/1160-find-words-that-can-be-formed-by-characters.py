from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_count = Counter(chars)
        total_length = 0
        
        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= chars_count[c] for c in word_count):
                total_length += len(word)
        
        return total_length

# Example test cases
solution = Solution()
words1 = ["cat","bt","hat","tree"]
chars1 = "atach"
print(solution.countCharacters(words1, chars1))  # Output: 6

words2 = ["hello","world","leetcode"]
chars2 = "welldonehoneyr"
print(solution.countCharacters(words2, chars2))  # Output: 10
