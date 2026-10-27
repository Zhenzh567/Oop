class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, index):
        return self.rows[index]

    def __contains__(self, value):
        for row in self.rows:
            if value in row:
                return True
        return False
