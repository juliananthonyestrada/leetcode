class Table:
    def __init__(self, name, col_count):
        self.name = name
        self.col_count = col_count
        self.idx = 1

        # row_idx -> row
        self.rows = {}
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if not isinstance(other, Table):
            return False
        return self.name == other.name

class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        for name, col_count in zip(names, columns):
            self.tables[name] = Table(name, col_count)

    def ins(self, name: str, row: List[str]) -> bool:
        # table doesn't exist
        if name not in self.tables or self.tables[name].col_count != len(row):
            return False
        # table exists - insert row to corresponding table
        else:
            curr_table = self.tables[name]
            curr_table.rows[curr_table.idx] = row
            curr_table.idx += 1
            return True
        
    def rmv(self, name: str, rowId: int) -> None:
        if name in self.tables:
            self.tables[name].rows.pop(rowId, None)
        
    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables:
            return "<null>"
        
        curr_table = self.tables[name]
        row = curr_table.rows.get(rowId)

        if row is None or columnId < 1 or columnId > curr_table.col_count:
            return "<null>"
            
        return curr_table.rows[rowId][columnId-1]

    def exp(self, name: str) -> List[str]:
        if name not in self.tables or len(self.tables[name].rows) == 0:
            return []
        else:
            remaining_rows = []
            curr_table = self.tables[name]
            for idx, row in curr_table.rows.items():
                remaining_rows.append(f"{idx},{','.join(row)}")
            return remaining_rows

