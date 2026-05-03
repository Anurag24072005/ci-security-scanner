def greet(name):
    return f"Hello, {name}"

def run_code(user_input):
    # Safe function (no eval)
    return str(user_input)

print(greet("Anurag"))