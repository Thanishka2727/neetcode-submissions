from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        worddict = set(wordList)

        if endWord not in worddict:
            return 0
        q = deque([(beginWord, 1)])

        visited = set(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyxz":
                    newword = word[:i] + ch + word[i+1:]
                    if newword in worddict and newword not in visited:

                        q.append((newword,steps+1))
                        visited.add(newword)
        return 0
                            
        