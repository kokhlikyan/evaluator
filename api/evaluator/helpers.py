import sympy
from sympy import parse_expr, simplify
from sympy.core.numbers import ComplexInfinity, Float


def evaluate_expression(expression):
    try:
        parsed_expression = parse_expr(expression)
        simplified_expression = simplify(parsed_expression)
        result = simplified_expression.evalf()
        if isinstance(result, ComplexInfinity):
            raise ZeroDivisionError("Division by zero")
        if isinstance(result, Float):
            return float(result)
        return result
    except Exception as e:
        raise Exception(e)
    except ZeroDivisionError as e:
        raise ZeroDivisionError(e)

