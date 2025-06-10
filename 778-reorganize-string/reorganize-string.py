class Solution:
    def reorganizeString(self, s: str) -> str:
        fmap = {}

        for c in s:
            fmap[c] = fmap.get(c, 0) + 1
        
        max_heap = [[-count, char] for char, count in fmap.items()]
        heapq.heapify(max_heap)

        prev = None
        res = ""

        while max_heap:
            count, cur = heapq.heappop(max_heap)
            if prev != cur:
                res += cur
                prev = cur
                count += 1
                if count != 0: heapq.heappush(max_heap, [count, cur])
            else:
                count2, next_char = 0, None
                if max_heap:
                    count2, next_char = heapq.heappop(max_heap)
                    res += next_char
                    prev = next_char
                    count2 += 1
                    if count2 != 0: heapq.heappush(max_heap, [count2, next_char])
                    heapq.heappush(max_heap, [count, cur])
                else:
                    return ""
        return res