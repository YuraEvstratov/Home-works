def safe_calculate(a, b, operation):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        else:
             raise ValueError("Unsupported operation")
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
         return
    except ValueError:
        return "Unsupported operation"

print(safe_calculate(10, 5, "divide"))    
print(safe_calculate(10, 0, "divide"))   
print(safe_calculate(10, "5", "add"))     
print(safe_calculate(10, 5, "mod"))  
