print("Le Hoa Hiep")
print("235752021610073")
from search_module import binary_search
n=int(input("Enter the number of elements in the list: "))
lst = []
for i in range (n):
    value = int(input(f"Enter the {i + 1}th element: "))
    lst.append(value)
lst.sort()
value = int(input("Nhập phần tử cần tìm: "))
found = binary_search (lst, value)
if found:
   print (f"Phần tử (value) có trong danh sách.")
else:
   print (f"Phần tử {value} không có trong danh sách.")
