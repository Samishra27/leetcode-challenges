""" QUESTIONS: 
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  

1. 1 is typically treated as an ugly number.
2. n does not exceed 1690.
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # nums=[]
        # for i in range(int(log(1690,5))):
        #     for j in range(int(log(1690,3))):
        #         for k in range(int(log(1690,2))):
        #             nums.append((5**i)*(3**j)*(2**k))
        # nums.sort()
        # print(len(nums))
        # print(nums)
        
        nums=[1]
        idx_2, idx_3, idx_5 = 0, 0, 0
        for i in range(n-1):
            next2=nums[idx_2]*2
            next3=nums[idx_3]*3
            next5=nums[idx_5]*5
            next=min(next2,next3,next5)
            nums.append(next)
            if next==next2:
                idx_2+=1
            if next ==next3:
                idx_3+=1
            if next==next5:
                idx_5+=1
        return nums[-1]

