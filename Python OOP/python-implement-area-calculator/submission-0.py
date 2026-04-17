import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width=None):
        if width is None:
            result = math.pi * (length * length)
            rounded_result = round(result, 2)
            return rounded_result
        else:
            area = length * width
            return area

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))