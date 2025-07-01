class Solution(object):
    def sortEvenOdd(self, nums):
        even=[]
        odd=[]
        a=len(nums)
        for i in range(a):
            if(i%2==0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort()
        nums=[]
        b=0
        c=-1
        for i in range(a):
            if(i%2==0):
                nums.append(even[b])
                b=b+1
            else:
                nums.append(odd[c])
                c=c-1
        return nums