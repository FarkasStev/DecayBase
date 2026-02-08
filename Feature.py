import random

from config import (
    MAX_FEATURE_COMPLEXITY,
    MAX_FEATURE_LINES,
    MIN_FEATURE_COMPLEXITY,
    MIN_FEATURE_LINES,
)


class Feature:
    def __init__(self):
        self.lines_of_code = random.randint(MIN_FEATURE_LINES, MAX_FEATURE_LINES)
        self.complexity = random.randint(MIN_FEATURE_COMPLEXITY, MAX_FEATURE_COMPLEXITY)
        self.estimated_hours = self.lines_of_code * self.complexity
        self.test_coverage = random.randint(0, 100)
        self.documentation_quality = random.randint(0, 100)
