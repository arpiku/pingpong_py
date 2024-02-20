import math

class Vector:
    def __init__(self, **components):
        self.components = components

    def __getattr__(self, name):
        return self.components.get(name, 0)

    def __setattr__(self, name, value):
        if name == 'components':
            super().__setattr__(name, value)
        else:
            self.components[name] = value

    def __add__(self, other):
        result = {}
        for key in set(self.components.keys()) | set(other.components.keys()):
            result[key] = self.components.get(key, 0) + other.components.get(key, 0)
        return Vector(**result)

    def __sub__(self, other):
        result = {}
        for key in set(self.components.keys()) | set(other.components.keys()):
            result[key] = self.components.get(key, 0) - other.components.get(key, 0)
        return Vector(**result)

    def __mul__(self, scalar):
        result = {}
        for key, value in self.components.items():
            result[key] = value * scalar
        return Vector(**result)

    def __truediv__(self, scalar):
        result = {}
        for key, value in self.components.items():
            result[key] = value / scalar
        return Vector(**result)

    def __str__(self):
        components_str = ", ".join(f"{key}={value}" for key, value in self.components.items())
        return f"Vector({components_str})"

    def magnitude(self):
        return math.sqrt(sum(component ** 2 for component in self.components.values()))

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return self / mag
        else:
            return Vector(**{key: 0 for key in self.components.keys()})


