class Solution:
    def hIndex(self, citations: List[int]) -> int:
        find = 0
        citations = sorted(citations, reverse=True)
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                find = i + 1
            else:
                break
        return find
