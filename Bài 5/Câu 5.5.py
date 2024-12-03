print("Le Hoa Hiep")
print("235752021610073")
import random
def create_list(n):
  """Tạo một danh sách ngẫu nhiên có n phần tử"""
  return [random.randint(1, 100) for _ in range(n)]
def sort_list(list):
  """Sắp xếp danh sách tăng dần"""
  list.sort()
  return list
def find_max_min(list):
  """Tìm phần tử lớn nhất và nhỏ nhất trong danh sách"""
  return list[-1], list[0]
if __name__ == "__main__":
  n = int(input("Nhập số lượng phần tử của danh sách: "))
  my_list = create_list(n)
  print("Danh sách ban đầu:", my_list)
  sorted_list = sort_list(my_list)
  print("Danh sách đã sắp xếp:", sorted_list)
  max_value, min_value = find_max_min(sorted_list)
  print("Phần tử lớn nhất:", max_value)
  print("Phần tử nhỏ nhất:", min_value)
