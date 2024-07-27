import numpy as np

def input_vector():
    vector = list(map(float, input("Enter the elements of the vector, separating numbers with spaces: ").split()))
    return np.array(vector)

def add_vectors(v1, v2):
    return v1 + v2

def subtract_vectors(v1, v2):
    return v1 - v2

def dot_product(v1, v2):
    return np.dot(v1, v2)

def cross_product(v1, v2):
    return np.cross(v1, v2)

def vector_magnitude(v):
    return np.linalg.norm(v)

def main():
    print("Enter the first vector:")
    v1 = input_vector()
    print("Enter the second vector:")
    v2 = input_vector()

    print("\nVector 1:", v1)
    print("Vector 2:", v2)

    print("\nVector addition (v1 + v2):", add_vectors(v1, v2))
    print("Vector subtraction (v1 - v2):", subtract_vectors(v1, v2))
    print("Dot product (v1 . v2):", dot_product(v1, v2))
    if len(v1) == 3 and len(v2) == 3:
        print("Cross product (v1 x v2):", cross_product(v1, v2))
    else:
        print("Cross product is defined only for 3-dimensional vectors.")
    print("Magnitude of vector 1 (|v1|):", vector_magnitude(v1))
    print("Magnitude of vector 2 (|v2|):", vector_magnitude(v2))

if name == "__main__":
    main()
