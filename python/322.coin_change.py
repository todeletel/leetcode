class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf_num = 99999999 # > 10 ** 4

        # 1. 状态确定  f(amount) = min([f(amount-coins[i])+1 for i in coins])
        # 2. 转移方程  f[amount] = min([f[amount-coins[i]]+1 for i in coins])
        # 3. 初始条件和边界情况  f[0] = 0
        f = [inf_num] * (amount+1)
        f[0] = 0
        for money in range(1, amount+1):
            min_cnt = inf_num
            for coin in coins:
                if (sub_money := money - coin) >= 0:
                    temp_min_cnt = f[sub_money] + 1
                    if temp_min_cnt < min_cnt:
                        min_cnt = temp_min_cnt
            f[money] = min_cnt
        
        return f[amount] if f[amount] != inf_num else -1
                    
