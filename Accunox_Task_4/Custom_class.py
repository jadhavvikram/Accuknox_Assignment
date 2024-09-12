class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Returning a generator that yields the length and width in the required format
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rect = Rectangle(5, 10)

# Iterating over the instance
for attribute in rect:
    print(attribute)
