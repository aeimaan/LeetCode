class Solution:
    def reorganizeString(self, s: str) -> str:
        fmap = {}

        for c in s:
            fmap[c] = 1 + fmap.get(c, 0)
        
        maxHeap = [[-count, char] for char, count in fmap.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if char == prev:
                if maxHeap:
                    count2, char2 = heapq.heappop(maxHeap)
                else:
                    return ""
                res += char2
                prev = char2
                count2 += 1
                if count2 != 0: heapq.heappush(maxHeap, [count2, char2])
                heapq.heappush(maxHeap, [count, char])
            else:
                res += char
                count += 1
                if count != 0: heapq.heappush(maxHeap, [count, char])
                prev = char
        return res



