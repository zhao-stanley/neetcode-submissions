class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            num_ones = 0
            binary_num = bin(i)[2:]
            for dig in binary_num:
                num_ones += int(dig)
            output.append(num_ones)
        return output