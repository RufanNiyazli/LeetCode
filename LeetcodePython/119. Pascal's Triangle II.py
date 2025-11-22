class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1], [1, 1]]

        for i in range(2,rowIndex ):
            new_list = [1]
            for j in range(i - 1):
                new_element = rows[i][j] + rows[i][j + 1]
            new_list.append(1)
            rows.append(new_list)
        return rows[-1]    
