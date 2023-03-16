from enum import Enum


class Rating(Enum):

    TERRIBLE = (0.00, 0.50)
    BAD = (0.50, 0.70)
    NORMAL = (0.70, 0.80)
    GOOD = (0.80, 0.90)
    VERY_GOOD = (0.90, 0.95)
    EXCELENT = (0.95, 1.00)
