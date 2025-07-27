class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        element_count = Counter(nums)
        
        majority_elements = []
        threshold = len(nums) // 3
        
        # Iterate through the element count to identify majority elements
        for element, count in element_count.items():
            # Check if the element count is greater than the threshold
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements