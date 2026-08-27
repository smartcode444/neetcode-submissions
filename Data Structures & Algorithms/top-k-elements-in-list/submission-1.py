class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        freqElement = list(sorted_freq.keys())
        return freqElement[:k]
