class Solution:
    def _is_valid_unit(self,unit: List[str]) -> bool:
        nums = [x for x in unit if x != '.']

        return len(set(nums)) == len(nums)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check strings
        for i in range(9):
            if not self._is_valid_unit(board[i]):
                return False
            
        for j in range(9):
            column = [board[i][j] for i in range(9)]
            if not self._is_valid_unit(column):
                return False
            
            for box_row in range(3):
                for box_col in range(3):
                    box_cells = []
                    start_row = box_row * 3
                    start_col = box_col * 3
                    for i in range(3):
                        for j in range(3):
                            box_cells.append(board[start_row + i][start_col + j])
                    if not self._is_valid_unit(box_cells):
                        return False
        return True