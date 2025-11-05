square = lambda x: x * x
print(square(5))

def num(a, b):
    result = a + b
    print(result)

num(1, 5)


def num(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        print("Error: Both inputs must be numbers!")
    finally:
        print("Execution completed.")

# ✅ Valid input
print("result:", num(10, 5))

# # ❌ Invalid input
# print("Result:", num(10, "five"))
