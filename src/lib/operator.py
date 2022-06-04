class BasicArithmeticOperator:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2    
    
    def add(self):
        return self.val1 + self.val2
    
    def sub(self):
        return self.val1 - self.val2

    def mul(self):
        return self.val1 * self.val2
    
    def dev(self):
        if self.val2 == 0:
            return "Zero division is not possible."
        else:
            return self.val1 / self.val2
