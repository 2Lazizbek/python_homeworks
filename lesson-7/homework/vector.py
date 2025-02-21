import math  # Import math module for mathematical operations (specifically for sqrt)

class Vector:
    def __init__(self, *args):
        # Initialize a vector with any number of dimensions
        self.coordinates = tuple(args)  # Store as tuple for immutability

    def __str__(self):
        # Return a human-readable representation of the vector
        return f"Vector{self.coordinates}"  # Display vector in a readable format

    def __len__(self):
        # Return the number of dimensions of the vector
        return len(self.coordinates)  # Length is the number of elements in the vector

    def __add__(self, other):
        # Add two vectors (element-wise)
        if len(self) != len(other):  # Check if vectors have the same number of dimensions
            raise ValueError("Cannot add vectors of different dimensions.")
        return Vector(*(a + b for a, b in zip(self.coordinates, other.coordinates)))  
        # Element-wise addition using zip()

    def __sub__(self, other):
        # Subtract one vector from another (element-wise)
        if len(self) != len(other):  # Check if vectors have the same number of dimensions
            raise ValueError("Cannot subtract vectors of different dimensions.")
        return Vector(*(a - b for a, b in zip(self.coordinates, other.coordinates)))  
        # Element-wise subtraction using zip()

    def __mul__(self, other):
        # Handle scalar multiplication and dot product
        if isinstance(other, (int, float)):  # If multiplying by a scalar (number)
            return Vector(*(a * other for a in self.coordinates))  # Multiply each element by scalar
        elif isinstance(other, Vector):  # If multiplying by another vector (dot product)
            if len(self) != len(other):  # Check if vectors have the same dimensions
                raise ValueError("Cannot compute dot product of vectors with different dimensions.")
            return sum(a * b for a, b in zip(self.coordinates, other.coordinates))  
            # Compute dot product (sum of element-wise multiplication)
        else:
            raise TypeError("Multiplication is only supported with a scalar or another Vector.")

    def magnitude(self):
        # Return the magnitude (length) of the vector
        return math.sqrt(sum(a ** 2 for a in self.coordinates))  
        # Return square root of the sum of squares of all elements

    def normalize(self):
        # Return the unit vector in the same direction
        mag = self.magnitude()  # Get magnitude of the vector
        if mag == 0:  # Prevent division by zero
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.coordinates))  
        # Divide each component by magnitude to get unit vector