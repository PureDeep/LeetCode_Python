#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (42.61%)
# Total Accepted:    1.6M
# Total Submissions: 3.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
class Solution:
    def twoSum(self, nums, target):
        #创建一个空词典
        index_map = {}

        for i in range(len(nums)):
            if nums[i] in index_map:    #这里是判断nums[i]是否存在于index_map的索引（index）部分
                return [index_map[nums[i]], i]

            #
            index_map[target - nums[i]] = i
