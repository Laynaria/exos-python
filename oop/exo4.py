# Exo 1:
def calculator(a: float | int, b: float | int, operator:str ) -> int | float:
    try:
        if isinstance(a, float | int) and isinstance(b, float | int) and isinstance(operator, str):
            match operator:
                case "+":
                    return a + b
                case "-":
                    return a - b
                case "*":
                    return a * b
                case "/":
                    return a / b
                case _ :
                    print(f"Please only use +, -, * or / operator, you typed: {operator}")
        else:
            print(f"Please enter numbers, you typed {a} and {b}")

    
    except ZeroDivisionError :
        print("You cant divide by zero!")
    except Exception:
        print("General Error")

print(calculator(12, 5, "+"))
print(calculator(12, 5, "-"))
print(calculator(12, 5, "*"))
print(calculator(12, 5, "/"))
print(calculator(12, 0, "/"))
print(calculator("a", 5, "/"))
print(calculator(12, "b", "/"))
print(calculator(12, 5, "a"))

# Exo 2:
class NegativeValueException(Exception):
    def __init__(self, message="Value can't be negative."):
        super().__init__(message)

def verify_value(value: int | float) -> None:
    if value < 0:
        raise NegativeValueException()
    else:
        print(value)

try:
    verify_value(4)
    verify_value(-1)
except NegativeValueException as e:
    print(e)