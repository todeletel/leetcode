class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # corner case
        # 数量不匹配  len(pattern) != len(s.split(' '))
        # 

        # pattern 含义 单词到 26个小写字母的一一映射 也就是说最多 输入只能有26类单词

        # 如何分配 字母到单词的映射 遍历pattern 字母 如果第一次出现就分配给 当前位置的字母
        # 如果非首次出现 说明以前分配了这种映射  映射中的字母是否和当前对应相通 如果发现不同返回失败
        # 迭代结束返回 成功

        # 定义字母-> 单词  单词-> 字母 两个变量
        char_to_word = {}
        word_to_char = {}
        
        word_list = s.split(' ')

        if len(word_list) != len(pattern):
            return False
        
        for index, char in enumerate(pattern):
            
            # 返回false 情况
            # 1. 字母到单词映射存在  并且 != 当前单词 返回false
            # 2. 字母到单词映射不存在 但是该单词存在映射到其他字母的关系 返回 false

            if char_to_word.get(char) is not None:  
                if char_to_word[char] != word_list[index]:
                    return False
            else:
                if word_to_char.get(word_list[index]):
                    return False
                char_to_word[char] = word_list[index]
                word_to_char[word_list[index]] = char
        return True
            
            



