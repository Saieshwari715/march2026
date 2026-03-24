class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        q=deque()
        q.append((beginWord,1))
        while q:
            word,level=q.popleft()
            if word==endWord:
                return level
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word=word[:i]+ch+word[i+1:]
                    if new_word in wordset:
                        q.append((new_word,level+1))
                        wordset.remove(new_word)
        return 0

        