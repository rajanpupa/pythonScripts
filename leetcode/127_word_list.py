# 127. Word Ladder
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
from typing import List

# Not Working
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        val = self.ll(beginWord, endWord, wordList, 0)
        if val > 0: return val+1
        return val
    
    def ll(self, beginWord, endWord, wordList, depth)->int:
        if endWord not in wordList: return 0
        if self.chardiff(beginWord, endWord)==1:
            print(depth , "->",beginWord, endWord, 1)
            return 1
        count = 999999999
        tc = 0
        wl = len(wordList)
        for j in range(wl):
            wrd = wordList[j]
            print(depth , "->","trying ", wrd, j)
            if self.chardiff(beginWord, wrd)==1:
                i = wordList.index(wrd)
                wordList.remove( wrd )
                tc =  self.ll( wrd, endWord, wordList, depth+1 )
                if tc < count :
                    print(depth , "->", beginWord, wrd, count, tc)
                    count = tc
                wordList.insert(i,wrd)
            else:
                print(depth , "->","        not ", wrd)
                pass
        if tc == 0: 
            print(depth , "->","ret ",0)
            return 0
        print(depth , "->","ret ",count+1)
        return count + 1

    def chardiff(self, word1, word2)->int:
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return diff

sln = Solution()
# print(sln.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])) # 5
print(sln.ladderLength("hit","cog",["hot","cog","dot","dog","hit","lot","log"])) # 5
# print(sln.ladderLength("hot","dog",["hot","dog"])) # 0
# print(sln.ladderLength("hot","dog",["hot","dog","cog","pot","dot"])) # 3

