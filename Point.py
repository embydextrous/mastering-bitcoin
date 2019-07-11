class Point:

    def __init__(self, x, y, a, b):
        self.a, self.b, self.x, self.y = a, b, x, y

        # Skip checking for infinity point
        if self.x is None and self.y is None:
            return

        # Check if the point actually lies on the curve
        if self.y ** 2 != self.x ** 3 + a * x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))

    # Returns true if coordinates (x, y) and curve (a, b) are same
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        # this should be the inverse of the == operator
        return not (self == other)

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        else:
            return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format
            (self, other))

        # self.x is None implies self is point of infinity or additive identity
        # So, we return other.
        if self.x is None:
            return other

        # other.x is None implies other is point of infinity or additive identity
        # So, we return self.
        if other.x is None:
            return self

        # self.x == other.x and self.y != other.y implies point lies on same vertical line
        # Or, self and other are additive insverses of each other. So, we return infinity.
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)

        # When the line joining the points is not vertical
        if self.x != other.x:
            m = (other.y - self.y) / (other.x - self.x)      # Calculate Slope
            x = m ** 2 - self.x - other.x
            y = m * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

        # When two points are same, the line is tangent to the curve
        if self == other:
            # Special case when the tangent is vertical
            #if self.y == 0 * self.x:
            #    return self.__class__(None, None, self.a, self.b)
            m = (self.x ** 2 + self.x ** 2 + self.x ** 2 + self.a) / (self.y + self.y)  # Calculate slope
            x = m ** 2 - self.x - self.x
            y = m * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)


    def __rmul__(self, coefficient):
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
                current += current
                coef >>= 1
        return result
