class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordset:
            return []
        
        graph=defaultdict(list)
        found=False
        q=deque()
        q.append(beginWord)
        while q and not found:
            level=set()
            for _ in range(len(q)):
                word=q.popleft()
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new_word=word[:i]+ch+word[i+1:]
                        if new_word in wordset:
                            if new_word not in level:
                                q.append(new_word)
                                level.add(new_word)
                            
                            graph[new_word].append(word)
                           
                            
                            if new_word==endWord:
                                found=True
                            
            wordset-=level
        res=[]
        def dfs(path,w):
            if w==beginWord:
                res.append(path[::-1])
                return 
            for nei in graph[w]:
                dfs(path+[nei],nei)


        dfs([endWord],endWord)
        return res


        