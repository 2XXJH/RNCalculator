import sys
import re

def num2Roman(n):
    if n < 1:
        return None
    roman_numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), 
                      (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), 
                      (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ""
    for value, symbol in roman_numerals:
        while n >= value:
            result += symbol
            n -= value
    return result

def roman2Num(s):
    roman_numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total, prev_value = 0, 0
    for char in reversed(s):
        value = roman_numerals[char]
        total += value if value >= prev_value else -value
        prev_value = value
    return total

def eval_expression(expr):
    expr = re.sub(r'([IVXLCDM]+)', lambda m: str(roman2Num(m.group(1))), expr.replace(" ", ""))
    try:
        result = eval(expr)
        return result if result > 0 else "Result is not representable in Roman numerals."
    except ZeroDivisionError:
        return "Error: Division by zero."
    except Exception:
        return "Error in expression."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py '<expression>'")
        sys.exit(1)

    input_expression = sys.argv[1]
    if re.fullmatch(r'[IVXLCDM]+', input_expression):
        print(num2Roman(roman2Num(input_expression)))
    else:
        result = eval_expression(input_expression)
        if isinstance(result, int):
            print(num2Roman(result))
        else:
            print(result)