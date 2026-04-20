from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #方法一

        # for i in range(n):这是一开始的版本，有几个问题，一是没考虑right递减到小于i，而是移动元素之后我直接i+了，没考虑到假如移动的是不是0？这样会跳过检验
        #     if nums[i] == 0:
        #         for j in range(i,right):
        #             nums[j] = nums[j+1]
        #         nums[right] = 0
        #         right -= 1


        #---------分割线----------#
        #下面是上面直接简单递推的做法的正确写法，但是显然时间复杂度比较高
        # right = len(nums) - 1
        # i = 0
        # while i < right:
        #     if nums[i] == 0:
        #         for j in range(i,right):
        #             nums[j] = nums[j+1]
        #         nums[right] = 0
        #         right -= 1
        #     else:
        #         i +=1

        non_zero = 0  # 指向下一个非零元素应放的位置
        for i in range(len(nums)):
            if nums[i] != 0:
                # 交换当前元素与 non_zero 位置的元素
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1

        


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        [0, 1, 0, 3, 12],
        [0, 0, 1],
        [1, 0, 2, 0, 3],
        [0],
        [1, 2, 3]
    ]

    sol = Solution()

    for nums in test_cases:
        print("原数组:", nums)
        sol.moveZeroes(nums)
        print("移动后:", nums)
        print("-" * 30)