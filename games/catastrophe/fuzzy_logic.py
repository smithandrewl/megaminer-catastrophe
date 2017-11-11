import math

class FuzzyValue:
    def __init__(self, value = 0.0):
        self.value = value
    def __str__(self):
        return str(self.value)

    def equals(self, other):
        return math.isclose(self.value, other.value, rel_tol = 0.0001)

    def fuzzyAnd(self, other):
        return FuzzyValue(min(self.value, other.value))

    def fuzzyOr(self, other):
        return FuzzyValue(max(self.value, other.value))

    def fuzzyNot(self):
        return FuzzyValue(1.0 - self.value)

def grade_membership(value, low, high):
    """
    A basic grade fuzzy logic membership function.

    :param value: The crisp input you are converting to a fuzzy value
    :param low:   The highest number which would return a membership of 0%
    :param high:  The lowest number which would return a membership of 100%
    :return: The fuzzy membership of a fuzzy set
    """

    if(value <= low):
        return FuzzyValue(0.0)

    if(value >= high):
        return FuzzyValue(1.0)

    return FuzzyValue((value / (high - low)) - (low / (high - low)))


def reverse_grade_membership(value, x0, x1):
    x = value

    if(x <= x0):
        return FuzzyValue(1.0)

    if(x >= x1):
        return FuzzyValue(0.0)

    return FuzzyValue((-x/(x1-x0))+(x1/(x1-x0)))


def triangular_membership(value, left, center, right):
  return FuzzyValue(
      max(
          min(
              (value - left)  / (center - left),
              (right - value) / (right  - center)
          ),
          0.0
      )
  )

def trapezoidal_membership(value, leftBottom, leftTop, rightTop, rightBottom):
  return FuzzyValue(
      max(
          min(
              1.0,
              min(
                  (value - leftBottom)  / (leftTop - leftBottom),
                  (rightBottom - value) / (rightBottom - rightTop)
              )
          ),
          0.0
      )
  )

