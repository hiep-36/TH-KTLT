print("Le Hoa Hiep")
print("235752021610073")
import numpy as np
data_type = [('name', 'U20'), ('class', 'i4'), ('height', 'f4')]
students = np.array([
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
], dtype=data_type)
print("Mảng ban đầu:")
print(students)
sorted_students = np.sort(students, order=['class', 'height'])
print("\nMảng đã sắp xếp:")
print(sorted_students)
