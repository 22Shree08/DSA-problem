class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        direction = 1

        for ch in s:
            rows[row] = rows[row] + ch

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row = row + direction

        result = ""
        for r in rows:
            result = result + r

        return result
