import sys

def romanToNum(roman):
    '''Assigns Roman Numerals to Numerical values.
    '''

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000

        }
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_values.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total if total > 0 else None

def num2Roman(n):
    ''''converts numerical value to Roman Numeral.
    '''
    
    if n < 1 or n > 3999:
        return None
    
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    roman_numeral = ""
    for i in range(len(num)):
        while n >= num[i]:
            roman_numeral += sym[i]
            n -= num[i]

    return roman_numeral

def evaluate_expression(expression):
    '''Returns invalid expression when value is not positive
    '''
    try:
        result = eval(expression)
        if result <= 0:
            raise ValueError("Result must be a positive integer.")
        return result
    except (SyntaxError, NameError, ZeroDivisionError):
        return None
    except ValueError as e:
        print(e)
        return None


if len(sys.argv) < 2:
    print("Usage: python main.py <roman_expression>")
    sys.exit(1)

input_expression = ' '.join(sys.argv[1:])


tokens = input_expression.split()
for i, token in enumerate(tokens):
    if all(c in "IVXLCDM" for c in token.upper()):  
        num_value = romanToNum(token.upper())
        if num_value is not None:
            tokens[i] = str(num_value)  


expression_to_evaluate = ' '.join(tokens)


if expression_to_evaluate.count('(') != expression_to_evaluate.count(')'):
    print("Invalid input or arithmetic expression: unbalanced parentheses.")
else:
    
    result = evaluate_expression(expression_to_evaluate)

    if result is None:
        print("Invalid input or arithmetic expression.")
    elif result == 0:
        print("0 does not exist in Roman numerals.")
    elif result > 3999:
        print("You're going to need a bigger calculator.")
    elif isinstance(result, float):
        print("There is no concept of a fractional number in Roman numerals.")
    else:
        #Print
        print(f"Result of the expression: {result}")
        print(f"Roman numeral: {num2Roman(result)}")