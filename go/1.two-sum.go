/*
 * [1] Two Sum
 *
 * https://leetcode.com/problems/two-sum/description/
 *
 * algorithms
 * Easy (37.43%)
 * Total Accepted:    818K
 * Total Submissions: 2.2M
 * Testcase Example:  '[3,2,4]\n6'
 *
 * Given an array of integers, return indices of the two numbers such that they
 * add up to a specific target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * 
 * Example:
 * 
 * Given nums = [2, 7, 11, 15], target = 9,
 * 
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * return [0, 1].
 * 
 * 
 */
func twoSum(nums []int, target int) []int {
	r:=[]int{0,0}
	/*for i :=0;i<len(nums);i++{
		for j:=0;j<len(nums);j++{
			if( i== j) {continue}
			if(nums[i] + nums[j] == target){
				r[0],r[1]=i,j
				return r
		}
	}    
}*/ temp:=map[int]int{}
	for i:=0;i<len(nums);i++{
	temp[nums[i]]=i
	}
	for j:=0;j<len(nums);j++{
		
		t1:=target-nums[j]
		t2,ok := temp[t1]
		if(ok){
			if(t2!=j){
			r[0],r[1]=t2,j}
		}
	}
	return r
}
