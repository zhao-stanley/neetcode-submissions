class Node:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq

class Solution:

    def heapify(self, index, items: List[Node]):
        size = len(items)
        largest_index = index
        
        while True:
            left_index = 2 * largest_index + 1
            right_index = 2 * largest_index + 2

            if left_index < size and items[left_index].freq > items[largest_index].freq:
                largest_index = left_index
            if right_index < size and items[right_index].freq > items[largest_index].freq:
                largest_index = right_index
            if largest_index != index:
                items[index], items[largest_index] = items[largest_index], items[index]
                index = largest_index
            else:
                break

        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        pq = []
        output = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num, freq in freq.items():
            node = Node(num, freq)
            pq.append(node)

        start_index = math.floor(len(pq) / 2) - 1

        for i in range(start_index, -1, -1):
            self.heapify(i, pq)

        j = 0
        for i in range(k):
            output.append(pq[0].val)
            pq[0] = pq[-1]
            pq.pop()
            self.heapify(0, pq)
        return output




        