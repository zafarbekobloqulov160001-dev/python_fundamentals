"""
Python Lambda, Map, and Filter Project

This script demonstrates how lambda functions,
map(), and filter() work in Python.

The program processes student scores.
"""

# List of student scores
scores = [45, 78, 92, 60, 55, 88, 30]

print("Original scores:", scores)

# -----------------------------
# Using map() with lambda
# Convert scores to percentage bonus (+5 points)
# -----------------------------

bonus_scores = list(map(lambda x: x + 5, scores))

print("\nScores after bonus:", bonus_scores)

# -----------------------------
# Using filter() with lambda
# Keep only passing scores (>= 60)
# -----------------------------

passing_scores = list(filter(lambda x: x >= 60, bonus_scores))

print("Passing scores:", passing_scores)

# -----------------------------
# Calculate average score
# -----------------------------

average_score = sum(passing_scores) / len(passing_scores)

print("\nAverage passing score:", round(average_score, 2))