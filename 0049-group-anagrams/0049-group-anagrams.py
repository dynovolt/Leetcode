class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited = [False] * len(strs)

        for i in range(len(strs)):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):
                if not visited[j] and self.isAnagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited[j] = True

            result.append(group)

        return result

    def isAnagram(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        return sorted(s1) == sorted(s2)