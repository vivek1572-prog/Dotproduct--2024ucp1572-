# Vector Dot-Product Program in Python

def dot_product(v1, v2):
    if len(v1) != len(v2):
        return 0
    return sum(x * y for x, y in zip(v1, v2))

if __name__ == "__main__":
    print("Dot Product Code v1")
    # Example vector calculation
    vector_a = [1, 2, 3]
    vector_b = [4, 5, 6]
    result = dot_product(vector_a, vector_b)
    print(f"The dot product is: {result}")

