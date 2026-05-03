# Secure function
def greet(name):
    return f"Hello, {name}"

# ❌ Insecure function (for testing)
def run_code(user_input):
    # eval is dangerous
    return str(user_input)

print(greet("Anurag"))