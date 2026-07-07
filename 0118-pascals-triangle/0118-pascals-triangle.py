class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            a = [1] * (i +1)
            for j in range(1, i):
                a[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(a)
        return triangle

        