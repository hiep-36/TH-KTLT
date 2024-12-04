print("Le Hoa Hiep")
print("235752021610073")
import numpy as np
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0])
sorted_indices = np.lexsort((student_id, student_height))
print("Chỉ số:", sorted_indices)
sorted_student_id = student_id[sorted_indices]
sorted_student_height = student_height[sorted_indices]
print("Chỉ số sắp xếp:", sorted_indices)
print("ID sinh viên được sắp xếp:", sorted_student_id)
print("Chiều cao sinh viên được sắp xếp:", sorted_student_height)
