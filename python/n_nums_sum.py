"""
根据认知心理学的工作空间理论,解决问题的时候将问题拆分问子问题 
有助于复杂问题的思考. 今后解题尝试用这种思考方式 来提高解决复杂问题的能力
"""

# 1.两数字之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1.可能的 corner case
        # 1. 结果不存在  题目假定有切只有一个答案 
        # 2. 数组长度小于2  题目不要求处理这种情况

        # 1.暴力的解法
        # 对每个数字遍历数组中的其他元素 时间复杂度为 O(n * (n-1))  不够优雅 尝试以空间换时间

        # 2. hash 法  将数组中的每个元素映射到hash表中  
        # 使得判断一个元素存不存在的复杂度变为O(1) 那么整个算法时间复杂度就变为O(n+n) 

        # 解法
        
        # 暂存元素
        nums_hash = {}
        for index, num_value in enumerate(nums):
            nums_hash[num_value] = index
        
        for index, num_value in enumerate(nums):
            need_num = target - num_value
            if nums_hash.get(need_num, None) is not None:
                # 同一元素不能用两次
                if nums_hash[need_num] != index:
                    return [index, nums_hash[need_num]]
