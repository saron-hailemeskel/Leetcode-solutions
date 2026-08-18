class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        if k > 0:
            l = 1
            r = k
        else:
            l = n + k
            r = n - 1

        curr_sum = 0

        for i in range(l, r + 1):
            curr_sum += code[i]

        for i in range(n):
            result[i] = curr_sum

            curr_sum -= code[l % n]
            l += 1

            r += 1
            curr_sum += code[r % n]

        return result