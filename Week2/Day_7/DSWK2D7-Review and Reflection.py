def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Inputs must be numbers"
    else:
        return result
    finally:
        print("Done computing")
