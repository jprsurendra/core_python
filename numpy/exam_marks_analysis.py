import numpy as np

marks = np.array([70, 40, 90, 60, 85, 30, 95, 50])

# Sort
sorted_marks = np.sort(marks)

# Ranking
order = np.argsort(marks)
top3_indices = order[-3:]
top3_marks = marks[top3_indices]

# Failing students
fail_indices = np.where(marks < 50)
fail_marks = marks[fail_indices]

print("Sorted Marks:", sorted_marks)
print("Top 3 Students (indices):", top3_indices)
print("Top 3 Marks:", top3_marks)
print("Fail Students (indices):", fail_indices)
print("Fail Marks:", fail_marks)
