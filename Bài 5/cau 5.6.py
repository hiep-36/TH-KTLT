from mymodule import sort_list, find_maximum, find_minimum
n = int(input("Nhập số lượng phần tử trong danh sách: "))
input_list = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i + 1}: "))
    input_list.append(value)
sorted_list = sort_list(input_list)
max_value = find_maximum(sorted_list)
min_value = find_minimum(sorted_list)
print("Danh sách đã sắp xếp:", sorted_list)
print("Phần tử lớn nhất là:", max_value)
print("Phần tử nhỏ nhất là:", min_value)
