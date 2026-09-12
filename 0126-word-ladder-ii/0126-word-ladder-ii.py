class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordList:
            return []
        graph=defaultdict(list)
        beginset={beginWord}
        found=False
        while beginset and not found:
            nxt=set()
            for word in beginset:
                for i in range(len(word)):
                    for ch in string.ascii_lowercase:
                        if ch==word[i]:
                            continue
                        new=word[:i]+ch+word[i+1:]
                        if new in wordset:
                            graph[new].append(word)
                            nxt.add(new)
                            if new==endWord:
                                found=True
            wordset-=nxt
            beginset=nxt
        ans=[]
        path=[endWord]
        def dfs(word):
            if word==beginWord:
                ans.append(path[::-1])
                return
            for parent in graph[word]:
                path.append(parent)
                dfs(parent)
                path.pop()
        if found:
            dfs(endWord)
        return ans