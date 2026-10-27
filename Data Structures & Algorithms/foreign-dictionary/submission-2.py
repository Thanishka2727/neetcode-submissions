from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        chars = set("".join(words))

        adj = {ch: set() for ch in chars}

        indegree = {ch: 0 for ch in chars}

        #graph build 

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            found = False

            for i in range(min(len(w1), len(w2))):

                if w1[i] != w2[i]:

                    if w2[i] not in adj[w1[i]]:
                        adj[w1[i]].add(w2[i])
                        indegree[w2[i]] += 1

                    found = True
                    break
            if not found and len(w1) > len(w2):
                return ""
        q = deque()

        for ch in chars:
            if indegree[ch] == 0:
                q.append(ch)
        ans =[]
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(ans) == len(chars):
            return "".join(ans)
        else:
            return ""
